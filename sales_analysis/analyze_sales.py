#!/usr/bin/env python3
"""
分析脚本：按产品类别统计 2025-10 到 2026-01 的销售变化，并输出聚合表、趋势图和简短报告。
用法示例：
python analyze_sales.py --input "2025年10月到2026年1月销售出库单数据汇总.xlsx" --output-dir output
"""
import argparse
import os
from pathlib import Path
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from dateutil.parser import parse

sns.set(style="whitegrid")

COMMON_DATE_COLS = ["日期","出库日期","单据日期","销售日期","date","Date","出库时间"]
COMMON_CATEGORY_COLS = ["产品类别","类别","类别名称","商品类别","产品分类","商品大类","category","Category","类别ID"]
COMMON_AMOUNT_COLS = ["金额","销售额","实收金额","金额(元)","总额","金额合计","amount","Amount","销售金额"]
COMMON_QTY_COLS = ["数量","数量(件)","qty","Qty","数量(kg)"]


def detect_column(df, candidates):
    for c in candidates:
        if c in df.columns:
            return c
    # fuzzy: lower-case match
    lowermap = {col.lower(): col for col in df.columns}
    for c in candidates:
        if c.lower() in lowermap:
            return lowermap[c.lower()]
    return None


def load_excel(path):
    # try reading first sheet, but allow user-specified sheet later
    df = pd.read_excel(path, engine="openpyxl")
    return df


def coerce_date(df, col):
    df[col] = pd.to_datetime(df[col], errors="coerce")
    return df


def main():
    p = argparse.ArgumentParser(description="按产品类别分析销售趋势")
    p.add_argument("--input", required=True, help="输入 Excel 文件路径")
    p.add_argument("--sheet", default=None, help="工作表名（可选）")
    p.add_argument("--output-dir", default="sales_analysis_output", help="输出目录")
    p.add_argument("--start", default="2025-10-01", help="起始日期，包含（YYYY-MM-DD）")
    p.add_argument("--end", default="2026-01-31", help="结束日期，包含（YYYY-MM-DD）")
    p.add_argument("--top-n", type=int, default=10, help="绘图时显示的前 N 类别（按总销售额）")
    args = p.parse_args()

    input_path = Path(args.input)
    out_dir = Path(args.output_dir)
    out_dir.mkdir(parents=True, exist_ok=True)

    print(f"读取: {input_path}")
    if args.sheet:
        df = pd.read_excel(input_path, sheet_name=args.sheet, engine="openpyxl")
    else:
        df = load_excel(input_path)

    print(f"原始行数: {len(df)}")

    # 自动检测列
    date_col = detect_column(df, COMMON_DATE_COLS)
    cat_col = detect_column(df, COMMON_CATEGORY_COLS)
    amt_col = detect_column(df, COMMON_AMOUNT_COLS)
    qty_col = detect_column(df, COMMON_QTY_COLS)

    if date_col is None:
        print("未能自动识别日期列。请确保文件包含日期列，或指定合适的列名。")
        print("可用列:", list(df.columns))
        return

    print(f"检测到列: 日期={date_col}, 类别={cat_col}, 金额={amt_col}, 数量={qty_col}")

    df = coerce_date(df, date_col)
    df = df.dropna(subset=[date_col])

    # 过滤日期范围
    start = pd.to_datetime(args.start)
    end = pd.to_datetime(args.end)
    mask = (df[date_col] >= start) & (df[date_col] <= end)
    df = df.loc[mask].copy()
    print(f"日期范围内行数: {len(df)}")

    # 清洗：去重
    before = len(df)
    df = df.drop_duplicates()
    print(f"去重移除: {before - len(df)} 行")

    # 类别列处理
    if cat_col is None:
        df["产品类别_detected"] = "未知"
        cat_col = "产品类别_detected"
    else:
        df[cat_col] = df[cat_col].fillna("未知")

    # 金额列处理
    if amt_col is None:
        # 尝试从其他列推断金额（如单价*数量）——未实现
        print("未检测到金额列，请确保有销售金额字段。将尝试将数量列作为金额（若存在）")
        if qty_col and qty_col in df.columns:
            amt_col = qty_col
        else:
            print("没有可用的金额/数量列，无法继续。")
            return
    df[amt_col] = pd.to_numeric(df[amt_col], errors="coerce")
    before = len(df)
    df = df.dropna(subset=[amt_col])
    print(f"移除缺失金额行: {before - len(df)} 行")

    # 数量列处理（可选）
    if qty_col and qty_col in df.columns:
        df[qty_col] = pd.to_numeric(df[qty_col], errors="coerce").fillna(0)

    # 聚合准备：按月
    df["month"] = df[date_col].dt.to_period('M').astype(str)

    # 聚合：按产品类别与月份
    agg_items = {amt_col: 'sum'}
    if qty_col and qty_col in df.columns:
        agg_items[qty_col] = 'sum'
    agg_items['month_rows'] = ('month', 'count') if False else None

    group_cols = ["产品类别_标准"] if False else None
    # 简单聚合实现：
    agg = df.groupby(["month", cat_col]).agg(
        sales_amount=(amt_col, 'sum'),
        qty=(qty_col, 'sum') if (qty_col and qty_col in df.columns) else (amt_col, 'count'),
        orders=(amt_col, 'count')
    ).reset_index()

    # 透视表：行=month, 列=category, 值=sales_amount
    pivot = agg.pivot(index='month', columns=cat_col, values='sales_amount').fillna(0)
    pivot = pivot.sort_index()

    # 计算环比变化（百分比）
    pct = pivot.pct_change().replace([np.inf, -np.inf], np.nan)

    # 保存聚合结果
    agg_csv = out_dir / 'aggregated_by_category_month.csv'
    agg.to_csv(agg_csv, index=False)
    pivot_csv = out_dir / 'sales_pivot.csv'
    pivot.to_csv(pivot_csv)
    pct_csv = out_dir / 'sales_pct_change.csv'
    pct.to_csv(pct_csv)

    print(f"已保存: {agg_csv}, {pivot_csv}, {pct_csv}")

    # 绘图：每类趋势线（若类太多则只绘前 N）
    total_by_cat = agg.groupby(cat_col)['sales_amount'].sum().sort_values(ascending=False)
    top_n = args.top_n
    top_cats = total_by_cat.head(top_n).index.tolist()

    plt.figure(figsize=(10, 6))
    for c in top_cats:
        if c in pivot.columns:
            plt.plot(pivot.index, pivot[c], marker='o', label=str(c))
    plt.xlabel('月份')
    plt.ylabel('销售金额')
    plt.title(f'按产品类别的销售趋势 (Top {len(top_cats)})')
    plt.legend(bbox_to_anchor=(1.05, 1), loc='upper left')
    plt.tight_layout()
    png = out_dir / 'sales_trends_top.png'
    plt.savefig(png)
    plt.close()

    print(f"已保存趋势图: {png}")

    # 简短报告：列出增长最快和下降最快的类别（按 2026-01 相比 2025-10）
    months = pivot.index.tolist()
    if len(months) >= 2:
        first = months[0]
        last = months[-1]
        change = (pivot[last] - pivot[first]).sort_values(ascending=False)
        change_pct = ((pivot[last] - pivot[first]) / pivot[first].replace(0, np.nan)).sort_values(ascending=False)

        report_lines = []
        report_lines.append(f"# 销售趋势简短报告\n")
        report_lines.append(f"时间范围: {start.date()} 到 {end.date()}\n")
        report_lines.append(f"样本月份: {months}\n")
        report_lines.append("\n## 销售额变化（按类别）\n")
        top_inc = change.head(10)
        top_dec = change.tail(10)

        report_lines.append("\n### 增长最多的类别（金额）\n")
        for i, (cat, val) in enumerate(top_inc.items(), 1):
            pctv = change_pct.get(cat, np.nan)
            report_lines.append(f"{i}. {cat}: 增长 {val:.2f}，环比(相对首月) {pctv:.2%}\n")

        report_lines.append("\n### 下降最多的类别（金额）\n")
        for i, (cat, val) in enumerate(top_dec.items(), 1):
            pctv = change_pct.get(cat, np.nan)
            report_lines.append(f"{i}. {cat}: 下降 {val:.2f}，环比(相对首月) {pctv:.2%}\n")

        # 保存报告
        report_path = out_dir / 'report.md'
        report_path.write_text('\n'.join(report_lines), encoding='utf-8')
        print(f"已生成报告: {report_path}")
    else:
        print("数据月份不足，无法比较首末月变化。")

    print("完成。输出目录:", out_dir)


if __name__ == '__main__':
    main()
