
<img width="64" height="64" alt="LOGO" src="https://github.com/user-attachments/assets/db792a84-9619-4b31-a838-310896e228b5" />

#  AiPy（AiPy Pro）
AiPy 是一款小白用户也能使用的通用AI智能体平台。用户无需懂编程，只需用大白话描述需求，AiPy 就能自动组建 AI 专家团队（架构师、工程师、测试、安全审计等），协作完成复杂任务。支持项目开发、数据分析、文档生成、图片制作、视频制作等场景。
- **官网：** <https://www.aipyaipy.com/>
- **下载：** <https://www.aipyaipy.com/download>
#### 1. 安装 AiPy
请从 [AiPy 官网](https://www.aipyaipy.com/download) 下载对应平台的安装包：
- Windows（`.exe`）
- macOS（`.dmg`，支持 Intel 与 Apple Silicon）
安装完成后启动 AiPy，进入主界面。
#### 2. 配置 DeepSeek 模型服务
AiPy 原生支持 OpenAI 兼容接口，可直接接入 DeepSeek 模型。
1. 在 AiPy 主界面中，点击左下角的 **设置** 图标。
2. 在导航中打开 **模型**，点击 **添加**。
3. 选择模型提供商 **DeepSeek官方** 类型，会自动填写Base Url，手动填写下方内容即可：
   
| 配置项 | 值 |
|--------|-----|
| **名称** | `DeepSeek` |
| **API 密钥** | 你的 [DeepSeek API Key](https://platform.deepseek.com/api_keys) |
| **模型** | `deepseek-v4-pro` |
4. 保存配置，DeepSeek 即可在 AiPy 中使用，也可点击设为默认，将DeepSeek模型设置为默认使用模型。

#### 3. 开始使用
配置完成后，在 AiPy 主界面的对话框中：
1. 用大白话描述你的需求，右侧模型处选择DeepSeek模型，（如果上一步骤中已经设为默认，则默认为DeepSeek模型）例如：
   - "帮我写个俄罗斯方块"
   - "帮我分析这份 Excel 销售数据，找出增长最快的产品"
   - "帮我把这 100 个文件按日期重命名"
   - "帮我写一份年终总结 PPT"
2. AiPy 会自动组建专家团队，分步骤完成任务。

#### 4. 进阶用法
完成 DeepSeek 配置后，你可以在 AiPy 的以下场景中充分发挥其能力：
- **数据分析**：上传 Excel/CSV 文件，AiPy 会自动调用 DeepSeek 进行数据解读、趋势分析、图表生成。
- **文档生成**：输入需求描述，AiPy 通过DeepSeek的任务规划能力调用工具结合生成 Word、PDF、PPT、HTML 报告等格式的文档。
#### 5. 模型选择建议
| 场景 | 推荐模型 | 说明 |
|------|----------|------|
| 复杂数据分析、多步骤任务 | `deepseek-v4-pro` | 最强推理能力，支持深度思考 |
| 简单问答、快速响应 | `deepseek-v4-flash` | 速度快、成本低 |
| 代码生成与调试 | `deepseek-v4-pro` | 支持 Tool Calls，可调用外部工具 |
