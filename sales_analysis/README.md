说明

此文件夹包含一个可在本地运行的脚本，用于分析 2025-10 到 2026-01 的销售出库单，按产品类别聚合并生成趋势图与简短报告。

准备

1. 将 Excel 文件放在本机某处（例如桌面）。
2. 在本项目根目录运行以下命令以创建虚拟环境并安装依赖：

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r sales_analysis/requirements.txt
```

运行

```bash
python sales_analysis/analyze_sales.py --input "/path/to/2025年10月到2026年1月销售出库单数据汇总.xlsx" --output-dir sales_output
```

输出

- sales_output/aggregated_by_category_month.csv：按类别与月份的明细聚合
- sales_output/sales_pivot.csv：月份×类别 的透视表（销售金额）
- sales_output/sales_pct_change.csv：环比变化表
- sales_output/sales_trends_top.png：按类别的趋势图（默认显示总额前10类别）
- sales_output/report.md：简短的文本报告，总结增长/下降类别

说明与提示

- 脚本会尝试自动识别常见列名（中文/英文），若无法识别请在 Excel 中确认列名或在运行时先打开文件并重命名列。
- 若你希望我代为运行并生成结果，请把文件上传到工作区路径（例如 sales_analysis/input.xlsx），我会直接处理并返回结果。
