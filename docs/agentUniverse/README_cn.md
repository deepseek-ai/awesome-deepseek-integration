___
<img src="assets/agentUniverse_logo.jpg" width="auto" height="auto" />

___

# [agentUniverse](https://github.com/antgroup/agentUniverse)

agentUniverse 是一个面向复杂业务场景设计的多智能体协作框架。其提供了快速易用的大模型智能体应用搭建能力，并着重于提供智能体协同调度、自主决策与动态反馈等机制，其源自蚂蚁集团在金融领域的真实业务实践沉淀。agentUniverse于2024年6月全面接入支持deepseek系列模型。

## 设计理念

<img src="https://raw.githubusercontent.com/antgroup/agentUniverse/refs/heads/master/docs/guidebook/_picture/agentuniverse_structure.png" />

## 在项目中使用 deepseek API

### 通过python代码配置
必须配置：DEEPSEEK_API_KEY  
可选配置：DEEPSEEK_API_BASE
```python
import os
os.environ['DEEPSEEK_API_KEY'] = 'sk-***'
os.environ['DEEPSEEK_API_BASE'] = 'https://xxxxxx'
```
### 通过配置文件配置
在项目的config目录下的custom_key.toml当中，添加配置：
```toml
DEEPSEEK_API_KEY="sk-******"
DEEPSEEK_API_BASE="https://xxxxxx"
```

更多使用详情可参阅[官方文档:DeepSeek接入使用](https://github.com/antgroup/agentUniverse/blob/master/docs/guidebook/zh/In-Depth_Guides/%E7%BB%84%E4%BB%B6%E5%88%97%E8%A1%A8/%E6%A8%A1%E5%9E%8B%E5%88%97%E8%A1%A8/DeepSeek%E4%BD%BF%E7%94%A8.md)

