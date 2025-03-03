___
<img src="assets/agentUniverse_logo.jpg" width="auto" height="auto" />

___

# [agentUniverse](https://github.com/antgroup/agentUniverse)

agentUniverse is a multi-agent collaboration framework designed for complex business scenarios. It offers rapid and user-friendly development capabilities for LLM agent applications, with a focus on mechanisms such as agent collaborative scheduling, autonomous decision-making, and dynamic feedback. The framework originates from Ant Group's real-world business practices in the financial industry. In June 2024, agentUniverse achieved full integration support for the DeepSeek series of models.

## Concepts

<img src="https://raw.githubusercontent.com/antgroup/agentUniverse/refs/heads/master/docs/guidebook/_picture/agentuniverse_structure_en.png" />

## Integrate with Deepseek API

### Configure via Python code
```python
import os
os.environ['DEEPSEEK_API_KEY'] = 'sk-***'
os.environ['DEEPSEEK_API_BASE'] = 'https://xxxxxx'
```
### Configure via the configuration file
In the custom_key.toml file under the config directory of the project, add the configuration:
```toml
DEEPSEEK_API_KEY="sk-******"
DEEPSEEK_API_BASE="https://xxxxxx"
```

For more details, please refer to the [Documentation: DeepSeek Integration](https://github.com/antgroup/agentUniverse/blob/master/docs/guidebook/en/In-Depth_Guides/Components/LLMs/DeepSeek_LLM_Use.md)

