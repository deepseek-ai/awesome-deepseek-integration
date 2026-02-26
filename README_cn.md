<div align="center">

<p align="center">
<img width="1280" alt="Awesome DeepSeek Integrations" src="docs/Awesome DeepSeek Integrations.png">
</p>

# DeepSeek 实用集成 ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

将 DeepSeek 大模型能力轻松接入各类软件。访问 [DeepSeek 开放平台](https://platform.deepseek.com/) 来获取您的 API key。

[English](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/README.md) / 简体中文 / [繁体中文](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/README_zh_tw.md) / [日本語](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/README_ja.md) / [Español](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/README_es.md)

</div>

<br></br>

## 目录

- [DeepSeek 实用集成 ](#deepseek-实用集成-)
  - [目录](#目录)
  - [项目列表](#项目列表)
    - [应用程序](#应用程序)
    - [AI Agent 框架](#ai-agent-框架)
    - [AI数据应用框架](#ai数据应用框架)
    - [RAG 框架](#rag-框架)
    - [FHE (全同态加密) frameworks](#fhe-全同态加密-frameworks)
    - [Solana 框架](#solana-框架)
    - [综合数据管理](#综合数据管理)
    - [即时通讯插件](#即时通讯插件)
    - [Office插件](#office插件)
    - [浏览器插件](#浏览器插件)
    - [VS Code 插件](#vs-code-插件)
    - [neovim 插件](#neovim-插件)
    - [JetBrains 插件](#jetbrains-插件)
    - [AI Code编辑器](#ai-code编辑器)
    - [安全](#安全)
    - [其它](#其它)

## 项目列表

###  <span id="applications">应用程序</span>

<table>
    <tr>
        <td><img src="docs/ETOS-LLM-Studio/assets/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="docs/ETOS-LLM-Studio/README.md">ETOS LLM Studio</a></td>
        <td>ETOS LLM Studio (ELS) 是一款专为 watchOS 与 iOS 深度定制的旗舰级 AI 客户端。它拥有“腕上智核”的独立交互体验、极简的律动美学设计以及全端联动的无缝体验。支持 DeepSeek 等多种模型，重塑你手腕上的 AI 交互维度。</td>
    </tr>
    <tr>
        <td><img src="docs/operit/assets/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/AAswordman/Operit">Operit AI</a></td>
        <td>面向安卓平台的开源系统集成化ai助手，支持几乎完整的mcp使用，高度兼容安卓系统。软件同时具备高度自定义和上手低门槛，内置文件操作/搜索/自动点击/格式转换等工具调用，并内置deepseek api网页。</td>
    </tr>
    <tr>
        <td><img src="docs/openEuler Intelligence/intelligence_icon.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://www.openeuler.org/zh/projects/intelligence/">openEuler Intelligence</a></td>
        <td>基于 openEuler 的大模型智能平台，深度整合了包括 DeepSeek 在内的主流大语言模型，并具备本地知识库构建能力。平台提供语义接口注册、MCP 服务管理、智能体（Agent）开发及自动化工作流编排等核心功能，同时支持 Web 端和桌面客户端双模式访问，显著提升开发效率与企业级应用体验！</td>
    </tr>
    <tr>
        <td><img src="docs/hh-wserver/wserver.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/hzmosi/ai-wechat">微信RPA智能客服</a></td>
        <td>AI双擎-微信智能客服。内置Deepseek官方API及阿里百炼Deepseek API，AI服务不可用时无缝自动切换，全天持续稳定运行！本工具通过RPA自动化实现，不访问私有接口。</td>
    </tr>
    <tr>
        <td><img src="docs/OpenXLab/migo/logo.svg" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://migo.intern-ai.org.cn/">觅果</a></td>
        <td>免费的 AI 创新加速工具，提供智能问答、论文深度理解、前沿 AI 工具以及个人学术知识库。作为探索的伙伴，觅果助你发现并实现卓越创意！</td>
    </tr>
    <tr>
        <td><img src="docs/eechat/assets/logo.svg" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/Lucassssss/eechat">eechat</a></td>
        <td>简洁易用的大模型本地部署工具，支持开源模型 DeepSeek-R1， DLlama 3, Phi-4, Mistral, Gemma 3 等模型的本地化隐私部署，同时支持远程大模型API调用。</td>
    </tr>
    <tr>
        <td><img src="docs/aingdesk/assets/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/aingdesk/AingDesk">AingDesk</a></td>
        <td>一键把AI模型部署在你电脑，操作可视化，内置精美聊天界面，可在线分享他人共用，支持 DeepSeek 等其他模型，支持联网搜索和第三方API</td>
    </tr>
    <tr>
        <td><img src="docs/dingtalk/assets/dingtalk_icon.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://www.dingtalk.com/">钉钉</a></td>
        <td>钉钉 AI 助理，它融合了钉钉平台的多项 AI 产品功能，以智能化的方式辅助企业日常的工作流程。钉钉 AI 助理具备多种智能能力，包括但不限于智能沟通、智能协同、智能管理等。通过这些功能，AI 助理能够在企业内部中归纳要点、生成会议纪要，并且能够为用户推送相关工作任务和日程提醒。此外，钉钉 AI 助理还能够通过知识库的能力智能地回答员工企业的行政流程、人力资源政策等多个方面的常见问题。</td>
    </tr>
    <tr>
        <td><img src="https://github.com/mrzhang1013/CodingSee/blob/main/codingseeicon.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://www.codingsee.com">CodingSee-AI伴学</a></td>
        <td>CodingSee是一款专为中国少儿编程设计的软件，内容包含社区，项目协作，站内实时消息，AI问答，Scratch/Python/C++编译环境，代码精准纠错的集成平台，UI设计友好，目前支持Windows和mac系统。</td>
    </tr>
    <tr>
        <td><img src="https://chatdoc.com/chatdoc/chatdoc.webp" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://chatdoc.com">ChatDOC</a></td>
        <td>ChatDOC是一款AI文档阅读工具，具备强大的溯源功能，确保每一条信息的来源清晰可查，助您高效、精准地掌握文档核心。</td>
    </tr>
    <tr>
        <td> <img src="./docs/SwiftChat/assets/favicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/SwiftChat/README_cn.md">SwiftChat</a></td>
        <td> <a href="https://github.com/aws-samples/swift-chat">SwiftChat</a> 是一款使用 React Native 构建的闪电般快速的跨平台 AI 聊天应用。它在 Android、iOS 和 macOS 上提供原生性能。功能包括实时流式聊天、丰富的 Markdown 支持、AI 图像生成、可自定义系统提示、快速切换模型和多模态能力。支持 DeepSeek、Amazon Bedrock、Ollama 和 OpenAI API 兼容的模型，并具有简洁的用户界面和高性能表现。</td>
    </tr>
    <tr>
        <td><img src="https://4everlogo.4everland.store/logo/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/4EVERChat/README_cn.md">4EVERChat</a></td>
        <td><a href="https://chat.4everland.org/">4EVERChat</a> 是集成数百款LLM的智能模型选型平台，支持直接对比不同模型的实时响应差异，基于<a href="https://www.4everland.org/">4EVERLAND</a> AI RPC 统一API端点实现零成本模型切换，自动选择响应快、成本低的模型组合。</td>
    </tr>
    <tr>
        <td><img src="./docs/xhai_browser/assets/logo_512.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="./docs/xhai_browser/README_cn.md">小海浏览器</a></td>
        <td>小海浏览器是安卓桌面管理&AI浏览器,DeepSeek是默认AI对话引擎.他有极致的性能(0.2秒启动),苗条的体型(apk 3M大),无广告,超高速广告拦截,多屏分类,屏幕导航,多搜索框,一框多搜</td>
    </tr>
    <tr>
        <td> <img src="./docs/gptbots/gptbots.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.gptbots.ai/zh_CN/docs">GPTBots</a> </td>
        <td> <a href="https://www.gptbots.ai/zh_CN">GPTBots</a> 是一个无代码的 AI Agent 构建平台，集成了包括 Deepseek 在内的国际主流 LLM，并提供了基于 RAG 的知识存储/检索，工具自定义/调用，工作流编排等模块，并可将 Agent 集成至多个主流平台（WhatsApp、Telegram 等），为企业提供端到端的 AI 解决方案，助力企业在 AI 时代脱颖而出。</td>
    </tr>
    <tr>
        <td><img src="https://github.com/ThinkInAIXYZ/deepchat/blob/main/build/icon.png?raw=true" alt="Icon" width="64" height="auto" style="border-radius: 10px" /></td>
        <td><a href="https://github.com/ThinkInAIXYZ/deepchat/blob/main/README.md">DeepChat</a></td>
        <td>DeepChat 是一款完全免费的桌面端智能助手，内置强大的 DeepSeek 大模型，支持多轮对话、联网搜索、文件上传、知识库等多种功能。</td>
    </tr>
    <tr>
        <td></td>
        <td> <a href="https://github.com/wangrongding/wechat-bot/blob/main/README.md"> Wechat-Bot </a></td>
        <td> 基于 wechaty 实现的微信机器人，结合了 DeepSeek 和其他 Ai 服务。 </td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/171659527?s=400&u=39906ab3b6e2066f83046096a66a77fb3f8bb836&v=4" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/quantalogic/quantalogic">Quantalogic</a> </td>
        <td> QuantaLogic 是一个 ReAct（推理和行动）框架，用于构建高级 AI 代理。 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/13600976/224d547a-6fbc-47c8-859f-aa14813e2b0f" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/chatbox/README_cn.md">Chatbox</a> </td>
        <td> 一个支持多种流行LLM模型的桌面客户端，可在 Windows、Mac 和 Linux 上使用 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/bb65404c-f867-42d8-ae2b-281fe953ab54" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/chatgpt_next_web/README_cn.md"> ChatGPT-Next-Web </a> </td>
        <td> 一键获取跨平台ChatGPT网页用户界面，支持流行的LLM </td>
    </tr>
    <tr>
        <td> <img src="docs/Casibase/assets/casibase.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://casibase.org/zh/docs/category/beginner-guide/">Casibase</a></td>
        <td> <a href="https://casibase.org">Casibase</a> 是一个开源的 AI 知识库和对话系统，它结合了最新的 RAG 技术、SSO 功能，并支持各种主流 AI 模型。旨在为企业和开发者提供一个功能强大、灵活易用的知识管理和智能对话平台。 </td>
    </tr>
    <tr>
        <td> <img src="docs/Coco AI/assets/favicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/Coco AI/README_cn.md">Coco AI</a></td>
        <td> <a href="https://coco.rs">Coco AI</a> 是一个完全开源、跨平台的统一搜索与效率工具，能够连接并搜索多种数据源，包括应用程序、文件、谷歌网盘、Notion、语雀、Hugo 等本地与云端数据。通过接入 DeepSeek 等大模型，Coco AI 实现了智能化的个人知识库管理，注重隐私，支持私有部署，帮助用户快速、智能地访问信息。 </td>
    </tr>
    <tr>
        <td> <img src="docs/liubai/assets/liubai-logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/liubai/README_cn.md">留白记事</a> </td>
        <td> 留白让你直接在微信上使用 DeepSeek 管理你的笔记、任务、日程和待办清单！ </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/1ac9791b-87f7-41d9-9282-a70698344e1d" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/pal/README_cn.md"> Pal - AI Chat Client<br/>(iOS, ipadOS) </a> </td>
        <td> 一款可以在 iPhone 或 iPad 上使用的 AI 助手 </td>
    </tr>
    <tr>
        <td> <img src="https://www.librechat.ai/librechat.svg" alt="LibreChat" width="64" height="auto" /> </td>
        <td> <a href="https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/deepseek">LibreChat</a> </td>
        <td> LibreChat 是一个可定制的开源应用程序，无缝集成了 DeepSeek，以增强人工智能交互体验 </td>
    </tr>
    <tr>
        <td> <img src="https://www.papersgpt.com/images/logo/favicon.ico" alt="PapersGPT" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/papersgpt/papersgpt-for-zotero">PapersGPT</a> </td>
        <td> PapersGPT是一款集成了DeepSeek及其他多种AI模型的辅助论文阅读的Zotero插件。 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/rss-translator/RSS-Translator/main/core/static/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/rss_translator/README_cn.md"> RSS翻译器 </a> </td>
        <td> 开源、简洁、可自部署的RSS翻译器 </td>
    </tr>
    <tr>
        <td> <img src="https://relingo.net/assets/images/relingo-logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://relingo.net"> Relingo </a> </td>
        <td> 在浏览网站和观看 YouTube 视频时，轻松构建和掌握词汇！ </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/ysnows/enconvo_media/main/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/enconvo/README_cn.md"> Enconvo </a> </td>
        <td> Enconvo是AI时代的启动器,是所有AI功能的入口,也是一位体贴的智能助理。 </td>
    </tr>
    <tr>
        <td><img src="https://github.com/kangfenmao/cherry-studio/blob/main/src/renderer/src/assets/images/logo.png?raw=true" alt="Icon" width="64" height="auto" style="border-radius: 10px" /></td>
        <td><a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/cherrystudio/README_cn.md">Cherry Studio</a></td>
        <td> 一款为创造者而生的桌面版 AI 助手 </td>
    </tr>
    <tr>
        <td> <img src="https://tomemo.top/images/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/tomemo/README_cn.md"> ToMemo (iOS, ipadOS) </a> </td>
        <td> 一款短语合集 + 剪切板历史 + 键盘输出的iOS应用，集成了AI大模型，可以在键盘中快速输出使用。 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/buxuku/video-subtitle-master/refs/heads/main/resources/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/buxuku/video-subtitle-master">Video Subtitle Master</a></td>
        <td> 批量为视频生成字幕，并可将字幕翻译成其它语言。这是一个客户端工具, 跨平台支持 mac 和 windows 系统, 支持百度，火山，deeplx, openai, deepseek, ollama 等多个翻译服务 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/icon_512x512@2x.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/tisfeng/Easydict">Easydict</a></td>
        <td> Easydict 是一个简洁易用的词典翻译 macOS App，能够轻松优雅地查找单词或翻译文本，支持调用大语言模型 API 翻译。 </td>
    </tr>
    <tr>
        <td> <img src="https://www.raycast.com/favicon-production.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/raycast/README_cn.md">Raycast</a></td>
        <td> <a href="https://raycast.com/?via=ViGeng">Raycast</a> 是一款 macOS 生产力工具，它允许你用几个按键来控制你的工具。它支持各种扩展，包括 DeepSeek AI。 </td>
    </tr>
    <tr>
        <td> <img src="./docs/chatpdflocal/assets/chatpdflocal-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.chatpdflocal.com">ChatPDFLocal</a> </td>
        <td> ChatPDFLocal 是一款基于AI的Mac OS App，可以帮助您与PDF互动，可以帮助您快速地理解PDF，它集成了DeepSeek及其他多种AI模型旨在提高您的阅读效率。</td>
    </tr>
    <tr>
        <td> <img src="docs/zotero/assets/zotero-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/zotero/README_cn.md">Zotero</a></td>
        <td> <a href="https://www.zotero.org">Zotero</a> 是一款免费且易于使用的文献管理工具，旨在帮助您收集、整理、注释、引用和分享研究成果。 </td>
    </tr>
    <tr>
        <td> <img src="https://b3log.org/images/brand/siyuan-128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/SiYuan/README_cn.md">思源笔记</a> </td>
        <td> 思源笔记是一款隐私优先的个人知识管理系统，支持完全离线使用，并提供端到端加密的数据同步功能。 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/ArvinLovegood/go-stock/raw/master/build/appicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/ArvinLovegood/go-stock/blob/master/README.md">go-stock</a> </td>
        <td> go-stock 是一个由 Wails 使用 NativeUI 构建并由 LLM 提供支持的股票数据查看分析器。 </td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/102771702?s=200&v=4" alt="Wordware" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-php/deepseek-wordware/blob/master/README.md">Wordware </a> </td>
        <td><a href="https://www.wordware.ai/">Wordware</a> 这是一个工具包，使任何人都可以仅通过自然语言构建、迭代和部署他们的AI堆栈 </td>
    </tr>
    <tr>
        <td> <img src="https://framerusercontent.com/images/xRJ6vNo9mUYeVNxt0KITXCXEuSk.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/langgenius/dify/">Dify</a> </td>
        <td> <a href="https://dify.ai/">Dify</a> 是一个支持 DeepSeek 模型的 LLM 应用开发平台，可用于创建 AI 助手、工作流、文本生成器等应用。 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/LiberSonora/LiberSonora/blob/main/assets/avatar.jpeg?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/LiberSonora/LiberSonora">LiberSonora</a> </td>
        <td> LiberSonora，寓意"自由的声音"，是一个 AI 赋能的、强大的、开源有声书工具集，包含智能字幕提取、AI标题生成、多语言翻译等功能，支持 GPU 加速、批量离线处理 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/ripperhe/Bob/master/docs/_media/icon_128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://bobtranslate.com/">Bob</a></td>
        <td> <a href="https://bobtranslate.com/">Bob</a> 是一款 macOS 平台的翻译和 OCR 软件，您可以在任何应用程序中使用 Bob 进行翻译和 OCR，即用即走！ </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/STranslate/STranslate/refs/heads/main/images/favicon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://stranslate.zggsong.com/">STranslate</a></td>
        <td> <a href="https://stranslate.zggsong.com/">STranslate</a>（Windows） 是 WPF 开发的一款即用即走的翻译、OCR工具 </td>
    </tr>
    <tr>
        <td> <img src="https://www.gptaiflow.tech/logo.png" alt="gpt-ai-flow-logo" width="64" height="auto" /> </td>
        <td> <a href="https://www.gptaiflow.tech/zh/docs/product/api-keys-setup#setup-deepseek-api-keys">GPT AI Flow</a></td>
        <td>
            工程师为效率狂人（他们自己）打造的终极生产力武器: <a href="https://www.gptaiflow.tech/zh/">GPT AI Flow</a>
            <ul>
                <li>`Shift+Alt+空格` 唤醒桌面智能中枢</li>
                <li>本地加密存储</li>
                <li>自定义指令引擎</li>
                <li>按需调用拒绝订阅捆绑</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/b09f17a8-936d-4dac-8b24-1682d52c9a3c" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/alecm20/story-flicks">Story-Flicks</a></td>
        <td> 通过一句话即可快速生成高清故事短视频，支持 DeepSeek 等模型。 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/Alpha派/assets/favicon1.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/Alpha派/README_cn.md"> Alpha派 </a> </td>
        <td> AI投研助理/AI驱动的新一代金融信息入口。代理投资者听会/记纪要，金融投资信息的搜索问答/定量分析等投资研究工作。 </td>
    </tr>
    <tr>
        <td> <img src="https://docs.xark-argo.com/img/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.xark-argo.com">argo</a> </td>
        <td> 本地下载并运行Huggingface及Ollama模型，支持RAG、LLM API、工具接入等，支持Mac/Windows/Linux。 </td>
    </tr>
    <tr>
        <td> <img src="https://5ire.app/favicon.ico" alt="5ire-logo" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/nanbingxyz/5ire">5ire</a> </td>
        <td> <a href="https://github.com/nanbingxyz/5ire">5ire</a>是一款设计友好的跨平台开源桌面智能助手，兼容市面主流的大模型，支持 MCP Servers，本地知识库、提示词库及众多实用功能。 </td>
    </tr>
    <tr>
        <td> <img src="https://www.petercat.ai/images/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.petercat.ai">PeterCat</a> </td>
        <td> 我们提供对话式答疑 Agent 配置系统、自托管部署方案和便捷的一体化应用 SDK，让您能够为自己的 GitHub 仓库一键创建智能答疑机器人，并快速集成到各类官网或项目中， 为社区提供更高效的技术支持生态。 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/labring/FastGPT/refs/heads/main/.github/imgs/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://fastgpt.cn/zh">FastGPT</a> </td>
        <td>
            FastGPT 基于 LLM 大模型的开源 AI 知识库构建平台，支持 DeepSeek、OpenAI 等多种模型。我们提供了开箱即用的数据处理、模型调用、RAG 检索、可视化 AI 工作流编排等能力，帮助您轻松构建复杂的 AI 应用。
        </td>
    </tr>
    <tr>
        <td> <img src="https://cdn.link-ai.tech/doc/CoW%20logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/zhayujie/chatgpt-on-wechat">Chatgpt-on-Wechat</a> </td>
        <td> Chatgpt-on-Wechat（CoW）项目是一个灵活的聊天机器人框架，支持将DeepSeek、OpenAI、Claude、Qwen等多种LLM 一键接入到微信公众号、企业微信、飞书、钉钉、网站等常用平台或办公软件，并支持丰富的自定义插件。 </td>
    </tr>
    <tr>
        <td> <img src="./docs/ruzhiai_note/assets/play_store_512.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/ruzhiai_note/README_cn.md">如知AI笔记</a> </td>
        <td>如知AI笔记是一款智能化的AI知识管理工具，致力于为用户提供一站式的知识管理和应用服务，包括AI搜索探索、AI结果转笔记、笔记管理与整理、知识演示与分享等。集成了DeepSeek深度思考模型，提供更稳定、更高质量的输出。</td>
    </tr>
    <tr>
        <td> <img src="https://athenalab.ai/assets/favicon/favicon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://athenalab.ai/">Athena</a> </td>
        <td>世界上首个具有先进认知架构和类人推理能力的自主通用人工智能，旨在解决复杂的现实世界挑战。</td>
    </tr>
    <tr>
        <td> <img src="./docs/TigerGPT/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.laohu8.com/gpt">TigerGPT</a> </td>
        <td>TigerGPT 是老虎集团开发的，业内首个基于 OpenAI 的金融 AI 投资助理。TigerGPT 旨在为投资者提供智能化的投资决策支持。2025年2月18日，TigerGPT 正式接入 DeepSeek-R1 模型，为用户提供支持深度推理的在线问答服务。 </td>
    </tr>
    <tr>
        <td> <img src="./docs/HIX.AI/assets/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://hix.ai">HIX.AI</a> </td>
        <td>免费试用 DeepSeek，在 HIX.AI 上享受无限量的 AI 聊天。使用 DeepSeek R1 进行 AI 聊天、写作、编码等。立即体验下一代 AI 聊天！</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/sharmt1411/askanywhere/blob/main/icon/Depth_8,_Frame_0explore-%E8%A7%92%E6%A0%87.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/sharmt1411/askanywhere">划词AI助手</a> </td>
        <td>一个划词ai助手，在任何地方划词，快速打开与Deepseek的对话！</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/OJZen/1chat/raw/refs/heads/main/doc/assets/icon.ico?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/OJZen/1chat">1查</a> </td>
        <td>一款能让你在本地运行 DeepSeek 的 iOS 应用</td>
    </tr>
    <tr>
        <td> <img src="https://chatlabsai.com/assets/logo/logo.png" alt="iOS AI 聊天机器人" width="64" height="auto" /> </td>
        <td> <a href="https://chatlabsai.com">在一个应用中访问250多个文本、图像大模型</a> </td>
        <td> 1AI iOS聊天机器人集成了250多个文本、图像、语音模型，让用户可以与OpenRouter、Replicate上的任何模型对话，包括Deepseek推理和Deepseek V3模型。</td>
    </tr>
    <tr>
        <td> <img src="./docs/PopAi/assets/logo.svg" alt="PopAi" width="64" height="auto" /> </td>
        <td> <a href="https://popai.pro">PopAi</a> </td>
        <td>PopAi推出DeepSeek R1！享受无延迟、闪电般快速的性能，尽在PopAi。轻松切换在线搜索开/关。</td>
    </tr>
    <tr>
        <td> <img src="https://pot-app.com/logo/icon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://pot-app.com/">Pot</a></td>
        <td> <a href="https://pot-app.com/">Pot</a> 🌈一个跨平台的划词翻译和OCR软件 </td>
    </tr>
    <tr>
        <td><img src="https://github.com/Byaidu/PDFMathTranslate/raw/main/docs/images/banner.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/Byaidu/PDFMathTranslate">PDFMathTranslate</a></td>
        <td>PDFMathTranslate是一款基于 AI 完整保留排版的 PDF 文档全文双语翻译工具。</td>
    </tr>
    <tr>
        <td><img src="https://github.com/Richasy/Bili.Copilot/raw/master/assets/StoreLogo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/Richasy/Bili.Copilot">哔哩助理</a></td>
        <td>B站第三方 Windows 桌面客户端，使用 Windows App SDK 构建的原生应用。</td>
    </tr>
    <tr>
        <td><img src="https://www.tensorbounce.com/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://www.tensorbounce.com/">LawAgent</a></td>
        <td>LawAgent是tensorbounce团队出品的知识库结合AI Agent的法律AI产品,拥有上千万官方法律相关知识库数据，用户可自定义知识库，专业模式结合DeepSeek-R1的推理能力应用在用户的法律分析、合同审查、文书生成、文件翻译等法律场景。</td>
    </tr>
    <tr>
        <td><img src="https://h1.appinn.me/file/1741929316827_21.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/jiqi136/DS-AI">实时联网AI助手</a></td>
        <td>AI助手支持DeepSeek-V3.1接口直连最强Claude Code代码模型，无需网络中转即可使用（成本直降90%）。 支持图片、PDF文件读取及免费生成图片；可自定义接入其他AI模型；支持调用本地浏览器实时联网检索海量网页内容。另提供R1等免费模型选择。</td>
    </tr>
    <tr>
        <td width=80> <img src="docs/AlphaBot/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://alphabot.x-pai.com/">AlphaBot</a> </td>
        <td> AlphaBot是一款智能股票分析助手，整合多源数据与AI分析技术，提供技术分析、预测和风险评估功能，帮助投资者做出数据驱动的交易决策。支持一键部署，操作简便，支持Windows/Linux/MacOS等平台</td>
    </tr>
    <tr>
        <td><img src="docs/remio/assets/remio_icon.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://www.remio.ai/">remio</a></td>
        <td>remio 是一个 AI 驱动的个人知识中心，通过自动捕获浏览的网页内容、解析本地文件并整合个人笔记，构建个性化的知识库。它支持在个人知识库中进行搜索和自然语言问答，以提供即时洞察，同时提供智能写作辅助——适应您的写作风格，轻松简化起草、润色和完成内容的过程。remio 采用本地优先存储设计，优先保护数据隐私，同时集中管理零散信息，以实现最大化的生产力。</td>
    </tr>
    <tr>
        <td><img src="docs/DocKit/assets/dockit.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://dockit.geekfun.club/">DocKit</a></td>
        <td>DocKit是一款由AI驱动的桌面GUI客户端，专为NoSQL数据库设计，支持Mac、Windows和Linux操作系统上的Elasticsearch和OpenSearch。通过集成DeepSeek等大型模型，DocKit可以帮助开发者编写复杂的DSL查询，并提升数据管理和分析的用户体验。</td>
    </tr>
    <tr>
        <td> <img src="docs/zenfeed/assets/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/glidea/zenfeed">zenfeed</a> </td>
        <td> 用 AI 赋能 RSS，自动筛选、总结、推送重要信息，告别信息过载。 </td>
    </tr>
    <tr>
        <td> <img src="docs/NoteGen/NoteGen.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/codexu/note-gen">NoteGen</a> </td>
        <td> NoteGen 是一款的跨端的 Markdown 笔记应用，致力于使用 AI 建立记录和写作的桥梁，将碎片化知识整理成一篇可读的笔记。 </td>
    </tr>
    <tr>
        <td></td>
        <td> <a href="https://github.com/SamYuan1990/i18n-agent-action">i18n-agent-action</a> </td>
        <td> i18n Agent是一款人工智能驱动的工具，旨在简化和自动化国际化（i18n）与本地化（l10n）工作流程。它通过先进的自然语言处理（NLP）和机器学习技术，帮助开发者、翻译人员和产品团队高效管理多语言内容——既能消除人工错误，又能加速全球部署进程。 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/obot-platform/obot/refs/heads/main/docs/static/img/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/obot-platform/obot">Obot</a> </td>
        <td> Obot 是一个用于构建和部署 AI 助手的智能体平台，内置 RAG、工作流自动化，并可与流行工具和服务无缝集成，支持 DeepSeek 等大语言模型。 </td>
    </tr>
    <tr>
        <td> <img src="https://3min.top/imgs/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://3min.top/zh">3mintop</a> </td>
        <td> 一个强大的AI驱动工具，帮助您在3分钟内快速总结和理解任何内容，支持DeepSeek模型以增强理解能力。 </td>
    </tr>
    <tr>
        <td> <img src="https://cantian.ai/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://cantian.ai/">参天AI</a></td>
        <td>基于高质量数据集打造的八字命理AI</td>
    </tr>
    <tr>
        <td> <img src="https://obsidian.md/favicon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/TarsLab/obsidian-tars">Obsidian Tars</a></td>
        <td> 把大模型对话融入到 Obsidian 的笔记编辑, deepseek-reasoner 的思维链以 callout 格式输出。 </td>
    </tr>
    <tr>
        <td> <img src="https://www.chatbotbuilder.dev/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/bobbylkchao/chatbotBuilder">AI Chatbot Builder</a> </td>
        <td> <a href="www.chatbotbuilder.dev/">Chatbot Builder</a> 是一个开源平台，集成了 DeepSeek 和 OpenAI模型，允许用户为不同的对话场景创建定制化的聊天机器人。通过低代码和可配置的方式，轻松构建智能对话体验。</td>
    </tr>
    <tr>
        <td> <img src="https://bibigpt.co/icons/lucid/icon_32x32@2x.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="http://bibigpt.co">BibiGPT</a> </td>
        <td> <a href="http://bibigpt.co">BibiGPT</a> 是一款AI音视频助理，支持B站、油管、小红书、小宇宙播客等主流平台的内容分析和总结，让音视频看得快、搜得到、用得好。提供内容摘要、智能问答和文章生成等功能。支持视频文件上传、笔记应用集成和DeepSeek R1及V3模型。 </td>
    </tr>
    <tr>
        <td> <img src="https://lobehub.com/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://lobehub.com/zh/docs/usage/providers/deepseek">LobeChat</a> </td>
        <td> <a href="https://lobehub.com">LobeChat</a> - 一款开源的现代化 AI 对话框架。支持 DeepSeek R1、知识库（文件上传/知识管理/RAG）、多模态能力（视觉/语音合成/插件/创作）。一键免费部署专属 DeepSeek 应用，打造您的私人 AI 助手。</td>
    </tr>
    <tr>
        <td> <img src="./docs/ruzhiai_note/assets/play_store_512.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/ruzhiai_note/README_cn.md">如知AI笔记</a> </td>
        <td>如知AI笔记是一款智能化的AI知识管理工具，致力于为用户提供一站式的知识管理和应用服务，包括AI搜索探索、AI结果转笔记、笔记管理与整理、知识演示与分享等。集成了DeepSeek深度思考模型，提供更稳定、更高质量的输出。</td>
    </tr>
    <tr>
        <td> <img src="https://cdn.link-ai.tech/doc/CoW%20logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/zhayujie/chatgpt-on-wechat">Chatgpt-on-Wechat</a> </td>
        <td> Chatgpt-on-Wechat（CoW）项目是一个灵活的聊天机器人框架，支持将DeepSeek、OpenAI、Claude、Qwen等多种LLM 一键接入到微信公众号、企业微信、飞书、钉钉、网站等常用平台或办公软件，并支持丰富的自定义插件。 </td>
    </tr>
    <tr>
        <td> <img src="https://www.weiyuai.cn/logo.png" alt="AI Customer Service" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Bytedesk/bytedesk">微语</a> </td>
        <td> 企业级多租户即时通讯解决方案，免费开源8件套：企业IM、在线客服、企业知识库、帮助文档、工单系统、AI对话、项目管理、工作流。.</td>
    </tr>
    <tr>
        <td><img src="https://raw.githubusercontent.com/rockbenben/subtitle-translator/main/public/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/rockbenben/subtitle-translator">Subtitle Translator</a></td>
        <td>支持 SRT/ASS/VTT/LRC 格式的批量字幕翻译工具，兼容 DeepSeek 等多种大模型接口和机器翻译接口。</td>
    </tr>
    <tr>
        <td width=80> <img src="docs/turtlenoir/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://haiguitang.net/"> 出前一汤 </a> </td>
        <td> <a href="https://haiguitang.net/"> 出前一汤 </a> 基于 DeepSeek 的 AI 主持人海龟汤 / 侧向思维解谜产品，可单人或者多人游玩。AI 进行控场与吐槽，围绕“是 / 否 / 无关”的问答推进推理；提供沉浸式玩法（更强剧情氛围与节奏引导）、引导提示与防卡关机制，同时结合向量检索 + DeepSeek 进行题目去重，并提供内容审核能力。适合轻量脑洞训练与在线陪玩。 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/songquanpeng/one-api/main/web/default/public/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/songquanpeng/one-api">One API</a> </td>
        <td> LLM API 管理 & 分发系统，支持 OpenAI、Azure、Anthropic Claude、Google Gemini、DeepSeek、字节豆包、ChatGLM、文心一言、讯飞星火、通义千问、360 智脑、腾讯混元等主流模型，统一 API 适配，可用于 key 管理与二次分发。单可执行文件，提供 Docker 镜像，一键部署，开箱即用。</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/guyoung/AIMatrices/raw/main/docs/assets/logo/ai-matrices1.png" alt="AIMatrices 图标" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/guyoung/AIMatrices/blob/main/README.md">AIMatrices</a> </td>
        <td>AIMatrices 是一款轻量级、高性能、可扩展、开源的AI应用快速构建平台，旨在为开发者提供高效、便捷的 AI 应用开发体验。它通过集成多种先进的技术和工具，帮助用户快速搭建、部署和维护 AI 应用，无需从零开始编写复杂的代码。</td>
    </tr>
    <tr>
        <td> <img src="docs/AIspire/assets/AIspire_logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.aispire.info">AIspire</a> </td>
        <td> AIspire是一个辅助AI学术写作的全能助手，从学术问题解答、学术灵感发现、文献管理、辅助阅读到全自动化AI辅助写作，让你的科研更精准、更高效。 </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="agent">AI Agent 框架</span>

<table>
        <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/182288589?s=200&v=4" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/DMontgomery40/deepseek-mcp-server/blob/main/README.md">DeepSeek MCP Server</a> </td>
        <td> 用于 DeepSeek 高级语言模型的 Model Context Protocol 服务器</td>
    </tr>
    <tr>
        <td> <img src="https://panda.fans/_assets/favicons/apple-touch-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/anda/README_cn.md">Anda</a> </td>
        <td> 一个专为 AI 智能体开发设计的 Rust 语言框架，致力于构建高度可组合、自主运行且具备永久记忆能力的 AI 智能体网络。 </td>
    </tr>
    <tr>
        <td> <img src="https://yomo.run/yomo-logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/yomo/README.md">YoMo</a> </td>
        <td> 一个有状态的无服务器大语言模型（LLM）函數调用框架，支持强类型语言。 </td>
    </tr>
    <tr>
        <td> <img src="https://alice.fun/alice-logo.png" alt="图标" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/bob-robert-ai/bob/blob/main/alice/readme.md">Alice</a> </td>
        <td> 一个基于 ICP 的自主 AI 代理，利用 DeepSeek 等大型语言模型进行链上决策。Alice 结合实时数据分析和独特的个性，管理代币、挖掘 BOB 并参与生态系统治理。 </td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/173022229" alt="图标" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/APRO-com">ATTPs</a> </td>
        <td> 一个用于Agent之间可信通信的基础协议框架，基于DeepSeek的Agent，可以接入<a href="https://docs.apro.com/attps">ATTPs</a>的SDK，获得注册Agent，发送可验证数据，获取可验证数据等功能，从而与其他平台的Agent进行可信通信。 </td>
    </tr>
    <tr>
        <td> <img src="docs/translate.js/assets/icon.png" alt="图标" width="64" height="auto" /> </td>
        <td> <a href="docs/translate.js/README_cn.md">translate.js</a> </td>
        <td> 面向前端开发者的 AI i18n, 两行js实现html全自动翻译，几十语种一键切换，无需改动页面、无语言配置文件、支持几十个微调扩展指令、对SEO友好。并且开放标准文本翻译API接口</td>
    </tr>
    <tr>
        <td width=80> <img src="docs/agentUniverse/assets/agentUniverse_logo_s.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/antgroup/agentUniverse"> agentUniverse </a> </td>
        <td> agentUniverse 是一个面向复杂业务场景设计的多智能体协作框架。其提供了快速易用的大模型智能体应用搭建能力，并着重于提供智能体协同调度、自主决策与动态反馈等机制，其源自蚂蚁集团在金融领域的真实业务实践沉淀。agentUniverse于2024年6月全面接入支持deepseek系列模型。  </td>
    </tr>
    <tr>
        <td width=80> <img src="docs/BotSharp/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/SciSharp/BotSharp"> BotSharp </a> </td>
        <td> BotSharp 是一个开源的多智能体应用开发框架，从简单的聊天机器人，再到多智能体协作，以及复杂的任务如【Text To Sql】框架都提供了开箱即用的使用方法，可以快速的将大模型的能力接入到现有的业务系统中，并且内置知识库和会话管理功能等，框架使用DeepSeek V3的模型进行了详细的测试，得益于DeepSeek V3的性能，框架的表现不输其他的闭源的模型。 </td>
    </tr>
    <tr>
        <td width=80> <img src="docs/eino/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/cloudwego/eino"> Eino </a> </td>
        <td> Eino（发音类似"I know"）旨在成为Go语言中最优秀的LLM应用开发框架。它借鉴了LangChain、LlamaIndex等开源社区优秀LLM框架的设计理念，同时吸收了前沿研究成果和实际应用经验，提供了一个更符合Go语言编程惯例的LLM应用开发框架，强调简洁性、可扩展性、可靠性和高效性。
        </td>
    </tr>
    <tr>
        <td width=80> <img src="https://raw.githubusercontent.com/Tencent/Youtu-agent/924aeeb6c49ee524b8bb4de2642a3dc84b7b86b9/docs/assets/mascot.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Tencent/Youtu-agent/"> Youtu-Agent </a> </td>
        <td> <a href="https://github.com/Tencent/Youtu-agent/"> Youtu-Agent </a> 是一个灵活、高性能的框架，用于构建、运行和评估自主智能体。除了在基准测试中名列前茅，该框架还提供了强大的智能体能力，采用开源模型即可实现例如数据分析、文件处理、深度研究等功能。 </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="data">AI数据应用框架</span>

<table>
    <tr>
        <td width="80"> <img src="https://github.com/user-attachments/assets/a327d72f-755f-4256-8a37-32a518a55df3" alt="Icon" width="96" height="auto" /> </td>
        <td width="120"> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/dbgpt/README_cn.md"> DB-GPT </a> </td>
        <td> DB-GPT是一个开源的AI原生数据应用开发框架(AI Native Data App Development framework with AWEL(Agentic Workflow Expression Language) and Agents)。
目的是构建大模型领域的基础设施，通过开发多模型管理(SMMF)、Text2SQL效果优化、RAG框架以及优化、Multi-Agents框架协作、AWEL(智能体工作流编排)等多种技术能力，让围绕数据库构建大模型应用更简单，更方便。
 </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="rag">RAG 框架</span>

<table>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/33142505/77093e84-9f7c-4716-9168-bac962fa1372" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/ragflow/README_cn.md"> RAGFlow </a> </td>
        <td> 一款基于深度文档理解构建的开源 RAG（Retrieval-Augmented Generation）引擎。RAGFlow 可以为各种规模的企业及个人提供一套精简的 RAG 工作流程，结合大语言模型（LLM）针对用户各类不同的复杂格式数据提供可靠的问答以及有理有据的引用。 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/pingcap/tidb.ai/main/frontend/app/public/nextra/icon-dark.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/autoflow/README_cn.md"> Autoflow </a> </td>
        <td> <a href="https://github.com/pingcap/autoflow">AutoFlow</a> 是一个开源的基于 GraphRAG 的知识库工具，构建于 <a href="https://www.pingcap.com/ai?utm_source=tidb.ai&utm_medium=community">TiDB</a> Vector、LlamaIndex 和 DSPy 之上。提供类 Perplexity 的搜索页面，并可以嵌入简单的 JavaScript 代码片段，轻松将 Autoflow 的对话式搜索窗口集成到您的网站。 </td>
    </tr>
    <tr>
        <td> <img src="https://assets.zilliz.com/Zilliz_Logo_Mark_White_20230223_041013_86057436cc.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/zilliztech/deep-searcher"> DeepSearcher </a> </td>
        <td> DeepSearcher 结合强大的 LLM（DeepSeek、OpenAI 等）和向量数据库（Milvus 等），根据私有数据进行搜索、评估和推理，提供高度准确的答案和全面的报告。 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/OpenSPG/openspg/089188f3e7b0392221f5a8e8f1a3629b6352a6f9/LOGO.png" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://github.com/OpenSPG/KAG/blob/master/README_cn.md"> KAG </a> </td>
        <td> KAG 是基于 <a href="https://github.com/OpenSPG/openspg">OpenSPG</a> 引擎和大型语言模型的逻辑推理问答框架，用于构建垂直领域知识库的逻辑推理问答解决方案。KAG 可以有效克服传统 RAG 向量相似度计算的歧义性和 OpenIE 引入的 GraphRAG 的噪声问题。KAG 支持逻辑推理、多跳事实问答等。 </td>
    </tr>
   <tr>
        <td width="80"> <img src="https://raw.githubusercontent.com/TencentCloudADP/youtu-graphrag/refs/heads/main/assets/logo.png" alt="Youtu-GraphRAG icon" width="64" height="auto"/> </td>
        <td> <a href="https://github.com/TencentCloudADP/Youtu-GraphRAG"> Youtu-GraphRAG </a> </td>
        <td>Youtu-GraphRAG是腾讯优图实验室开源的图检索增强生成新范式，通过Schema连接两个智能体，在图构建、索引和检索上实现垂直统一和认知闭环，以领先的落地级图构建与推理能力推动GraphRAG进入新的阶段。</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="fhe">FHE (全同态加密) frameworks</span>

<table>
    <tr>
        <td> <img src="./docs/fhe.mind-network/mind-network-log.png" alt="Icon" width="200" height="auto" /> </td>
        <td> <a href="https://github.com/mind-network/mind-sdk-deepseek-rust"> Mind FHE Rust SDK </a> </td>
        <td> <p>一个开源 SDK，可使用**全同态加密（FHE）**对 AI 进行加密，实现代理共识。FHE被誉为密码学的圣杯，能够在无需解密的情况下直接对加密数据进行计算。借助FHE，代理在使用Deepseek时可以保护隐私，同时确保模型的完整性和计算结果的一致性，无需暴露任何数据。该SDK的<a href="https://github.com/mind-network/mind-sdk-deepseek-rust">源代码</a>采用纯Rust实现，并可在<a href="https://crates.io/crates/mind_sdk_deepseek">crates.io</a>获取</p> </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="solana">Solana 框架</span>

<table>
    <tr>
        <td style="background-color: black"> <img src="docs/solana-agent-kit/assets/sendai-logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/sendaifun/solana-agent-kit"> Solana Agent Kit </a> </td>
        <td> 一个用于连接 AI 智能体到 Solana 协议的开源工具包。现在，任何使用 DeepSeek LLM 的智能体都可以自主执行 60+ 种 Solana 操作。 </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="sythetic">综合数据管理</span>

<table>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/192579850?s=200&v=4" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/DataEval/dingo"> Dingo </a> </td>
        <td> 一个综合性的数据质量评估工具。 </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="im">即时通讯插件</span>

<table>
    <tr>
        <td> <img src="https://github.com/InternLM/HuixiangDou/releases/download/v0.1.0rc1/huixiangdou.jpg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/huixiangdou/README_cn.md">茴香豆<br/>（个人微信/飞书）</a> </td>
        <td> 一个集成到个人微信群/飞书群的领域知识助手，专注解答问题不闲聊</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/RockChinQ/LangBot/blob/master/res/logo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/RockChinQ/LangBot">LangBot<br/>（QQ, 企微, 飞书）</a> </td>
        <td> 大模型原生即时通信机器人平台，适配 QQ / QQ频道 / 飞书 / OneBot / 企业微信（wecom） 等多种消息平台 </td>
    </tr>
    <tr>
        <td> <img src="https://nonebot.dev/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/KomoriDev/nonebot-plugin-deepseek">NoneBot<br/>（QQ, 飞书, Discord, TG, etc.）</a> </td>
        <td> 基于 NoneBot 框架，支持智能对话与深度思考功能。适配 QQ / 飞书 / Discord, TG 等多种消息平台 </td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/197911947?s=200&v=4" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/AstrBotDevs/AstrBot/">AstrBot<br/>（QQ, 微信, 企微, 飞书, TG, etc.）</a> </td>
        <td> 支持大模型的多平台聊天机器人及开发框架。支持 RAG、长期记忆以及网页搜索等各种 LLM Agent 功能, 支持插件开发。</td>
    </tr>
    <tr>
        <td> <img src="https://oss.nekro.ai/nekro_agent_logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/KroMiose/nekro-agent">NekroAgent<br/>（QQ, Discord, BiliBiliLive, Minecraft etc.）</a> </td>
        <td> Nekro Agent 是一个智能优雅的 AI 代理执行框架，其核心是通过强大灵活的提示词构建系统，引导 AI 生成代码并在安全的沙盒环境中执行。它通过原生的多平台适配器架构实现了强大的跨平台事件流处理能力，能够无缝支持 OneBot v11 (QQ)、Discord、Minecraft 和 B站直播(驱动VTB进行演出) 等多种主流平台。项目还拥有高度可扩展的插件系统、人设与插件共享生态，并支持在复杂的群聊多人交互场景中进行高效互动。目标是为用户和开发者提供极致高效、高自由度与易用性的开发友好型智能中枢。</td>
    </tr>
    <tr>
        <td> <img src="https://www.lanyingim.com/img/header/dock_lanying.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.lanyingim.com">蓝莺IM<br/></a> </td>
        <td> <b>AI Chatbot SDK 和云服务</b>，<br>包括一个跨平台（iOS、安卓、网页、PC、Linux等）的<a href="https://github.com/maxim-top/maxim-bistro">聊天SDK</a>和一个AI Agent平台。<br/> 可嵌入应用APP，支持对接微信、公众号。<br/> 原生支持DeepSeek，无需单独配置API-Key。</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="office">Office插件</span>

<table>
     <tr>
        <td> <img src="https://image.yoojober.com/users/2025-05/6836d9fdc8508.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.chatppt.cn/">ChatPPT</a> </td>
        <td>对话式AI创作PPT产品，国内最早（2023年3月4日上线）首款基于Chat对话式创作的AI PPT产品，目前支持web网页版、Office插件版（微软+WPS）、PC应用端（windows、mac、linux）、微信小程序等多版本，已经实现超过1800+指令服务，目前注册使用超过1500+万，且支持用户基于DeepSeek进行自由对话与文档对话两种模式，也满足用户配置自己的DeepSeek模型。</td>
    </tr> 
  <tr>
        <td> <img src="https://www.44886.com/view/img/bukeng.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.bukenghezi.com/">不坑盒子</a> </td>
        <td>一款支持Word、Excel、PPT三件套的Office插件（WPS三件套也支持），给Office增加300多功能</td>
    </tr>
    <tr>
        <td> <img src="https://www.aippt.cn/_nuxt/logo_cn.eYEokZzA.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.aippt.cn/">AiPPT</a> </td>
        <td>AiPPT.com 超2000万用户选择的正版AiPPT。一句话，一分钟，一键生成 PPT。</td>
    </tr>
    <tr>
        <td> <img src="https://www.office-ai.cn/static/images/officeai/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.office-ai.cn/">OfficeAI助手</a> </td>
        <td>OfficeAI助手是一款免费的办公插件，在Office中提供AI问答、AI校对、AI排版、AI创作、AI数据处理等功能，可提高办公效率。兼容Microsoft Office和WPS Office。</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="browser">浏览器插件</span>

<table>
    <tr>
        <td><img src="./docs/SelectTranslate/assets/icon.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://selecttranslate.com/">精挑翻译</a></td>
        <td>一款免费开放的 AI 翻译插件，拥有双语网页翻译、择优翻译（文案翻译）、输入翻译、PDF 翻译等创新实用的翻译功能。</td>
    </tr>
    <tr>
        <td><img src="./docs/deepshare/assets/logo_200.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="./docs/deepshare/README_cn.md">小智蜂</a></td>
        <td> 小智蜂是免费免登录一键分享AI聊天的油猴插件,专门解决数千字AI问答发给朋友,导致其手机被刷屏,或长截图被压缩,打开模糊不清,不方便阅读的问题,满足用户将自己与AI智慧的结晶分享给他人的需求
        </td>
    </tr>
    <tr>
        <td><img src="docs/OpenXLab/migo/logo.svg" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://chromewebstore.google.com/detail/cjapgnecnkblehipjghhegiccobeloka?utm_source=item-share-cb">觅果</a></td>
        <td> 提供全面的文本处理、信息检索与知识问答功能，灵活适配多种在线办公与科研场景（如飞书、arXiv、Overleaf 等），助力高效智能化工作流</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/9d3f42b8-fcd0-47ab-8b06-1dd0554dd80e" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/immersive_translate/README_cn.md"> 沉浸式翻译 </a> </td>
        <td> 一款双语对照网页翻译插件，简洁，高效 </td>
    </tr>
    <tr>
        <td> <img src="https://lh3.googleusercontent.com/K9i0qJb8phasC5wWf5tU68rhnfvX4swsE0hrhJP-WB3WV7MwE5KpMUIJvHKNHHRE6GKNIvIdTNSWoDMl_NggrmUsaw=s120" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/immersive_reading_guide/README_cn.md"> 沉浸式导读 </a> </td>
        <td> NO Sidebar!!! 沉浸式的 AI 网页摘要，提问... </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/8a301619-a3de-489b-81fd-69aaa7c1c561" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/chatgpt_box/README_cn.md"> ChatGPT Box </a> </td>
        <td> 将 LLM 作为私人助手，整合到你的浏览器中 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/c3d9d100-247a-41cc-97c1-10b01ed25e70" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/hcfy/README_cn.md"> 划词翻译 </a> </td>
        <td> 整合了多家翻译 API 以及 LLM API 的浏览器翻译插件 </td>
    </tr>
    <tr>
        <td> <img src="https://static.eudic.net/web/trans/en_trans.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/Lulu Translate/README_cn.md"> 欧路翻译 </a> </td>
        <td> 提供鼠标划词搜索、逐段对照翻译、PDF文献翻译功能。可以使用支持 DeepSeek AI、Bing、GPT、Google 等多种翻译引擎。 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/Bistutu/FluentRead/raw/refs/heads/main/public/icon/192.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://fluent.thinkstu.com/"> 流畅阅读 </a> </td>
        <td> 一款革新性的浏览器开源翻译插件，让所有人都能够拥有基于母语般的阅读体验 </td>
    </tr>
    <tr>
        <td> <img src="https://www.ncurator.com/_next/image?url=%2Ffavicon.ico&w=96&q=75" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.ncurator.com/"> 馆长 </a> </td>
        <td> 知识库AI问答助手 - 让AI帮助你整理与分析知识</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/oinzen/RSSFlow-doc/blob/main/docs/images/en/icon64.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://rssflow.oinchain.com"> RssFlow </a> </td>
        <td> 一款智能的RSS阅读器浏览器扩展，具有AI驱动的RSS摘要和多维度订阅视图功能。支持配置DeepSeek模型以增强内容理解能力。 </td>
    </tr>
    <tr>
        <td> <img src="https://www.typral.com/_next/image?url=%2Ffavicon.ico&w=96&q=75" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.typral.com/"> Typral </a> </td>
        <td> 超快的AI写作助手 - 让AI帮你快速优化日报，文章，文本等等... </td>
    </tr>
    <tr>
        <td> <img src="https://static.trancy.org/assets/trancy_logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.trancy.org/"> Trancy </a> </td>
        <td> 沉浸双语对照翻译、视频双语字幕、划句/划词翻译插件 </td>
    </tr>
    <tr>
        <td> <img src="https://ziziyi.com/svg/anything_copilot.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/baotlake/anything-copilot"> Anything Copilot </a> </td>
        <td> Anything Copilot 是一款可以让你在侧边栏无缝使用任意主流AI工具的浏览器插件 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/Hedwi/deepchat/refs/heads/main/images/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://chromewebstore.google.com/detail/deepchat-power-of-deepsee/femhcibnncinlabdboehojdhfcihpkpl?hl=en"> DeepChat </a> </td>
        <td>一款Chrome扩展程序，允许用户在任何网站上通过打开侧边栏与DeepSeek聊天。此外，它还在任何网站上选中的文本下方提供一个浮动菜单，使用户能够生成文本摘要、检查语法问题和翻译内容。</td>
    </tr>
    <tr>
        <td> <img src="http://cdn.docky.ai/assets/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/docky-ai/README_cn.md"> Docky AI </a> </td>
        <td>Docky AI 是一款功能强大的浏览器插件，允许您通过侧边栏与多个 AI 模型进行实时对话。它支持多模型同时交流，并能协助您阅读网页、写作、翻译和创作图片</td>
    </tr>
    <tr>
        <td> <img src="./docs/refinereader/assets/refinereader-128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://refinereader.cuihuaer.com"> Refine Reader </a> </td>
        <td> 一款基于 AI （DeepSeek、OpenAI等） 的智能阅读助手，致力于帮助用户快速理解和提炼文章精华，支持阅读互动。</td>
    </tr>
    <tr>
        <td><img src="https://readfrog.mengxi.work/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://readfrog.mengxi.work"> 🐸 陪读蛙 </a></td>
        <td>借助 AI 深度翻译并理解任何网页。</td>
    </tr>
    <tr>
        <td> <img src="./docs/Rearview/assets/favicon.webp" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="./docs/Rearview/README_cn.md"> RearView </a> </td>
        <td>Rearview 是一款浏览器历史管理扩展，支持对历史浏览内容的全文搜索，并将浏览历史转换为可对话的知识库。</td>
    </tr>
    <tr>
        <td> <img src="https://www.chatgot.io/chat/assets/imgs/logo@2x.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.chatgot.io/"> ChatGOT </a> </td>
        <td> 一个免费的AI聊天机器人助手，用于提高生产力 </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="vscode">VS Code 插件</span>

<table>
    <tr>
        <td> <img src="https://github.com/continuedev/continue/blob/main/docs/static/img/logo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/continue/README_cn.md"> Continue </a> </td>
        <td> 开源 IDE 插件，使用 LLM 做你的编程助手 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/cline/assets/favicon.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/cline/README.md"> Cline </a> </td>
        <td> Cline 是一款能够使用您的 CLI 和编辑器的 AI 助手 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/Sitoi/ai-commit/refs/heads/main/images/logo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Sitoi/ai-commit/blob/main/README.md"> AI Commit </a> </td>
        <td> 使用 AI 生成 git commit message 的 VS Code 插件 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/titusTong/seekCodeCopilot/blob/main/assets/SeekCodeCopilotLogo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/titusTong/seekCodeCopilot/blob/main/README.md"> SeekCode Copilot </a> </td>
        <td> vscode智能编码助手，支持配置本地部署的DeepSeek模型 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/intellism/vscode-comment-translate/blob/master/doc/image/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/intellism/vscode-comment-translate/blob/master/doc/README_ZH.md"> Comment Translation </a> </td>
        <td> 这款扩展程序能够帮助开发者翻译代码中的注释、字符串、代码提示、错误信息以及变量名。 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/AITK/assets/AIToolkit.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://code.visualstudio.com/docs/intelligentapps/overview"> AI Toolkit </a> </td>
        <td> Visual Studio Code 的 AI Toolkit 是一个综合性扩展，为开发人员和 AI 工程师提供使用生成式 AI 模型构建、测试和部署智能应用程序的能力。 </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/joygqz/commit-genie/refs/heads/main/images/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://marketplace.visualstudio.com/items?itemName=joygqz.commit-genie"> Commit Genie </a> </td>
        <td> 适用于 VS Code 的 AI 代码审查和提交消息生成器。自动审查您的代码更改并生成有意义的标准提交消息。 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/JohnnyZ93/oai-compatible-copilot/blob/main/assets/logo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/oai-compatible-copilot/README_cn.md"> OAI Compatible Provider for Copilot </a> </td>
        <td> 开源的 VS Code 扩展，可在 GitHub Copilot 中使用 OpenAI 兼容的推理提供商。 </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="neovim">neovim 插件</span>

<table>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/c316f70a-0a3c-4a32-b148-4df15e609acc" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/avante.nvim/README_cn.md"> avante.nvim </a> </td>
        <td> 开源 IDE 插件，使用 LLM 做你的编程助手 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/d66dfc62-8e69-4b00-8549-d0158e48e2e0" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/llm.nvim/README.md"> llm.nvim </a> </td>
        <td> 免费的大语言模型插件，让你在Neovim中与大模型交互，支持任意一款大模型，比如DeepSeek，GPT，GLM，kimi或者本地运行的大模型(比如ollama) </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/d66dfc62-8e69-4b00-8549-d0158e48e2e0" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/minuet-ai.nvim/README_cn.md"> minuet-ai.nvim </a> </td>
        <td> Minuet 提供实时代码补全功能，支持多个主流大语言模型，包括 DeepSeek、OpenAI、Gemini、Claude、Ollama、Codestral 等。 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/d66dfc62-8e69-4b00-8549-d0158e48e2e0" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/codecompanion.nvim/README.md"> codecompanion.nvim </a> </td>
        <td> AI 驱动的编码，在 Neovim 中无缝集成。 </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="jetbrains">JetBrains 插件</span>

<table>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/a18792721831/studyplugin/535b9cab69da0f97b42dcaebb00bb0d4ed15c8a6/translate/src/main/resources/META-INF/pluginIcon.svg" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://plugins.jetbrains.com/plugin/18336-chinese-english-translate">Chinese-English Translate</a> </td>
        <td> 集成了多家国内翻译和AI厂商，将中文翻译到英文的插件。 </td>
    </tr>
    <tr>
        <td> <img src="https://plugins.jetbrains.com/files/24851/659002/icon/pluginIcon.svg" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://plugins.jetbrains.com/plugin/24851-ai-git-commit">AI Git Commit</a> </td>
        <td> 使用AI生成git commit message的插件。 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/YiiGuxing/TranslationPlugin/blob/master/pluginIcon.svg?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://intellij-translation.yiiguxing.top">IntelliJ Translation Plugin</a> </td>
        <td> IntelliJ Translation Plugin 是一个适用于基于 IntelliJ 的 IDE 的翻译插件，它集成了包括 OpenAI 翻译（兼容 DeepSeek，Doubao，Ollama，……）在内的众多翻译服务，让您能够随时在 IDE 中直接翻译代码中的任何文本，如代码注释和代码文档等。</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="codeeditor">AI Code编辑器</span>

<table>
    <tr>
        <td> <img src="https://global.discourse-cdn.com/flex020/uploads/cursor1/original/2X/a/a4f78589d63edd61a2843306f8e11bad9590f0ca.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.cursor.com/"> Cursor </a> </td>
        <td> 基于VS Code进行扩展的AI Code编辑器 </td>
    </tr>
    <tr>
        <td> <img src="https://exafunction.github.io/public/images/windsurf/windsurf-app-icon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://codeium.com/windsurf"> WindSurf </a> </td>
        <td> 另一个基于VS Code的AI Code编辑器，由Codeium出品 </td>
    </tr>
    <tr>
        <td> <img src="docs/wusigram/assets/logo-512.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/wusigram/README_cn.md"> 无思微程序 </a> </td>
        <td> 移动端AI编程和运行工具，DeepSeek编程搭档 </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="security">安全</span>

<table>
    <tr>
        <td> <img src="./docs/tencent/hunyuan.png"  alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/tencent/AI-Infra-Guard"> AI-Infra-Guard </a> </td>
        <td> 腾讯混元安全-AI基础设施安全评估工具，发现和检测AI系统中的潜在安全风险。</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

###  <span id="others">其它</span>

<table>
    <tr>
        <td></td>
        <td> <a href="https://github.com/lunary-ai/abso/blob/main/README.md"> Abso </a></td>
        <td> TypeScript SDK 使用 OpenAI 格式与任何 LLM 提供商进行交互。 </td>
    </tr>
    <tr>
        <td> <img src="https://i.imgur.com/IsQYInJ.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/djcopley/ShellOracle/"> ShellOracle </a> </td>
        <td> 一种用于智能 shell 命令生成的终端工具。 </td>
    </tr>
    <tr>
        <td> <img src="https://pics.fatwang2.com/56912e614b35093426c515860f9f2234.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/fatwang2/siri-ultra"> Siri Ultra </a> </td>
        <td> GitHub 千星开源项目，支持联网、多轮对话，支持 DeepSeek 系列模型</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/c1e47b01-1766-4f7e-bfe6-ab3cb3991c30" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/tree/main/docs/siri_deepseek_shortcut"> 深度求索（快捷指令） </a> </td>
        <td> 使用 DeepSeek API 增强Siri能力的快捷指令 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/n8n-io/n8n/blob/master/assets/n8n-logo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/rubickecho/n8n-deepseek"> n8n-nodes-deepseek </a> </td>
        <td> 一个 N8N 的社区节点，支持直接使用 DeepSeek API 集成到工作流中 </td>
    </tr>
    <tr>
        <td> <img src="https://www.promptfoo.dev/img/logo-panda.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/promptfoo/README.md"> promptfoo </a> </td>
        <td> 测试和评估LLM提示，包括DeepSeek模型。比较不同的LLM提供商，捕获回归，并评估响应。 </td>
    </tr>
    <tr>
        <td></td>
        <td> <a href="https://github.com/AndersonBY/deepseek-tokenizer"> deepseek-tokenizer </a> </td>
        <td> 一个高效的轻量级tokenization库，仅依赖`tokenizers`库，不依赖`transformers`等重量级依赖。 </td>
    </tr>
    <tr>
        <td></td>
        <td> <a href="https://github.com/hustcer/deepseek-review"> deepseek-review </a> </td>
        <td> 🚀 使用 DeepSeek 进行代码审核，支持 GitHub Action 和本地 🚀 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/suqicloud/wp-ai-chat/raw/main/ic_logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/suqicloud/wp-ai-chat"> WordPress ai助手 </a> </td>
        <td> 对接DeepSeek API用于WordPress站点的AI对话助手、AI文章生成、AI文章总结插件。 </td>
    </tr>
    <tr>
        <td> <img src="docs/ComfyUI-Copilot/assets/logo 2.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/AIDC-AI/ComfyUI-Copilot"> ComfyUI-Copilot </a> </td>
        <td> 基于Comfy-UI框架构建的智能助手，通过自然语言交互简化和增强AI算法调试和部署过程。 </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/Optima-CityU/llm4ad/blob/main/assets/figs/logo_short.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Optima-CityU/llm4ad">LLM4AD</a> </td>
        <td> <a href="https://github.com/Optima-CityU/llm4ad">LLM4AD</a> 是一个开源、简洁、模块化的基于大模型的自动算法设计平台，使用DeepSeek API进行算法设计。</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/yincongcyincong/telegram-deepseek-bot/blob/main/static/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/yincongcyincong/telegram-deepseek-bot">telegram-deepseek-bot</a> </td>
        <td> <a href="https://github.com/yincongcyincong/telegram-deepseek-bot">telegram-deepseek-bot</a> 是一个集成deepseek-ai能力的telegram机器人。 </td>
    </tr>
    <tr>
        <td></td>
        <td> <a href="https://github.com/eqld/nlsh">nlsh</a> </td>
        <td> <a href="https://github.com/eqld/nlsh">nlsh</a> 是一个基于人工智能的命令行工具，支持多后端大语言模型，能够生成上下文感知的 Shell 命令。它兼容 Shell 专用语法、提供只读系统工具支持，并允许接入自定义推理端点。</td>
    </tr>
    <tr>
        <td> <img src="https://www.godtierprompts.com/logo.jpg" alt="Icon" width="64" height="auto" /></td>
        <td> <a href="https://www.godtierprompts.com">God Tier Prompts</a></td>
        <td> <a href="https://www.godtierprompts.com">God Tier Prompts</a> 是一个由社区驱动的排行榜，让最优秀的提示词脱颖而出。</td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/89342560?s=200&v=4" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Jeff2Ma/AlfredWorkflow-DeepSeek">DeepSeek Alfred WorkFlow</a> </td>
        <td> 在 Mac Alfred App 中快速调用 DeekSeek 的 workflow。 </td>
    </tr>
    <tr>
        <td> <img src="https://i.imgur.com/zDgW8wB.png" width="64" alt="Icon" height="auto" /> </td>
        <td> <a href="https://github.com/skypilot-org/skypilot">SkyPilot</a> </td>
        <td> <a href="https://github.com/skypilot-org/skypilot/tree/master/llm/deepseek-r1">在任何云基础设施上部署DeepSeek模型</a>（Kubernetes、AWS、Azure、GCP或GPU云）。支持多区域、多集群和多云的自动扩展。</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/cbf6193b-fd66-4b88-bcf7-98699becf046" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/sally-suite/open-office-copilot">Open Office Copilot</a> </td>
        <td> Open Office Copilot 是一个开源的 Office 助手，支持 Microsoft Office 和 Google Workspace，基于 AI-Agent。它可以帮助你在 Word 中写作、在 PowerPoint 中生成幻灯片、在 Excel 中分析数据、在 Outlook 里帮你生成邮件等，现在已经集成了 DeepSeek。</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#目录">^ 返回目录 ^</a></p>

### Star History

[![Star History Chart](https://api.star-history.com/svg?repos=deepseek-ai/awesome-deepseek-integration&type=Date)](https://star-history.com/#deepseek-ai/awesome-deepseek-integration&Date)
