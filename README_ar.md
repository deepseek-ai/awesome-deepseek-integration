<div align="center">

<p align="center">
<img width="1000px" alt="Awesome DeepSeek Integrations" src="docs/Awesome DeepSeek Integrations.png">
</p>

# تكاملات DeepSeek الرائعة ![Awesome](https://cdn.rawgit.com/sindresorhus/awesome/d7305f38d29fed78fa85652e3a63e154dd8e8829/media/badge.svg)

قم بدمج واجهة برمجة تطبيقات DeepSeek في البرمجيات الشائعة. قم بالوصول إلى [منصة DeepSeek المفتوحة](https://platform.deepseek.com/) للحصول على مفتاح API.

English/[简体中文](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/README_cn.md)/[繁體中文](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/README_zh_tw.md)/[日本語](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/README_ja.md)/[Español](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/README_es.md)/[العربية](https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/README_ar.md)

<a href="https://trendshift.io/repositories/12798" target="_blank"><img src="https://trendshift.io/api/badge/repositories/12798" alt="deepseek-ai%2Fawesome-deepseek-integration | Trendshift" style="width: 250px; height: 55px;" width="250" height="55"/></a>
</div>

## جدول المحتويات

- [Awesome DeepSeek Integrations ](#awesome-deepseek-integrations-)
  - [جدول المحتويات](#table-of-contents)
  - [قائمة المشاريع](#project-list)
    - [التطبيقات](#applications)
    - [أطر عمل وكلاء الذكاء الاصطناعي](#ai-agent-frameworks)
    - [أطر تطبيقات بيانات الذكاء الاصطناعي](#data-ai-applications-frameworks)
    - [أطر RAG](#rag-frameworks)
    - [أطر التشفير الكامل المتجانس (FHE)](#fhe-fully-homomorphic-encryption-frameworks)
    - [أطر Solana](#solana-frameworks)
    - [تنسيق البيانات الاصطناعية](#synthetic-data-curation)
    - [ملحقات تطبيقات المراسلة الفورية](#im-application-plugins)
    - [إضافات أوفيس](#office-addin)
    - [ملحقات المتصفح](#browser-extensions)
    - [امتدادات VS Code](#vs-code-extensions)
    - [امتدادات Visual Studio](#visual-studio-extensions)
    - [امتدادات neovim](#neovim-extensions)
    - [امتدادات JetBrains](#jetbrains-extensions)
    - [بوتات Discord](#discord-bots)
    - [محررات كود الذكاء الاصطناعي الأصلية](#native-ai-code-editor)
    - [Emacs](#emacs)
    - [الأمان](#security)
    - [المزودون](#providers)
    - [أخرى](#others)
    - [تاريخ النجوم](#star-history)

## قائمة المشاريع

###  <span id="applications">التطبيقات</span>

<table>
    <tr>
        <td><img src="docs/OpenXLab/migo/logo.svg" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://migo.intern-ai.org.cn/education">Migo</a></td>
        <td>مسرّع ابتكار ذكي مجاني يوفر أسئلة وأجوبة ذكية، فهم عميق للأوراق البحثية، أدوات ذكاء اصطناعي متطورة، وقاعدة معرفة أكاديمية شخصية. كشريك استكشاف، يساعدك Migo على اكتشاف وتحقيق الأفكار المتميزة!</td>
    </tr>
    <tr>
        <td><img src="docs/eechat/assets/logo.svg" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/Lucassssss/eechat">eechat</a></td>
        <td>أداة بسيطة وسهلة الاستخدام للنشر المحلي لنماذج اللغة الكبيرة، تدعم النشر الخاص المحلي لنماذج مفتوحة المصدر مثل DeepSeek-R1 وDLlama 3 وPhi-4 وMistral وGemma 3 وغيرها، مع دعم أيضاً لاستدعاءات واجهة LLM عن بُعد.</td>
    </tr>
    <tr>
        <td><img src="docs/aingdesk/assets/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/aingdesk/AingDesk">AingDesk</a></td>
        <td>نشر بنقرة واحدة لنماذج الذكاء الاصطناعي على جهاز الكمبيوتر مع واجهة مرئية، تتميز بواجهة دردشة أنيقة. تتيح المشاركة عبر الإنترنت للاستخدام التعاوني، وتدعم نماذج متنوعة مثل DeepSeek، وتمكن البحث على الويب وتكامل واجهات الطرف الثالث.</td>
    </tr>
    <tr>
        <td><img src="docs/dingtalk/assets/dingtalk_icon.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://www.dingtalk.com/">DingTalk</a></td>
        <td>مساعد DingTalk الذكي يدمج ميزات متعددة لمنتجات الذكاء الاصطناعي من منصة DingTalk لدعم المؤسسات بذكاء في سير عملها اليومي. يمتلك قدرات ذكية متنوعة، تشمل على سبيل المثال لا الحصر التواصل الذكي والتعاون الذكي والإدارة الذكية.

بهذه الوظائف، يمكن للمساعد الذكي تلخيص النقاط الرئيسية داخل المنظمة، وإنتاج محاضر الاجتماعات، وتوفير إشعارات المهام ذات الصلة وتذكيرات الجدولة للمستخدمين. بالإضافة لذلك، يستفيد مساعد DingTalk الذكي من قاعدة معرفته للإجابة بذكاء على استفسارات الموظفين الشائعة حول العمليات الإدارية للشركة وسياسات الموارد البشرية والموضوعات ذات الصلة الأخرى.</td>
    </tr>
    <tr>
        <td><img src="https://chatdoc.com/chatdoc/chatdoc.webp" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://chatdoc.com">ChatDOC</a></td>
        <td>ChatDOC أداة قراءة مستندات مدعومة بالذكاء الاصطناعي مجهزة بميزات تتبع قوية، تضمن أن مصدر كل معلومة واضح وقابل للتحقق، مما يساعدك على فهم جوهر مستنداتك بكفاءة ودقة.</td>
    </tr>
    <tr>
        <td> <img src="./docs/SwiftChat/assets/favicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/SwiftChat/README.md">SwiftChat</a></td>
        <td> <a href="https://github.com/aws-samples/swift-chat">SwiftChat</a> تطبيق دردشة ذكي عبر منصات متعددة بسرعة البرق مبني بـ React Native. يوفر أداءً أصلياً على Android وiOS وmacOS. الميزات تشمل دردشة بث فوري، دعم Markdown غني، إنتاج صور ذكي، رسائل نظام قابلة للتخصيص، اختيار سريع للنماذج وقدرات متعددة الوسائط. يدعم مزودي ذكاء اصطناعي متعددين بما في ذلك DeepSeek وAmazon Bedrock وOllama ونماذج متوافقة مع OpenAI بواجهة نظيفة وأداء عالي.</td>
    </tr>
    </tr>
        <td><img src="https://4everlogo.4everland.store/logo/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/4EVERChat/README.md">4EVERChat</a></td>
        <td><a href="https://chat.4everland.org/">4EVERChat</a> منصة اختيار نماذج ذكية تدمج مئات من LLMs، تمكن المقارنة الفورية لأداء النماذج. بالاستفادة من نقطة واجهة API موحدة لـ <a href="https://www.4everland.org/">4EVERLAND</a> AI RPC، تحقق تبديل نماذج بدون تكلفة وتختار تلقائياً التركيبات ذات الاستجابات السريعة والتكاليف المنخفضة.</td>
    </tr>
    <tr>
        <td><img src="./docs/xhai_browser/assets/logo_512.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="./docs/xhai_browser/README.md">xhai Browser</a></td>
        <td>xhai Browser متصفح إدارة سطح مكتب Android وذكاء اصطناعي، DeepSeek هو محرك الحوار الذكي الافتراضي. يتمتع بأداء فائق (0.2 ثانية للبدء)، حجم نحيف (apk 3M)، بدون إعلانات، حجب إعلانات فائق السرعة، تصنيف متعدد الشاشات، ملاحة الشاشة، مربع بحث متعدد، صندوق بحث متعدد!</td>
    </tr>
    <tr>
        <td><img src="https://i.imgur.com/FkbmMVG.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://intellibar.app/">IntelliBar</a></td>
        <td>IntelliBar مساعد جميل لـ Mac يتيح لك استخدام نماذج متقدمة مثل DeepSeek R1 مع أي تطبيق على Mac — مثل: تحرير الإيميلات في تطبيق البريد أو تلخيص المقالات في متصفحك.</td>
    </tr>
    <tr>
        <td><img src="./docs/gptbots/gptbots.png" alt="Icon" width="64" height="auto" /> </td>
        <td><a href="https://www.gptbots.ai/docs">GPTBots</a></td>
        <td><a href="https://www.gptbots.ai/">GPTBots</a> منصة بناء وكلاء ذكاء اصطناعي بدون كود تدمج LLMs دولية رئيسية، بما في ذلك Deepseek. توفر وحدات لتخزين/استرجاع المعرفة المعتمد على RAG، تخصيص/استدعاء الأدوات، وتنسيق سير العمل. بالإضافة لذلك، تتيح دمج الوكلاء في منصات رئيسية متعددة (مثل WhatsApp وTelegram وغيرها)، موفرة حلول ذكاء اصطناعي شاملة للشركات ومساعدتها على التميز في عصر الذكاء الاصطناعي.</td>
    </tr>
    <tr>
        <td><img src="https://github.com/ThinkInAIXYZ/deepchat/blob/main/build/icon.png?raw=true" alt="Icon" width="64" height="auto" style="border-radius: 10px" /></td>
        <td><a href="https://github.com/ThinkInAIXYZ/deepchat/blob/main/README.md">DeepChat</a></td>
        <td>DeepChat مساعد سطح مكتب ذكي مجاني بالكامل، مع نموذج DeepSeek الكبير القوي، يدعم المحادثات متعددة الجولات، البحث على الإنترنت، رفع الملفات، قواعد المعرفة، وأكثر.</td>
    </tr>
    <tr>
        <td width=80> <img src="https://avatars.githubusercontent.com/u/171659527?s=400&u=39906ab3b6e2066f83046096a66a77fb3f8bb836&v=4" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/quantalogic/quantalogic">Quantalogic</a> </td>
        <td> QuantaLogic إطار عمل ReAct (الاستدلال والعمل) لبناء وكلاء ذكاء اصطناعي متقدمين. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/13600976/224d547a-6fbc-47c8-859f-aa14813e2b0f" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/chatbox/README.md">Chatbox</a> </td>
        <td> Chatbox عميل سطح مكتب لنماذج LLM متطورة متعددة، متوفر على Windows وMac وLinux. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/bb65404c-f867-42d8-ae2b-281fe953ab54" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/chatgpt_next_web/README.md"> ChatGPT-Next-Web </a> </td>
        <td> ChatGPT Next Web واجهة ويب ChatGPT عبر منصات متعددة، مع دعم GPT3 وGPT4 وGemini Pro. </td>
    </tr>
    <tr>
        <td> <img src="docs/Casibase/assets/casibase.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://casibase.org/docs/category/beginner-guide/">Casibase</a></td>
        <td> <a href="https://casibase.org">Casibase</a> نظام قاعدة معرفة وحوار ذكي مفتوح المصدر يجمع بين أحدث تقنيات RAG ووظائف SSO ودعم مجموعة واسعة من نماذج الذكاء الاصطناعي الرئيسية. Casibase مصمم لتوفير منصة إدارة معرفة وحوار ذكي قوية ومرنة وسهلة الاستخدام للمؤسسات والمطورين. </td>
    </tr>
    <tr>
        <td> <img src="./docs/Coco AI/assets/favicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/Coco AI/README.md">Coco AI</a></td>
        <td> <a href="https://coco.rs">Coco AI</a> هي أداة مفتوحة المصدر، تتكامل مع مصادر بيانات متعددة، بما في ذلك تطبيقات التطوير وGoogle Drive وNotion وYuque وHugo وغيرها، ذات أساس محلي ومشترك. بالتكامل مع نماذج كبيرة، تمكن Coco AI من إدارة المعرفة الشخصية بشكل ذكي، مع تركيز على الخصوصية ودعم النشر المحلي، مساعدة المستخدمين على الوصول بكفاءة ودقة إلى المعلومات.</td>
    </tr>
    <tr>
        <td> <img src="./docs/liubai/assets/liubai-logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/liubai/README.md">Liubai</a> </td>
        <td> Liubai يسمح لـ DeepSeek بالحصول على ذراعين وذيول للتداول على WeChat!</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/1ac9791b-87f7-41d9-9282-a70698344e1d" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/pal/README.md"> Pal - AI Chat Client<br/>(iOS, ipadOS) </a> </td>
        <td> Pal هي ملعب دردشة ذكي مخصص على iOS. </td>
    </tr>
    <tr>
        <td> <img src="https://www.librechat.ai/librechat.svg" alt="LibreChat" width="64" height="auto" /> </td>
        <td> <a href="https://www.librechat.ai/docs/configuration/librechat_yaml/ai_endpoints/deepseek">LibreChat</a> </td>
        <td> LibreChat هي تطبيق مفتوح المصدر يدمج تكاملاً ممتازاً مع DeepSeek لتحسين تجربة التفاعل الذكي. </td>
    </tr>
     <tr>
        <td> <img src="https://raw.githubusercontent.com/longevity-genie/chat-ui/11c6647c83f9d2de21180b552474ac5ffcf53980/static/geneticsgenie/icon-128x128.png" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://github.com/longevity-genie/just-chat">Just-Chat</a> </td>
        <td> اجعل وكيل LLM الخاص بك والدردشة معه بسيطاً وسريعاً!</td>
     </tr>
    <tr>
        <td> <img src="https://www.papersgpt.com/images/logo/favicon.ico" alt="PapersGPT" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/papersgpt/papersgpt-for-zotero">PapersGPT</a> </td>
        <td> PapersGPT هي مكونة على منصة Zotero تدمج مع DeepSeek ونماذج ذكاء اصطناعي أخرى لقراءة المقالات في Zotero بسرعة.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/rss-translator/RSS-Translator/main/core/static/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/rss_translator/README.md"> RSS Translator </a> </td>
        <td> ترجم تغذيات RSS إلى لغتك! </td>
    </tr>
    <tr>
        <td> <img src="https://relingo.net/assets/images/relingo-logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://relingo.net"> Relingo </a> </td>
        <td> ابنِ وأتقن مفرداتك أثناء تصفح المواقع ومشاهدة يوتيوب! </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/ysnows/enconvo_media/main/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/enconvo/README.md"> Enconvo </a> </td>
        <td> Enconvo هو محرر الذكاء الاصطناعي لعصر الذكاء الاصطناعي، نقطة الدخول لجميع وظائف الذكاء الاصطناعي، ومساعد ذكي مفيد.</td>
    </tr>
    <tr>
        <td><img src="https://github.com/kangfenmao/cherry-studio/blob/main/src/renderer/src/assets/images/logo.png?raw=true" alt="Icon" width="64" height="auto" style="border-radius: 10px" /></td>
        <td><a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/cherrystudio/README.md">Cherry Studio</a></td>
        <td>مساعد سطح مكتب ذكي قوي للمنتجين</td>
    </tr>
    <tr>
        <td> <img src="https://tomemo.top/images/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/tomemo/README.md"> ToMemo (iOS, ipadOS) </a> </td>
        <td> تطبيق iOS يجمع بين دفتر العبارات وتاريخ الحافظة ولوحة المفاتيح مع نمذجة ذكاء اصطناعي متكاملة للاستخدام السريع في لوحة المفاتيح.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/buxuku/video-subtitle-master/refs/heads/main/resources/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/buxuku/video-subtitle-master">Video Subtitle Master</a></td>
        <td> إنتاج جماعي لترجمات الفيديو، مع القدرة على ترجمة الترجمات إلى لغات أخرى. هذه أداة من جانب العميل تدعم منصتي Mac وWindows وتتكامل مع خدمات ترجمة متعددة مثل Baidu وVolcengine وDeepLx وOpenAI وDeepSeek وOllama.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/UnknownEnergy/chatgpt-api/blob/master/dist/assets/chatworm-72x72.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/UnknownEnergy/chatgpt-api/blob/master/README.md">Chatworm</a> </td>
        <td> Chatworm تطبيق ويب لنماذج LLM متطورة متعددة، مفتوح المصدر ومتوفر أيضاً على Android. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/icon_512x512@2x.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/tisfeng/Easydict">Easydict</a></td>
        <td> Easydict قاموس ترجمة موجز وسهل الاستخدام لتطبيق macOS يتيح لك البحث عن الكلمات أو ترجمة النص بسهولة وأناقة. يدعم استدعاء واجهات نماذج اللغة الكبيرة للترجمة.</td>
    </tr>
    <tr>
        <td> <img src="https://www.raycast.com/favicon-production.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/raycast/README.md">Raycast</a></td>
        <td> <a href="https://raycast.com/?via=ViGeng">Raycast</a> أداة إنتاجية لـ macOS تتيح لك التحكم في أدواتك بضغطات مفاتيح قليلة. تدعم امتدادات متنوعة بما في ذلك DeepSeek AI.</td>
    </tr>
    <tr>
        <td> <img src="./docs/chatpdflocal/assets/chatpdflocal-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.chatpdflocal.com">ChatPDFLocal</a> </td>
        <td> ChatPDFLocal تطبيق Mac OS مدعوم بالذكاء الاصطناعي لمساعدة الدردشة مع PDF، يعمل بسلاسة مع DeepSeek ونماذج ذكاء اصطناعي متعددة أخرى لتحسين كفاءة قراءتك. </td>
    </tr>
    <tr>
        <td> <img src="https://niceprompt.app/favicon.ico" alt="Icon" width="64" height="auto" /> </td> <td> <a href="https://niceprompt.app">Nice Prompt</a></td> <td> <a href="https://niceprompt.app">Nice Prompt</a> نظم وشارك واستخدم رسائلك في محرر الكود، مع Cursor وVSCode.</td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/193405629?s=200&v=4" alt="PHP Client" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-php/deepseek-php-client/blob/master/README.md">PHP Client</a> </td>
        <td> Deepseek PHP Client مكتبة عميل PHP قوية ومدفوعة من المجتمع للتكامل السلس مع واجهة Deepseek. </td>
    </tr>
        <tr>
  <td>
    <img
      src="https://github.com/tornikegomareli/DeepSwiftSeek/blob/main/logo.webp"
      alt="DeepSwiftSeek Logo"
      width="64"
      height="auto"
    />
  </td>
  <td>
    <a href="https://github.com/tornikegomareli/DeepSwiftSeek/blob/main/README.md">DeepSwiftSeek</a>
  </td>
  <td>
    DeepSwiftSeek عبارة عن مكتبة عميل Swift خفيفة وقوية في الوقت نفسه، وتوفر تكاملاً ممتازاً مع واجهة DeepSeek.
    توفر تزامناً سهلاً في Swift من أجل الدردشة، البث المتدفق، إكمال FIM (الملء في المنتصف) وغيرها.
  </td>
</tr>
        <td> <img src="https://avatars.githubusercontent.com/u/958072?s=200&v=4" alt="Laravel Integration" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-php/deepseek-laravel/blob/master/README.md">Laravel Integration</a> </td>
        <td> غلاف Laravel لعميل DeepSeek PHP لتكامل واجهة DeepSeek بسلاسة مع تطبيقات Laravel.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/cohesion-org/deepseek-go/refs/heads/main/internal/images/deepseek-go.png" alt="Go Client" width="64" height="auto"> </td>
        <td> <a href="https://github.com/cohesion-org/deepseek-go/blob/main/README.md">Deepseek Go</a> </td>
        <td>  عميل DeepSeek مكتوب بلغة Go يدعم نماذج الدردشة والاستدلال، ويدعم أيضاً مزودين خارجيين مثل Azure وOpenRouter وغيرهما. </td>
    </tr>
    <tr>
        <td> <img src="./docs/zotero/assets/zotero-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/zotero/README_cn.md">Zotero</a></td>
        <td> <a href="https://www.zotero.org">Zotero</a> أداة مجانية وسهلة الاستخدام تساعدك على جمع الأبحاث وتنظيمها وتعليقها والاستشهاد بها ومشاركتها. ويمكنها استخدام DeepSeek كخدمة ترجمة.</td>
    </tr>
    <tr>
        <td> <img src="https://b3log.org/images/brand/siyuan-128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/SiYuan/README.md">SiYuan</a> </td>
        <td> SiYuan نظام إدارة معرفة شخصي يركز على الخصوصية ويدعم الاستخدام دون اتصال بالكامل بالإضافة إلى مزامنة بيانات مشفّرة من طرف إلى طرف.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/ArvinLovegood/go-stock/raw/master/build/appicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/ArvinLovegood/go-stock/blob/master/README.md">go-stock</a> </td>
        <td>go-stock عارض بيانات الأسهم الصينية مبني بـ Wails مع NativeUI ومدعوم بنماذج اللغة الكبيرة.</td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/102771702?s=200&v=4" alt="Wordware" width="64" height="auto" /> </td>
        <td> <a href="docs/wordware/README.md">Wordware</a> </td>
        <td><a href="https://www.wordware.ai/">Wordware</a> مجموعة أدوات تمكن أي شخص من بناء وتكرار ونشر مجموعة أدوات الذكاء الاصطناعي باستخدام اللغة الطبيعية فقط.</td>
    </tr>
    <tr>
        <td> <img src="https://framerusercontent.com/images/xRJ6vNo9mUYeVNxt0KITXCXEuSk.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/langgenius/dify/">Dify</a> </td>
        <td> <a href="https://dify.ai/">Dify</a> منصة تطوير تطبيقات LLM تدعم نماذج DeepSeek لإنشاء المساعدين وسير العمل ومولدات النصوص والمزيد. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/enricoros/big-AGI/refs/heads/v2-dev/public/favicon.ico" alt="Big-AGI" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/enricoros/big-AGI/blob/v2-dev/README.md">Big-AGI</a> </td>
        <td><a href="https://big-agi.com/">Big-AGI</a> هي مجموعة ذكاء اصطناعي رائدة مصممة لتسهيل الوصول إلى الذكاء الاصطناعي المتقدم للجميع.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/LiberSonora/LiberSonora/blob/main/assets/avatar.jpeg?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/LiberSonora/LiberSonora/blob/main/README_en.md">LiberSonora</a> </td>
        <td> LiberSonora، التي تعني "صوت الحرية"، هي مجموعة أدوات كتب صوتية قوية مفتوحة المصدر مدعومة بالذكاء الاصطناعي تتضمن ميزات مثل استخراج الترجمات الذكي، توليد عناوين بالذكاء الاصطناعي، الترجمة متعددة اللغات، مع دعم تسريع GPU ومعالجة دفعية دون اتصال.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/ripperhe/Bob/master/docs/_media/icon_128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://bobtranslate.com/">Bob</a></td>
        <td> <a href="https://bobtranslate.com/">Bob</a> أداة ترجمة وOCR لنظام macOS جاهزة للاستخدام في أي تطبيق — مباشرة!</td>
    </tr>
    <tr>
        <td> <img src="https://agenticflow.ai/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://agenticflow.ai/">AgenticFlow</a> </td>
        <td> <a href="https://agenticflow.ai/">AgenticFlow</a> منصة بدون كود حيث يبني المسوقون سير عمل ذكاء اصطناعي وكيل لأتمتة الانطلاق للسوق، مدعومة بمئات التطبيقات اليومية كأدوات لوكلاء الذكاء الاصطناعي.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/ZGGSONG/STranslate/raw/main/img/favicon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://stranslate.zggsong.com/en/">STranslate</a></td>
        <td> <a href="https://stranslate.zggsong.com/en/">STranslate</a>（Windows） أداة ترجمة OCR جاهزة مطورة بـ WPF </td>
    </tr>
    <tr>
        <td> <img src="https://devinci.onicai.com/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://devinci.onicai.com/">DeVinci</a></td>
        <td> <a href="https://devinci.onicai.com/">DeVinci</a> تطبيق دردشة ذكاء اصطناعي لامركزي شامل للدردشة الخاصة مع نماذج LLM مفتوحة المصدر.</td>
    </tr>
     <tr>
        <td> <img src="https://github.com/user-attachments/assets/5e16beb0-993e-47bf-807e-7c8804b313a2" alt="Asp Client" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Anwar-alhitar/Deepseek.Asp.Client/blob/master/README.md">ASP Client</a> </td>
        <td><a href="https://github.com/Anwar-alhitar/Deepseek.Asp.Client/blob/master/README.md">Deepseek.ASPClient</a> غلاف ASP.NET خفيف لواجهة Deepseek AI، مصمم لتبسيط معالجة النصوص المدفوعة بالذكاء الاصطناعي في تطبيقات .NET.. </td>
    </tr>
    <tr>
        <td> <img src="https://www.gptaiflow.tech/logo.png" alt="gpt-ai-flow-logo" width="64" height="auto" /> </td>
        <td> <a href="https://www.gptaiflow.tech/docs/product/api-keys-setup#setup-deepseek-api-keys">GPT AI Flow</a></td>
        <td>
            السلاح الإنتاجي النهائي المبني من المهندسين لعشاق الكفاءة (أنفسهم): <a href="https://www.gptaiflow.tech/">GPT AI Flow</a>
            <ul>
                <li>`Shift+Alt+Space` تنشيط مركز الذكاء المكتبي</li>
                <li>تخزين محلي مشفر</li>
                <li>محرك تعليمات مخصص</li>
                <li>استدعاء عند الطلب بدون ربط اشتراك</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/b09f17a8-936d-4dac-8b24-1682d52c9a3c" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/alecm20/story-flicks">Story-Flicks</a></td>
        <td>بجملة واحدة فقط، يمكنك بسرعة إنشاء مقاطع فيديو قصيرة عالية الدقة للقصص، مع دعم نماذج مثل DeepSeek.</td>
    </tr>
    <tr>
        <td> <img src="https://prompt.16x.engineer/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/16x_prompt/README.md">16x Prompt</a> </td>
        <td> <a href="https://prompt.16x.engineer/">16x Prompt</a> أداة برمجة ذكاء اصطناعي مع إدارة السياق. تساعد المطورين على إدارة سياق الكود المصدري وصياغة التعليمات للمهام البرمجية المعقدة على قواعد الكود الحالية.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/Alpha派/assets/favicon1.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/Alpha派/README.md"> Alpha Pai </a> </td>
        <td> مساعد بحث ذكاء اصطناعي / بوابة المعلومات المالية من الجيل القادم مدفوعة بالذكاء الاصطناعي.<br>وكيل للمستثمرين لحضور الاجتماعات وتدوين الملاحظات، بالإضافة إلى توفير خدمات البحث والأسئلة والأجوبة للمعلومات المالية والتحليل الكمي لأبحاث الاستثمار.</td>
    </tr>
        <td> <img src="https://docs.xark-argo.com/img/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.xark-argo.com">argo</a> </td>
        <td>قم بتنزيل وتشغيل نماذج Ollama وHuggingface محلياً مع RAG على Mac/Windows/Linux. يدعم أيضاً واجهة برمجة تطبيقات LLM.</td>
    </tr>
    <tr>
        <td> <img src="https://www.petercat.ai/images/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.petercat.ai">PeterCat</a> </td>
        <td> نظام تكوين وكيل أسئلة وأجوبة تفاعلي، حلول نشر ذاتية الاستضافة، ومجموعة تطوير تطبيقات شاملة وسهلة الاستخدام، تتيح لك إنشاء روبوتات أسئلة وأجوبة ذكية لمستودعات GitHub الخاصة بك.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/labring/FastGPT/refs/heads/main/.github/imgs/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://fastgpt.cn/en">FastGPT</a> </td>
        <td>
            FastGPT منصة قاعدة معرفة ذكاء اصطناعي مفتوحة المصدر مبنية على نماذج اللغة الكبيرة (LLMs)، تدعم نماذج متنوعة بما في ذلك DeepSeek وOpenAI. نوفر قدرات جاهزة للاستخدام لمعالجة البيانات، استدعاء النماذج، استرجاع RAG، وتنسيق سير عمل الذكاء الاصطناعي المرئي، مما يمكنك من بناء تطبيقات ذكاء اصطناعي متطورة بسهولة.
        </td>
   </tr>
   <tr>
        <td> <img src="./docs/ruzhiai_note/assets/play_store_512.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/ruzhiai_note/README.md">RuZhi AI Notes</a> </td>
        <td>RuZhi AI Notes أداة إدارة معرفة ذكية مدعومة بالذكاء الاصطناعي، توفر خدمات إدارة وتطبيق معرفة شاملة تشمل البحث والاستكشاف بالذكاء الاصطناعي، تحويل نتائج الذكاء الاصطناعي إلى ملاحظات، إدارة وتنظيم الملاحظات، عرض ومشاركة المعرفة. متكاملة مع نموذج DeepSeek لتوفير مخرجات أكثر استقراراً وجودة أعلى.</td>
    </tr>
    <tr>
        <td> <img src="https://cdn.link-ai.tech/doc/CoW%20logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/zhayujie/chatgpt-on-wechat">Chatgpt-on-Wechat</a> </td>
        <td> Chatgpt-on-Wechat(CoW) إطار عمل روبوت دردشة مرن يدعم التكامل السلس لنماذج LLM متعددة، بما في ذلك DeepSeek وOpenAI وClaude وQwen وغيرها، في منصات أو برمجيات مكتبية شائعة الاستخدام مثل حسابات WeChat الرسمية وWeCom وFeishu وDingTalk والمواقع. كما يدعم مجموعة واسعة من الإضافات المخصصة. </td>
    </tr>
    <tr>
        <td> <img src="https://athenalab.ai/assets/favicon/favicon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://athenalab.ai/">Athena</a> </td>
        <td>أول ذكاء اصطناعي عام مستقل في العالم مع هندسة معرفية متقدمة وقدرات استدلال شبيهة بالبشر، مصمم لمواجهة التحديات الحقيقية المعقدة.</td>
    </tr>
    <tr>
        <td> <img src="https://maxkb.cn/images/favicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/1Panel-dev/MaxKB">MaxKB</a> </td>
        <td> <a href="https://maxkb.cn/">MaxKB</a> روبوت دردشة RAG مرن وجاهز للاستخدام. </td>
    </tr>
    <tr>
        <td> <img src="./docs/TigerGPT/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://ttm.financial/gpt">TigerGPT</a> </td>
        <td>TigerGPT هو أول مساعد استثماري ذكاء اصطناعي مالي من نوعه مبني على OpenAI، طوره مجموعة Tiger. يهدف TigerGPT إلى توفير دعم اتخاذ قرارات استثمارية ذكي للمستثمرين. في 18 فبراير 2025، دمج TigerGPT رسمياً نموذج DeepSeek-R1 لتوفير خدمات أسئلة وأجوبة عبر الإنترنت تدعم الاستدلال العميق للمستخدمين. </td>
    </tr>
    <tr>
        <td> <img src="./docs/HIX.AI/assets/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://hix.ai">HIX.AI</a> </td>
        <td>جرب DeepSeek مجاناً واستمتع بدردشة ذكاء اصطناعي غير محدودة على HIX.AI. استخدم DeepSeek R1 للدردشة بالذكاء الاصطناعي، الكتابة، البرمجة والمزيد. اختبر دردشة الذكاء الاصطناعي من الجيل القادم الآن!</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/sharmt1411/askanywhere/blob/main/icon/Depth_8,_Frame_0explore-%E8%A7%92%E6%A0%87.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/sharmt1411/askanywhere">Askanywhere</a> </td>
        <td>حدد النص في أي مكان وابدأ محادثة مع Deepseek</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/OJZen/1chat/raw/refs/heads/main/doc/assets/icon.ico?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/OJZen/1chat">1chat</a> </td>
        <td>تطبيق iOS يتيح لك الدردشة مع نموذج DeepSeek-R1 محلياً.</td>
    </tr>
    <tr>
        <td> <img src="https://chatlabsai.com/assets/logo/logo.png" alt="iOS AI Chatbot" width="64" height="auto" /> </td>
        <td> <a href="https://chatlabsai.com">Access 250+ text, image LLMs in one app</a> </td>
        <td> 1AI iOS Chatbot يتكامل مع أكثر من 250 نموذج نص وصورة وصوت يتيح للمستخدمين الدردشة مع أي نموذج في العالم بما في ذلك نماذج Deepseek R1 وDeepseek V3.</td>
    </tr>
    <tr>
        <td> <img src="./docs/PopAi/assets/logo.svg" alt="PopAi" width="64" height="auto" /> </td>
        <td> <a href="https://popai.pro">PopAi</a> </td>
        <td>PopAi تطلق DeepSeek R1! استمتع بأداء سريع البرق وبدون تأخير مع PopAi. قم بالتبديل بسلاسة بين البحث عبر الإنترنت تشغيل/إيقاف.</td>
    </tr>
    <tr>
        <td> <img src="https://pot-app.com/logo/icon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://pot-app.com/">Pot</a></td>
        <td> <a href="https://pot-app.com/">Pot</a> 🌈 برنامج متعدد المنصات لترجمة النصوص والتعرف عليها. </td>
    </tr>
    <tr>
        <td><img src="https://github.com/Byaidu/PDFMathTranslate/raw/main/docs/images/banner.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/Byaidu/PDFMathTranslate">PDFMathTranslate</a></td>
        <td>PDF Math Translate أداة ترجمة ثنائية اللغة شاملة مبنية على الذكاء الاصطناعي تحافظ على تخطيط مستندات PDF بالكامل.</td>
    </tr>
    <tr>
        <td><img src="https://github.com/Richasy/Bili.Copilot/raw/master/assets/StoreLogo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/Richasy/Bili.Copilot">Bili.Copilot</a></td>
        <td>Bilibili عميل سطح مكتب Windows من طرف ثالث، تطبيق أصلي مبني بـ Windows App SDK.</td>
    </tr>
    <tr>
        <td><img src="https://www.tensorbounce.com/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://www.tensorbounce.com/">LawAgent</a></td>
        <td>LawAgent منتج ذكاء اصطناعي قانوني طوره فريق Tensorbounce، يدمج قاعدة معرفة مع قدرات AI Agent. يتميز بمستودع ضخم من عشرات الملايين من نقاط البيانات الرسمية المتعلقة بالقانون كما يتيح تكوينات قاعدة معرفة مخصصة. الوضع المهني يستفيد من قدرات الاستدلال لـ DeepSeek-R1 لمساعدة المستخدمين في التحليل القانوني، مراجعة العقود، توليد المستندات، ترجمة الملفات، وسيناريوهات قانونية أخرى.</td>
    </tr>
    <tr>
        <td width=80> <img src="docs/AlphaBot/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://alphabot.x-pai.com/">AlphaBot</a> </td>
        <td> AlphaBot مساعد تحليل أسهم ذكي يدمج بيانات متعددة المصادر مع تقنية تحليل الذكاء الاصطناعي لتوفير التحليل الفني والتنبؤات وتقييم المخاطر، مساعداً المستثمرين على اتخاذ قرارات تداول مبنية على البيانات. يدعم نشر بنقرة واحدة، عمليات سهلة، يدعم منصات Windows/Linux/MacOS وغيرها</td>
     <tr>
        <td><img src="https://h1.appinn.me/file/1741929316827_21.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/jiqi136/DS-AI">Multi-platform connected DeepSeek</a></td>
        <td>يستفيد من محرك الذكاء الاصطناعي ثلاثي القنوات المدعوم من DeepSeek الرسمي وسحابة علي بابا وبركان دويين، حيث يتطور ذكاؤه باستمرار. بالإضافة إلى ذلك، يستخدم وضعاً هجيناً يجمع بين "البحث عبر الإنترنت + التفكير العميق".</td>
    </tr>
    <tr>
    <td><img src="docs/remio/assets/remio_icon.png" alt="Icon" width="64" height="auto" /></td>
    <td><a href="https://www.remio.ai/">remio</a></td>
    <td>remio مركز معرفة شخصي مدعوم بالذكاء الاصطناعي يبني قواعد معرفة شخصية من خلال التقاط تلقائي لمحتوى الويب المتصفح، تحليل الملفات المحلية، ودمج الملاحظات الشخصية. يمكن البحث والأسئلة والأجوبة بالللغة الطبيعية داخل قاعدة معرفتك الشخصية للحصول على رؤى فورية مع توفير مساعدة كتابة ذكية—تتكيف مع أسلوبك لتبسيط الصياغة والتحسين وإكمال المحتوى بسهولة. مصمم مع تخزين محلي أولاً، remio يعطي الأولوية لخصوصية البيانات مع تمركز المعلومات المجزأة لتحقيق أقصى إنتاجية.</td>
    </tr> 
    <tr>
    <td><img src="docs/DocKit/assets/dockit.png" alt="Icon" width="64" height="auto" /></td>
    <td><a href="https://dockit.geekfun.club/">DocKit</a></td>
    <td>DocKit عميل GUI سطح مكتب مدعوم بالذكاء الاصطناعي مصمم لقاعدة بيانات NoSQL، يدعم Elasticsearch وOpenSearch عبر Mac وWindows وLinux. من خلال التكامل مع نماذج كبيرة مثل DeepSeek، يمكن لـ DocKit مساعدة المطورين على كتابة استعلامات DSL معقدة، وتوفير تجربة أفضل لإدارة البيانات والتحليل. </td>
    </tr> 
    <tr>
        <td> <img src="docs/zenfeed/assets/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/glidea/zenfeed">zenfeed</a> </td>
        <td> تمكين RSS بالذكاء الاصطناعي، تصفية تلقائية وتلخيص ودفع المعلومات المهمة للتغلب على حمولة المعلومات الزائدة. </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="agent">أطر عمل وكلاء الذكاء الاصطناعي</span>

<table>
    <tr>
        <td width=80> <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/smolagents/mascot_smol.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/huggingface/smolagents/tree/main"> smolagents </a> </td>
        <td> أبسط طريقة لبناء وكلاء رائعين. الوكلاء يكتبون كود Python لاستدعاء الأدوات وتنسيق وكلاء آخرين. دعم أولوية للنماذج المفتوحة مثل DeepSeek-R1!  </td>
    </tr>
    <tr>
        <td><img src="https://yomo.run/yomo-logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/yomo/README.md">YoMo</a></td>
        <td>إطار عمل Serverless واحد مع دعم اللغات قوية الكتابة لاستدعاء دوال LLM</td>
     </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/superagentxai/superagentX/refs/heads/master/docs/logo/icononly_transparent_nobuffer.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/superagentx/README.md">SuperAgentX</a> </td>
        <td>SuperAgentX: إطار عمل ذكاء اصطناعي مفتوح المصدر خفيف مبني للتطبيقات متعددة الوكلاء المستقلة مع قدرات الذكاء الاصطناعي العام (AGI).</td>
    </tr>
    <tr>
        <td> <img src="https://panda.fans/_assets/favicons/apple-touch-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/anda/README.md">Anda</a> </td>
        <td>إطار عمل Rust لتطوير وكلاء الذكاء الاصطناعي، مصمم لبناء شبكة من وكلاء الذكاء الاصطناعي قابلة للتركيب بدرجة عالية، مستقلة، وذات ذاكرة دائمة.</td>
    </tr>
    <tr>
        <td> <img src="https://rig.rs/assets/favicon.png" alt="Icon" width="64" height="auto" alt="Rig (Rust)" /> </td>
        <td> <a href="https://rig.rs">RIG</a> </td>
        <td>بناء تطبيقات LLM نمطية وقابلة للتوسع في Rust.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/longevity-genie/chat-ui/11c6647c83f9d2de21180b552474ac5ffcf53980/static/geneticsgenie/icon-128x128.png" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://github.com/longevity-genie/just-chat">Just-Chat</a> </td>
        <td>Make your LLM agent and chat with it simple and fast!</td>
     </tr>
    <tr>
        <td> <img src="https://www.papersgpt.com/images/logo/favicon.ico" alt="PapersGPT" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/papersgpt/papersgpt-for-zotero">PapersGPT</a> </td>
        <td> PapersGPT هي مكونة على منصة Zotero تدمج مع DeepSeek ونماذج ذكاء اصطناعي أخرى لقراءة المقالات في Zotero بسرعة.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/rss-translator/RSS-Translator/main/core/static/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/rss_translator/README.md"> RSS Translator </a> </td>
        <td> ترجم تغذيات RSS إلى لغتك! </td>
    </tr>
    <tr>
        <td> <img src="https://relingo.net/assets/images/relingo-logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://relingo.net"> Relingo </a> </td>
        <td> ابنِ وأتقن مفرداتك أثناء تصفح المواقع ومشاهدة يوتيوب! </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/ysnows/enconvo_media/main/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/enconvo/README.md"> Enconvo </a> </td>
        <td> Enconvo هو محرر الذكاء الاصطناعي لعصر الذكاء الاصطناعي، نقطة الدخول لجميع وظائف الذكاء الاصطناعي، ومساعد ذكي مفيد.</td>
    </tr>
    <tr>
        <td><img src="https://github.com/kangfenmao/cherry-studio/blob/main/src/renderer/src/assets/images/logo.png?raw=true" alt="Icon" width="64" height="auto" style="border-radius: 10px" /></td>
        <td><a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/cherrystudio/README.md">Cherry Studio</a></td>
        <td>مساعد سطح مكتب ذكي قوي للمنتجين</td>
    </tr>
    <tr>
        <td> <img src="https://tomemo.top/images/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/tomemo/README.md"> ToMemo (iOS, ipadOS) </a> </td>
        <td> تطبيق iOS يجمع بين دفتر العبارات وتاريخ الحافظة ولوحة المفاتيح مع نمذجة ذكاء اصطناعي متكاملة للاستخدام السريع في لوحة المفاتيح.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/buxuku/video-subtitle-master/refs/heads/main/resources/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/buxuku/video-subtitle-master">Video Subtitle Master</a></td>
        <td> إنتاج جماعي لترجمات الفيديو، مع القدرة على ترجمة الترجمات إلى لغات أخرى. هذه أداة من جانب العميل تدعم منصتي Mac وWindows وتتكامل مع خدمات ترجمة متعددة مثل Baidu وVolcengine وDeepLx وOpenAI وDeepSeek وOllama.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/UnknownEnergy/chatgpt-api/blob/master/dist/assets/chatworm-72x72.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/UnknownEnergy/chatgpt-api/blob/master/README.md">Chatworm</a> </td>
        <td> Chatworm تطبيق ويب لنماذج LLM متطورة متعددة، مفتوح المصدر ومتوفر أيضاً على Android. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/icon_512x512@2x.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/tisfeng/Easydict">Easydict</a></td>
        <td> Easydict قاموس ترجمة موجز وسهل الاستخدام لتطبيق macOS يتيح لك البحث عن الكلمات أو ترجمة النص بسهولة وأناقة. يدعم استدعاء واجهات نماذج اللغة الكبيرة للترجمة.</td>
    </tr>
    <tr>
        <td> <img src="https://www.raycast.com/favicon-production.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/raycast/README.md">Raycast</a></td>
        <td> <a href="https://raycast.com/?via=ViGeng">Raycast</a> أداة إنتاجية لـ macOS تتيح لك التحكم في أدواتك بضغطات مفاتيح قليلة. تدعم امتدادات متنوعة بما في ذلك DeepSeek AI.</td>
    </tr>
    <tr>
        <td> <img src="./docs/chatpdflocal/assets/chatpdflocal-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.chatpdflocal.com">ChatPDFLocal</a> </td>
        <td> ChatPDFLocal تطبيق Mac OS مدعوم بالذكاء الاصطناعي لمساعدة الدردشة مع PDF، يعمل بسلاسة مع DeepSeek ونماذج ذكاء اصطناعي متعددة أخرى لتحسين كفاءة قراءتك. </td>
    </tr>
    <tr>
        <td> <img src="https://niceprompt.app/favicon.ico" alt="Icon" width="64" height="auto" /> </td> <td> <a href="https://niceprompt.app">Nice Prompt</a></td> <td> <a href="https://niceprompt.app">Nice Prompt</a> نظم وشارك واستخدم رسائلك في محرر الكود، مع Cursor وVSCode.</td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/193405629?s=200&v=4" alt="PHP Client" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-php/deepseek-php-client/blob/master/README.md">PHP Client</a> </td>
        <td> Deepseek PHP Client مكتبة عميل PHP قوية ومدفوعة من المجتمع للتكامل السلس مع واجهة Deepseek. </td>
    </tr>
        <tr>
  <td>
    <img
      src="https://github.com/tornikegomareli/DeepSwiftSeek/blob/main/logo.webp"
      alt="DeepSwiftSeek Logo"
      width="64"
      height="auto"
    />
  </td>
  <td>
    <a href="https://github.com/tornikegomareli/DeepSwiftSeek/blob/main/README.md">DeepSwiftSeek</a>
  </td>
  <td>
    DeepSwiftSeek عبارة عن مكتبة عميل Swift خفيفة وقوية في الوقت نفسه، وتوفر تكاملاً ممتازاً مع واجهة DeepSeek.
    توفر تزامناً سهلاً في Swift من أجل الدردشة، البث المتدفق، إكمال FIM (الملء في المنتصف) وغيرها.
  </td>
</tr>
        <td> <img src="https://raw.githubusercontent.com/cohesion-org/deepseek-go/refs/heads/main/internal/images/deepseek-go.png" alt="Go Client" width="64" height="auto"> </td>
        <td> <a href="https://github.com/cohesion-org/deepseek-go/blob/main/README.md">Deepseek Go</a> </td>
        <td>  عميل DeepSeek مكتوب بلغة Go يدعم نماذج الدردشة والاستدلال، ويدعم أيضاً مزودين خارجيين مثل Azure وOpenRouter وغيرهما. </td>
    </tr>
    <tr>
        <td> <img src="./docs/zotero/assets/zotero-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/zotero/README_cn.md">Zotero</a></td>
        <td> <a href="https://www.zotero.org">Zotero</a> أداة مجانية وسهلة الاستخدام تساعدك على جمع الأبحاث وتنظيمها وتعليقها والاستشهاد بها ومشاركتها. ويمكنها استخدام DeepSeek كخدمة ترجمة.</td>
    </tr>
    <tr>
        <td> <img src="https://b3log.org/images/brand/siyuan-128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/SiYuan/README.md">SiYuan</a> </td>
        <td> SiYuan نظام إدارة معرفة شخصي يركز على الخصوصية ويدعم الاستخدام دون اتصال بالكامل بالإضافة إلى مزامنة بيانات مشفّرة من طرف إلى طرف.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/ArvinLovegood/go-stock/raw/master/build/appicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/ArvinLovegood/go-stock/blob/master/README.md">go-stock</a> </td>
        <td>go-stock عارض بيانات الأسهم الصينية مبني بـ Wails مع NativeUI ومدعوم بنماذج اللغة الكبيرة.</td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/102771702?s=200&v=4" alt="Wordware" width="64" height="auto" /> </td>
        <td> <a href="docs/wordware/README.md">Wordware</a> </td>
        <td><a href="https://www.wordware.ai/">Wordware</a> مجموعة أدوات تمكن أي شخص من بناء وتكرار ونشر مجموعة أدوات الذكاء الاصطناعي باستخدام اللغة الطبيعية فقط.</td>
    </tr>
    <tr>
        <td> <img src="https://framerusercontent.com/images/xRJ6vNo9mUYeVNxt0KITXCXEuSk.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/langgenius/dify/">Dify</a> </td>
        <td> <a href="https://dify.ai/">Dify</a> منصة تطوير تطبيقات LLM تدعم نماذج DeepSeek لإنشاء المساعدين وسير العمل ومولدات النصوص والمزيد. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/enricoros/big-AGI/refs/heads/v2-dev/public/favicon.ico" alt="Big-AGI" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/enricoros/big-AGI/blob/v2-dev/README.md">Big-AGI</a> </td>
        <td><a href="https://big-agi.com/">Big-AGI</a> هي مجموعة ذكاء اصطناعي رائدة مصممة لتسهيل الوصول إلى الذكاء الاصطناعي المتقدم للجميع.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/LiberSonora/LiberSonora/blob/main/assets/avatar.jpeg?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/LiberSonora/LiberSonora/blob/main/README_en.md">LiberSonora</a> </td>
        <td> LiberSonora، التي تعني "صوت الحرية"، هي مجموعة أدوات كتب صوتية قوية مفتوحة المصدر مدعومة بالذكاء الاصطناعي تتضمن ميزات مثل استخراج الترجمات الذكي، توليد عناوين بالذكاء الاصطناعي، الترجمة متعددة اللغات، مع دعم تسريع GPU ومعالجة دفعية دون اتصال.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/ripperhe/Bob/master/docs/_media/icon_128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://bobtranslate.com/">Bob</a></td>
        <td> <a href="https://bobtranslate.com/">Bob</a> أداة ترجمة وOCR لنظام macOS جاهزة للاستخدام في أي تطبيق — مباشرة!</td>
    </tr>
    <tr>
        <td> <img src="https://agenticflow.ai/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://agenticflow.ai/">AgenticFlow</a> </td>
        <td> <a href="https://agenticflow.ai/">AgenticFlow</a> منصة بدون كود حيث يبني المسوقون سير عمل ذكاء اصطناعي وكيل لأتمتة الانطلاق للسوق، مدعومة بمئات التطبيقات اليومية كأدوات لوكلاء الذكاء الاصطناعي.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/ZGGSONG/STranslate/raw/main/img/favicon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://stranslate.zggsong.com/en/">STranslate</a></td>
        <td> <a href="https://stranslate.zggsong.com/en/">STranslate</a>（Windows） أداة ترجمة OCR جاهزة مطورة بـ WPF </td>
    </tr>
    <tr>
        <td> <img src="https://devinci.onicai.com/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://devinci.onicai.com/">DeVinci</a></td>
        <td> <a href="https://devinci.onicai.com/">DeVinci</a> تطبيق دردشة ذكاء اصطناعي لامركزي شامل للدردشة الخاصة مع نماذج LLM مفتوحة المصدر.</td>
    </tr>
     <tr>
        <td> <img src="https://github.com/user-attachments/assets/5e16beb0-993e-47bf-807e-7c8804b313a2" alt="Asp Client" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Anwar-alhitar/Deepseek.Asp.Client/blob/master/README.md">ASP Client</a> </td>
        <td><a href="https://github.com/Anwar-alhitar/Deepseek.Asp.Client/blob/master/README.md">Deepseek.ASPClient</a> غلاف ASP.NET خفيف لواجهة Deepseek AI، مصمم لتبسيط معالجة النصوص المدفوعة بالذكاء الاصطناعي في تطبيقات .NET.. </td>
    </tr>
    <tr>
        <td> <img src="https://www.gptaiflow.tech/logo.png" alt="gpt-ai-flow-logo" width="64" height="auto" /> </td>
        <td> <a href="https://www.gptaiflow.tech/docs/product/api-keys-setup#setup-deepseek-api-keys">GPT AI Flow</a></td>
        <td>
            السلاح الإنتاجي النهائي المبني من المهندسين لعشاق الكفاءة (أنفسهم): <a href="https://www.gptaiflow.tech/">GPT AI Flow</a>
            <ul>
                <li>`Shift+Alt+Space` تنشيط مركز الذكاء المكتبي</li>
                <li>تخزين محلي مشفر</li>
                <li>محرك تعليمات مخصص</li>
                <li>استدعاء عند الطلب بدون ربط اشتراك</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/b09f17a8-936d-4dac-8b24-1682d52c9a3c" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/alecm20/story-flicks">Story-Flicks</a></td>
        <td>بجملة واحدة فقط، يمكنك بسرعة إنشاء مقاطع فيديو قصيرة عالية الدقة للقصص، مع دعم نماذج مثل DeepSeek.</td>
    </tr>
    <tr>
        <td> <img src="https://prompt.16x.engineer/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/16x_prompt/README.md">16x Prompt</a> </td>
        <td> <a href="https://prompt.16x.engineer/">16x Prompt</a> أداة برمجة ذكاء اصطناعي مع إدارة السياق. تساعد المطورين على إدارة سياق الكود المصدري وصياغة التعليمات للمهام البرمجية المعقدة على قواعد الكود الحالية.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/Alpha派/assets/favicon1.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/Alpha派/README.md"> Alpha Pai </a> </td>
        <td> مساعد بحث ذكاء اصطناعي / بوابة المعلومات المالية من الجيل القادم مدفوعة بالذكاء الاصطناعي.<br>وكيل للمستثمرين لحضور الاجتماعات وتدوين الملاحظات، بالإضافة إلى توفير خدمات البحث والأسئلة والأجوبة للمعلومات المالية والتحليل الكمي لأبحاث الاستثمار.</td>
    </tr>
        <td> <img src="https://docs.xark-argo.com/img/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.xark-argo.com">argo</a> </td>
        <td>قم بتنزيل وتشغيل نماذج Ollama وHuggingface محلياً مع RAG على Mac/Windows/Linux. يدعم أيضاً واجهة برمجة تطبيقات LLM.</td>
    </tr>
    <tr>
        <td> <img src="https://www.petercat.ai/images/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.petercat.ai">PeterCat</a> </td>
        <td> نظام تكوين وكيل أسئلة وأجوبة تفاعلي، حلول نشر ذاتية الاستضافة، ومجموعة تطوير تطبيقات شاملة وسهلة الاستخدام، تتيح لك إنشاء روبوتات أسئلة وأجوبة ذكية لمستودعات GitHub الخاصة بك.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/labring/FastGPT/refs/heads/main/.github/imgs/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://fastgpt.cn/en">FastGPT</a> </td>
        <td>
            FastGPT منصة قاعدة معرفة ذكاء اصطناعي مفتوحة المصدر مبنية على نماذج اللغة الكبيرة (LLMs)، تدعم نماذج متنوعة بما في ذلك DeepSeek وOpenAI. نوفر قدرات جاهزة للاستخدام لمعالجة البيانات، استدعاء النماذج، استرجاع RAG، وتنسيق سير عمل الذكاء الاصطناعي المرئي، مما يمكنك من بناء تطبيقات ذكاء اصطناعي متطورة بسهولة.
        </td>
   </tr>
   <tr>
        <td> <img src="./docs/ruzhiai_note/assets/play_store_512.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/ruzhiai_note/README.md">RuZhi AI Notes</a> </td>
        <td>RuZhi AI Notes أداة إدارة معرفة ذكية مدعومة بالذكاء الاصطناعي، توفر خدمات إدارة وتطبيق معرفة شاملة تشمل البحث والاستكشاف بالذكاء الاصطناعي، تحويل نتائج الذكاء الاصطناعي إلى ملاحظات، إدارة وتنظيم الملاحظات، عرض ومشاركة المعرفة. متكاملة مع نموذج DeepSeek لتوفير مخرجات أكثر استقراراً وجودة أعلى.</td>
    </tr>
    <tr>
        <td> <img src="https://cdn.link-ai.tech/doc/CoW%20logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/zhayujie/chatgpt-on-wechat">Chatgpt-on-Wechat</a> </td>
        <td> Chatgpt-on-Wechat(CoW) إطار عمل روبوت دردشة مرن يدعم التكامل السلس لنماذج LLM متعددة، بما في ذلك DeepSeek وOpenAI وClaude وQwen وغيرها، في منصات أو برمجيات مكتبية شائعة الاستخدام مثل حسابات WeChat الرسمية وWeCom وFeishu وDingTalk والمواقع. كما يدعم مجموعة واسعة من الإضافات المخصصة. </td>
    </tr>
    <tr>
        <td> <img src="https://athenalab.ai/assets/favicon/favicon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://athenalab.ai/">Athena</a> </td>
        <td>أول ذكاء اصطناعي عام مستقل في العالم مع هندسة معرفية متقدمة وقدرات استدلال شبيهة بالبشر، مصمم لمواجهة التحديات الحقيقية المعقدة.</td>
    </tr>
    <tr>
        <td> <img src="https://maxkb.cn/images/favicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/1Panel-dev/MaxKB">MaxKB</a> </td>
        <td> <a href="https://maxkb.cn/">MaxKB</a> روبوت دردشة RAG مرن وجاهز للاستخدام. </td>
    </tr>
    <tr>
        <td> <img src="./docs/TigerGPT/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://ttm.financial/gpt">TigerGPT</a> </td>
        <td>TigerGPT هو أول مساعد استثماري ذكاء اصطناعي مالي من نوعه مبني على OpenAI، طوره مجموعة Tiger. يهدف TigerGPT إلى توفير دعم اتخاذ قرارات استثمارية ذكي للمستثمرين. في 18 فبراير 2025، دمج TigerGPT رسمياً نموذج DeepSeek-R1 لتوفير خدمات أسئلة وأجوبة عبر الإنترنت تدعم الاستدلال العميق للمستخدمين. </td>
    </tr>
    <tr>
        <td> <img src="./docs/HIX.AI/assets/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://hix.ai">HIX.AI</a> </td>
        <td>جرب DeepSeek مجاناً واستمتع بدردشة ذكاء اصطناعي غير محدودة على HIX.AI. استخدم DeepSeek R1 للدردشة بالذكاء الاصطناعي، الكتابة، البرمجة والمزيد. اختبر دردشة الذكاء الاصطناعي من الجيل القادم الآن!</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/sharmt1411/askanywhere/blob/main/icon/Depth_8,_Frame_0explore-%E8%A7%92%E6%A0%87.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/sharmt1411/askanywhere">Askanywhere</a> </td>
        <td>حدد النص في أي مكان وابدأ محادثة مع Deepseek</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/OJZen/1chat/raw/refs/heads/main/doc/assets/icon.ico?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/OJZen/1chat">1chat</a> </td>
        <td>تطبيق iOS يتيح لك الدردشة مع نموذج DeepSeek-R1 محلياً.</td>
    </tr>
    <tr>
        <td> <img src="https://chatlabsai.com/assets/logo/logo.png" alt="iOS AI Chatbot" width="64" height="auto" /> </td>
        <td> <a href="https://chatlabsai.com">Access 250+ text, image LLMs in one app</a> </td>
        <td> 1AI iOS Chatbot يتكامل مع أكثر من 250 نموذج نص وصورة وصوت يتيح للمستخدمين الدردشة مع أي نموذج في العالم بما في ذلك نماذج Deepseek R1 وDeepseek V3.</td>
    </tr>
    <tr>
        <td> <img src="./docs/PopAi/assets/logo.svg" alt="PopAi" width="64" height="auto" /> </td>
        <td> <a href="https://popai.pro">PopAi</a> </td>
        <td>PopAi تطلق DeepSeek R1! استمتع بأداء سريع البرق وبدون تأخير مع PopAi. قم بالتبديل بسلاسة بين البحث عبر الإنترنت تشغيل/إيقاف.</td>
    </tr>
    <tr>
        <td> <img src="https://pot-app.com/logo/icon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://pot-app.com/">Pot</a></td>
        <td> <a href="https://pot-app.com/">Pot</a> 🌈 برنامج متعدد المنصات لترجمة النصوص والتعرف عليها. </td>
    </tr>
    <tr>
        <td><img src="https://github.com/Byaidu/PDFMathTranslate/raw/main/docs/images/banner.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/Byaidu/PDFMathTranslate">PDFMathTranslate</a></td>
        <td>PDF Math Translate أداة ترجمة ثنائية اللغة شاملة مبنية على الذكاء الاصطناعي تحافظ على تخطيط مستندات PDF بالكامل.</td>
    </tr>
    <tr>
        <td><img src="https://github.com/Richasy/Bili.Copilot/raw/master/assets/StoreLogo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/Richasy/Bili.Copilot">Bili.Copilot</a></td>
        <td>Bilibili عميل سطح مكتب Windows من طرف ثالث، تطبيق أصلي مبني بـ Windows App SDK.</td>
    </tr>
    <tr>
        <td><img src="https://www.tensorbounce.com/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://www.tensorbounce.com/">LawAgent</a></td>
        <td>LawAgent منتج ذكاء اصطناعي قانوني طوره فريق Tensorbounce، يدمج قاعدة معرفة مع قدرات AI Agent. يتميز بمستودع ضخم من عشرات الملايين من نقاط البيانات الرسمية المتعلقة بالقانون كما يتيح تكوينات قاعدة معرفة مخصصة. الوضع المهني يستفيد من قدرات الاستدلال لـ DeepSeek-R1 لمساعدة المستخدمين في التحليل القانوني، مراجعة العقود، توليد المستندات، ترجمة الملفات، وسيناريوهات قانونية أخرى.</td>
    </tr>
    <tr>
        <td width=80> <img src="docs/AlphaBot/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://alphabot.x-pai.com/">AlphaBot</a> </td>
        <td> AlphaBot مساعد تحليل أسهم ذكي يدمج بيانات متعددة المصادر مع تقنية تحليل الذكاء الاصطناعي لتوفير التحليل الفني والتنبؤات وتقييم المخاطر، مساعداً المستثمرين على اتخاذ قرارات تداول مبنية على البيانات. يدعم نشر بنقرة واحدة، عمليات سهلة، يدعم منصات Windows/Linux/MacOS وغيرها</td>
     <tr>
        <td><img src="https://h1.appinn.me/file/1741929316827_21.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/jiqi136/DS-AI">Multi-platform connected DeepSeek</a></td>
        <td>Leveraging the three-channel AI engine powered by DeepSeek Official, Alibaba Cloud, and Douyin Volcano, it continuously evolves its         intelligence. Additionally, it employs a hybrid mode combining "online search + deep thinking".</td>
    </tr>
    <tr>
    <td><img src="docs/remio/assets/remio_icon.png" alt="Icon" width="64" height="auto" /></td>
    <td><a href="https://www.remio.ai/">remio</a></td>
    <td>remio مركز معرفة شخصي مدعوم بالذكاء الاصطناعي يبني قواعد معرفة شخصية من خلال التقاط تلقائي لمحتوى الويب المتصفح، تحليل الملفات المحلية، ودمج الملاحظات الشخصية. يمكن البحث والأسئلة والأجوبة بالللغة الطبيعية داخل قاعدة معرفتك الشخصية للحصول على رؤى فورية مع توفير مساعدة كتابة ذكية—تتكيف مع أسلوبك لتبسيط الصياغة والتحسين وإكمال المحتوى بسهولة. مصمم مع تخزين محلي أولاً، remio يعطي الأولوية لخصوصية البيانات مع تمركز المعلومات المجزأة لتحقيق أقصى إنتاجية.</td>
    </tr> 
    <tr>
    <td><img src="docs/DocKit/assets/dockit.png" alt="Icon" width="64" height="auto" /></td>
    <td><a href="https://dockit.geekfun.club/">DocKit</a></td>
    <td>DocKit عميل GUI سطح مكتب مدعوم بالذكاء الاصطناعي مصمم لقاعدة بيانات NoSQL، يدعم Elasticsearch وOpenSearch عبر Mac وWindows وLinux. من خلال التكامل مع نماذج كبيرة مثل DeepSeek، يمكن لـ DocKit مساعدة المطورين على كتابة استعلامات DSL معقدة، وتوفير تجربة أفضل لإدارة البيانات والتحليل. </td>
    </tr> 
    <tr>
        <td> <img src="docs/zenfeed/assets/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/glidea/zenfeed">zenfeed</a> </td>
        <td> تمكين RSS بالذكاء الاصطناعي، تصفية تلقائية وتلخيص ودفع المعلومات المهمة للتغلب على حمولة المعلومات الزائدة. </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="agent">أطر عمل وكلاء الذكاء الاصطناعي</span>

<table>
    <tr>
        <td width=80> <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/smolagents/mascot_smol.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/huggingface/smolagents/tree/main"> smolagents </a> </td>
        <td> أبسط طريقة لبناء وكلاء رائعين. الوكلاء يكتبون كود Python لاستدعاء الأدوات وتنسيق وكلاء آخرين. دعم أولوية للنماذج المفتوحة مثل DeepSeek-R1!  </td>
    </tr>
    <tr>
        <td><img src="https://yomo.run/yomo-logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/yomo/README.md">YoMo</a></td>
        <td>إطار عمل Serverless واحد مع دعم اللغات قوية الكتابة لاستدعاء دوال LLM</td>
     </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/superagentxai/superagentX/refs/heads/master/docs/logo/icononly_transparent_nobuffer.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/superagentx/README.md">SuperAgentX</a> </td>
        <td>SuperAgentX: إطار عمل ذكاء اصطناعي مفتوح المصدر خفيف مبني للتطبيقات متعددة الوكلاء المستقلة مع قدرات الذكاء الاصطناعي العام (AGI).</td>
    </tr>
    <tr>
        <td> <img src="https://panda.fans/_assets/favicons/apple-touch-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/anda/README.md">Anda</a> </td>
        <td>إطار عمل Rust لتطوير وكلاء الذكاء الاصطناعي، مصمم لبناء شبكة من وكلاء الذكاء الاصطناعي قابلة للتركيب بدرجة عالية، مستقلة، وذات ذاكرة دائمة.</td>
    </tr>
    <tr>
        <td> <img src="https://rig.rs/assets/favicon.png" alt="Icon" width="64" height="auto" alt="Rig (Rust)" /> </td>
        <td> <a href="https://rig.rs">RIG</a> </td>
        <td>بناء تطبيقات LLM نمطية وقابلة للتوسع في Rust.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/longevity-genie/chat-ui/11c6647c83f9d2de21180b552474ac5ffcf53980/static/geneticsgenie/icon-128x128.png" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://github.com/longevity-genie/just-chat">Just-Chat</a> </td>
        <td>Make your LLM agent and chat with it simple and fast!</td>
     </tr>
    <tr>
        <td> <img src="https://www.papersgpt.com/images/logo/favicon.ico" alt="PapersGPT" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/papersgpt/papersgpt-for-zotero">PapersGPT</a> </td>
        <td> PapersGPT هي مكونة على منصة Zotero تدمج مع DeepSeek ونماذج ذكاء اصطناعي أخرى لقراءة المقالات في Zotero بسرعة.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/rss-translator/RSS-Translator/main/core/static/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/rss_translator/README.md"> RSS Translator </a> </td>
        <td> ترجم تغذيات RSS إلى لغتك! </td>
    </tr>
    <tr>
        <td> <img src="https://relingo.net/assets/images/relingo-logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://relingo.net"> Relingo </a> </td>
        <td> ابنِ وأتقن مفرداتك أثناء تصفح المواقع ومشاهدة يوتيوب! </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/ysnows/enconvo_media/main/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/enconvo/README.md"> Enconvo </a> </td>
        <td> Enconvo هو محرر الذكاء الاصطناعي لعصر الذكاء الاصطناعي، نقطة الدخول لجميع وظائف الذكاء الاصطناعي، ومساعد ذكي مفيد.</td>
    </tr>
    <tr>
        <td><img src="https://github.com/kangfenmao/cherry-studio/blob/main/src/renderer/src/assets/images/logo.png?raw=true" alt="Icon" width="64" height="auto" style="border-radius: 10px" /></td>
        <td><a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/cherrystudio/README.md">Cherry Studio</a></td>
        <td>مساعد سطح مكتب ذكي قوي للمنتجين</td>
    </tr>
    <tr>
        <td> <img src="https://tomemo.top/images/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/tomemo/README.md"> ToMemo (iOS, ipadOS) </a> </td>
        <td> تطبيق iOS يجمع بين دفتر العبارات وتاريخ الحافظة ولوحة المفاتيح مع نمذجة ذكاء اصطناعي متكاملة للاستخدام السريع في لوحة المفاتيح.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/buxuku/video-subtitle-master/refs/heads/main/resources/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/buxuku/video-subtitle-master">Video Subtitle Master</a></td>
        <td> إنتاج جماعي لترجمات الفيديو، مع القدرة على ترجمة الترجمات إلى لغات أخرى. هذه أداة من جانب العميل تدعم منصتي Mac وWindows وتتكامل مع خدمات ترجمة متعددة مثل Baidu وVolcengine وDeepLx وOpenAI وDeepSeek وOllama.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/UnknownEnergy/chatgpt-api/blob/master/dist/assets/chatworm-72x72.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/UnknownEnergy/chatgpt-api/blob/master/README.md">Chatworm</a> </td>
        <td> Chatworm تطبيق ويب لنماذج LLM متطورة متعددة، مفتوح المصدر ومتوفر أيضاً على Android. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/icon_512x512@2x.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/tisfeng/Easydict">Easydict</a></td>
        <td> Easydict قاموس ترجمة موجز وسهل الاستخدام لتطبيق macOS يتيح لك البحث عن الكلمات أو ترجمة النص بسهولة وأناقة. يدعم استدعاء واجهات نماذج اللغة الكبيرة للترجمة.</td>
    </tr>
    <tr>
        <td> <img src="https://www.raycast.com/favicon-production.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/raycast/README.md">Raycast</a></td>
        <td> <a href="https://raycast.com/?via=ViGeng">Raycast</a> أداة إنتاجية لـ macOS تتيح لك التحكم في أدواتك بضغطات مفاتيح قليلة. تدعم امتدادات متنوعة بما في ذلك DeepSeek AI.</td>
    </tr>
    <tr>
        <td> <img src="./docs/chatpdflocal/assets/chatpdflocal-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.chatpdflocal.com">ChatPDFLocal</a> </td>
        <td> ChatPDFLocal تطبيق Mac OS مدعوم بالذكاء الاصطناعي لمساعدة الدردشة مع PDF، يعمل بسلاسة مع DeepSeek ونماذج ذكاء اصطناعي متعددة أخرى لتحسين كفاءة قراءتك. </td>
    </tr>
    <tr>
        <td> <img src="https://niceprompt.app/favicon.ico" alt="Icon" width="64" height="auto" /> </td> <td> <a href="https://niceprompt.app">Nice Prompt</a></td> <td> <a href="https://niceprompt.app">Nice Prompt</a> نظم وشارك واستخدم رسائلك في محرر الكود، مع Cursor وVSCode.</td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/193405629?s=200&v=4" alt="PHP Client" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-php/deepseek-php-client/blob/master/README.md">PHP Client</a> </td>
        <td> Deepseek PHP Client مكتبة عميل PHP قوية ومدفوعة من المجتمع للتكامل السلس مع واجهة Deepseek. </td>
    </tr>
        <tr>
  <td>
    <img
      src="https://github.com/tornikegomareli/DeepSwiftSeek/blob/main/logo.webp"
      alt="DeepSwiftSeek Logo"
      width="64"
      height="auto"
    />
  </td>
  <td>
    <a href="https://github.com/tornikegomareli/DeepSwiftSeek/blob/main/README.md">DeepSwiftSeek</a>
  </td>
  <td>
    DeepSwiftSeek عبارة عن مكتبة عميل Swift خفيفة وقوية في الوقت نفسه، وتوفر تكاملاً ممتازاً مع واجهة DeepSeek.
    توفر تزامناً سهلاً في Swift من أجل الدردشة، البث المتدفق، إكمال FIM (الملء في المنتصف) وغيرها.
  </td>
</tr>
        <td> <img src="https://raw.githubusercontent.com/cohesion-org/deepseek-go/refs/heads/main/internal/images/deepseek-go.png" alt="Go Client" width="64" height="auto"> </td>
        <td> <a href="https://github.com/cohesion-org/deepseek-go/blob/main/README.md">Deepseek Go</a> </td>
        <td>  عميل DeepSeek مكتوب بلغة Go يدعم نماذج الدردشة والاستدلال، ويدعم أيضاً مزودين خارجيين مثل Azure وOpenRouter وغيرهما. </td>
    </tr>
    <tr>
        <td> <img src="./docs/zotero/assets/zotero-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/zotero/README_cn.md">Zotero</a></td>
        <td> <a href="https://www.zotero.org">Zotero</a> أداة مجانية وسهلة الاستخدام تساعدك على جمع الأبحاث وتنظيمها وتعليقها والاستشهاد بها ومشاركتها. ويمكنها استخدام DeepSeek كخدمة ترجمة.</td>
    </tr>
    <tr>
        <td> <img src="https://b3log.org/images/brand/siyuan-128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/SiYuan/README.md">SiYuan</a> </td>
        <td> SiYuan نظام إدارة معرفة شخصي يركز على الخصوصية ويدعم الاستخدام دون اتصال بالكامل بالإضافة إلى مزامنة بيانات مشفّرة من طرف إلى طرف.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/ArvinLovegood/go-stock/raw/master/build/appicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/ArvinLovegood/go-stock/blob/master/README.md">go-stock</a> </td>
        <td>go-stock عارض بيانات الأسهم الصينية مبني بـ Wails مع NativeUI ومدعوم بنماذج اللغة الكبيرة.</td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/102771702?s=200&v=4" alt="Wordware" width="64" height="auto" /> </td>
        <td> <a href="docs/wordware/README.md">Wordware</a> </td>
        <td><a href="https://www.wordware.ai/">Wordware</a> مجموعة أدوات تمكن أي شخص من بناء وتكرار ونشر مجموعة أدوات الذكاء الاصطناعي باستخدام اللغة الطبيعية فقط.</td>
    </tr>
    <tr>
        <td> <img src="https://framerusercontent.com/images/xRJ6vNo9mUYeVNxt0KITXCXEuSk.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/langgenius/dify/">Dify</a> </td>
        <td> <a href="https://dify.ai/">Dify</a> منصة تطوير تطبيقات LLM تدعم نماذج DeepSeek لإنشاء المساعدين وسير العمل ومولدات النصوص والمزيد. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/enricoros/big-AGI/refs/heads/v2-dev/public/favicon.ico" alt="Big-AGI" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/enricoros/big-AGI/blob/v2-dev/README.md">Big-AGI</a> </td>
        <td><a href="https://big-agi.com/">Big-AGI</a> هي مجموعة ذكاء اصطناعي رائدة مصممة لتسهيل الوصول إلى الذكاء الاصطناعي المتقدم للجميع.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/LiberSonora/LiberSonora/blob/main/assets/avatar.jpeg?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/LiberSonora/LiberSonora/blob/main/README_en.md">LiberSonora</a> </td>
        <td> LiberSonora، التي تعني "صوت الحرية"، هي مجموعة أدوات كتب صوتية قوية مفتوحة المصدر مدعومة بالذكاء الاصطناعي تتضمن ميزات مثل استخراج الترجمات الذكي، توليد عناوين بالذكاء الاصطناعي، الترجمة متعددة اللغات، مع دعم تسريع GPU ومعالجة دفعية دون اتصال.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/ripperhe/Bob/master/docs/_media/icon_128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://bobtranslate.com/">Bob</a></td>
        <td> <a href="https://bobtranslate.com/">Bob</a> أداة ترجمة وOCR لنظام macOS جاهزة للاستخدام في أي تطبيق — مباشرة!</td>
    </tr>
    <tr>
        <td> <img src="https://agenticflow.ai/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://agenticflow.ai/">AgenticFlow</a> </td>
        <td> <a href="https://agenticflow.ai/">AgenticFlow</a> منصة بدون كود حيث يبني المسوقون سير عمل ذكاء اصطناعي وكيل لأتمتة الانطلاق للسوق، مدعومة بمئات التطبيقات اليومية كأدوات لوكلاء الذكاء الاصطناعي.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/ZGGSONG/STranslate/raw/main/img/favicon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://stranslate.zggsong.com/en/">STranslate</a></td>
        <td> <a href="https://stranslate.zggsong.com/en/">STranslate</a>（Windows） أداة ترجمة OCR جاهزة مطورة بـ WPF </td>
    </tr>
    <tr>
        <td> <img src="https://devinci.onicai.com/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://devinci.onicai.com/">DeVinci</a></td>
        <td> <a href="https://devinci.onicai.com/">DeVinci</a> تطبيق دردشة ذكاء اصطناعي لامركزي شامل للدردشة الخاصة مع نماذج LLM مفتوحة المصدر.</td>
    </tr>
     <tr>
        <td> <img src="https://github.com/user-attachments/assets/5e16beb0-993e-47bf-807e-7c8804b313a2" alt="Asp Client" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Anwar-alhitar/Deepseek.Asp.Client/blob/master/README.md">ASP Client</a> </td>
        <td><a href="https://github.com/Anwar-alhitar/Deepseek.Asp.Client/blob/master/README.md">Deepseek.ASPClient</a> غلاف ASP.NET خفيف لواجهة Deepseek AI، مصمم لتبسيط معالجة النصوص المدفوعة بالذكاء الاصطناعي في تطبيقات .NET.. </td>
    </tr>
    <tr>
        <td> <img src="https://www.gptaiflow.tech/logo.png" alt="gpt-ai-flow-logo" width="64" height="auto" /> </td>
        <td> <a href="https://www.gptaiflow.tech/docs/product/api-keys-setup#setup-deepseek-api-keys">GPT AI Flow</a></td>
        <td>
            السلاح الإنتاجي النهائي المبني من المهندسين لعشاق الكفاءة (أنفسهم): <a href="https://www.gptaiflow.tech/">GPT AI Flow</a>
            <ul>
                <li>`Shift+Alt+Space` تنشيط مركز الذكاء المكتبي</li>
                <li>تخزين محلي مشفر</li>
                <li>محرك تعليمات مخصص</li>
                <li>استدعاء عند الطلب بدون ربط اشتراك</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/b09f17a8-936d-4dac-8b24-1682d52c9a3c" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/alecm20/story-flicks">Story-Flicks</a></td>
        <td>بجملة واحدة فقط، يمكنك بسرعة إنشاء مقاطع فيديو قصيرة عالية الدقة للقصص، مع دعم نماذج مثل DeepSeek.</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="agent">أطر عمل وكلاء الذكاء الاصطناعي</span>

<table>
    <tr>
        <td width=80> <img src="https://huggingface.co/datasets/huggingface/documentation-images/resolve/main/smolagents/mascot_smol.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/huggingface/smolagents/tree/main"> smolagents </a> </td>
        <td> أبسط طريقة لبناء وكلاء رائعين. الوكلاء يكتبون كود Python لاستدعاء الأدوات وتنسيق وكلاء آخرين. دعم أولوية للنماذج المفتوحة مثل DeepSeek-R1!  </td>
    </tr>
    <tr>
        <td><img src="https://yomo.run/yomo-logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/yomo/README.md">YoMo</a></td>
        <td>إطار عمل Serverless واحد مع دعم اللغات قوية الكتابة لاستدعاء دوال LLM</td>
     </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/superagentxai/superagentX/refs/heads/master/docs/logo/icononly_transparent_nobuffer.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/superagentx/README.md">SuperAgentX</a> </td>
        <td>SuperAgentX: إطار عمل ذكاء اصطناعي مفتوح المصدر خفيف مبني للتطبيقات متعددة الوكلاء المستقلة مع قدرات الذكاء الاصطناعي العام (AGI).</td>
    </tr>
    <tr>
        <td> <img src="https://panda.fans/_assets/favicons/apple-touch-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/anda/README.md">Anda</a> </td>
        <td>إطار عمل Rust لتطوير وكلاء الذكاء الاصطناعي، مصمم لبناء شبكة من وكلاء الذكاء الاصطناعي قابلة للتركيب بدرجة عالية، مستقلة، وذات ذاكرة دائمة.</td>
    </tr>
    <tr>
        <td> <img src="https://rig.rs/assets/favicon.png" alt="Icon" width="64" height="auto" alt="Rig (Rust)" /> </td>
        <td> <a href="https://rig.rs">RIG</a> </td>
        <td>بناء تطبيقات LLM نمطية وقابلة للتوسع في Rust.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/longevity-genie/chat-ui/11c6647c83f9d2de21180b552474ac5ffcf53980/static/geneticsgenie/icon-128x128.png" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://github.com/longevity-genie/just-chat">Just-Chat</a> </td>
        <td>اجعل وكيل LLM الخاص بك والدردشة معه بسيطاً وسريعاً!</td>
     </tr>
    <tr>
        <td> <img src="https://www.papersgpt.com/images/logo/favicon.ico" alt="PapersGPT" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/papersgpt/papersgpt-for-zotero">PapersGPT</a> </td>
        <td> PapersGPT هي مكونة على منصة Zotero تدمج مع DeepSeek ونماذج ذكاء اصطناعي أخرى لقراءة المقالات في Zotero بسرعة.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/rss-translator/RSS-Translator/main/core/static/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/rss_translator/README.md"> RSS Translator </a> </td>
        <td> ترجم تغذيات RSS إلى لغتك! </td>
    </tr>
    <tr>
        <td> <img src="https://relingo.net/assets/images/relingo-logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://relingo.net"> Relingo </a> </td>
        <td> ابنِ وأتقن مفرداتك أثناء تصفح المواقع ومشاهدة يوتيوب! </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/ysnows/enconvo_media/main/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/enconvo/README.md"> Enconvo </a> </td>
        <td> Enconvo هو محرر الذكاء الاصطناعي لعصر الذكاء الاصطناعي، نقطة الدخول لجميع وظائف الذكاء الاصطناعي، ومساعد ذكي مفيد.</td>
    </tr>
    <tr>
        <td><img src="https://github.com/kangfenmao/cherry-studio/blob/main/src/renderer/src/assets/images/logo.png?raw=true" alt="Icon" width="64" height="auto" style="border-radius: 10px" /></td>
        <td><a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/cherrystudio/README.md">Cherry Studio</a></td>
        <td>مساعد سطح مكتب ذكي قوي للمنتجين</td>
    </tr>
    <tr>
        <td> <img src="https://tomemo.top/images/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/tomemo/README.md"> ToMemo (iOS, ipadOS) </a> </td>
        <td> تطبيق iOS يجمع بين دفتر العبارات وتاريخ الحافظة ولوحة المفاتيح مع نمذجة ذكاء اصطناعي متكاملة للاستخدام السريع في لوحة المفاتيح.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/buxuku/video-subtitle-master/refs/heads/main/resources/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/buxuku/video-subtitle-master">Video Subtitle Master</a></td>
        <td> إنتاج جماعي لترجمات الفيديو، مع القدرة على ترجمة الترجمات إلى لغات أخرى. هذه أداة من جانب العميل تدعم منصتي Mac وWindows وتتكامل مع خدمات ترجمة متعددة مثل Baidu وVolcengine وDeepLx وOpenAI وDeepSeek وOllama.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/UnknownEnergy/chatgpt-api/blob/master/dist/assets/chatworm-72x72.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/UnknownEnergy/chatgpt-api/blob/master/README.md">Chatworm</a> </td>
        <td> تطبيق ويب لنماذج LLM متطورة متعددة، مفتوح المصدر ومتوفر أيضاً على Android. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/tisfeng/ImageBed/main/uPic/icon_512x512@2x.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/tisfeng/Easydict">Easydict</a></td>
        <td> Easydict قاموس ترجمة موجز وسهل الاستخدام لتطبيق macOS يتيح لك البحث عن الكلمات أو ترجمة النص بسهولة وأناقة. يدعم استدعاء واجهات نماذج اللغة الكبيرة للترجمة.</td>
    </tr>
    <tr>
        <td> <img src="https://www.raycast.com/favicon-production.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/raycast/README.md">Raycast</a></td>
        <td> <a href="https://raycast.com/?via=ViGeng">Raycast</a> أداة إنتاجية لـ macOS تتيح لك التحكم في أدواتك بضغطات مفاتيح قليلة. تدعم امتدادات متنوعة بما في ذلك DeepSeek AI.</td>
    </tr>
    <tr>
        <td> <img src="./docs/chatpdflocal/assets/chatpdflocal-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.chatpdflocal.com">ChatPDFLocal</a> </td>
        <td> ChatPDFLocal تطبيق Mac OS مدعوم بالذكاء الاصطناعي لمساعدة الدردشة مع PDF، يعمل بسلاسة مع DeepSeek ونماذج ذكاء اصطناعي متعددة أخرى لتحسين كفاءة قراءتك. </td>
    </tr>
    <tr>
        <td> <img src="https://niceprompt.app/favicon.ico" alt="Icon" width="64" height="auto" /> </td> <td> <a href="https://niceprompt.app">Nice Prompt</a></td> <td> <a href="https://niceprompt.app">Nice Prompt</a> نظم وشارك واستخدم رسائلك في محرر الكود، مع Cursor وVSCode.</td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/193405629?s=200&v=4" alt="PHP Client" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-php/deepseek-php-client/blob/master/README.md">PHP Client</a> </td>
        <td> Deepseek PHP Client مكتبة عميل PHP قوية ومدفوعة من المجتمع للتكامل السلس مع واجهة Deepseek. </td>
    </tr>
        <tr>
  <td>
    <img
      src="https://github.com/tornikegomareli/DeepSwiftSeek/blob/main/logo.webp"
      alt="DeepSwiftSeek Logo"
      width="64"
      height="auto"
    />
  </td>
  <td>
    <a href="https://github.com/tornikegomareli/DeepSwiftSeek/blob/main/README.md">DeepSwiftSeek</a>
  </td>
  <td>
    DeepSwiftSeek عبارة عن مكتبة عميل Swift خفيفة وقوية في الوقت نفسه، وتوفر تكاملاً ممتازاً مع واجهة DeepSeek.
    توفر تزامناً سهلاً في Swift من أجل الدردشة، البث المتدفق، إكمال FIM (الملء في المنتصف) وغيرها.
  </td>
</tr>
        <td> <img src="https://raw.githubusercontent.com/cohesion-org/deepseek-go/refs/heads/main/internal/images/deepseek-go.png" alt="Go Client" width="64" height="auto"> </td>
        <td> <a href="https://github.com/cohesion-org/deepseek-go/blob/main/README.md">Deepseek Go</a> </td>
        <td>  عميل DeepSeek مكتوب بلغة Go يدعم نماذج الدردشة والاستدلال، ويدعم أيضاً مزودين خارجيين مثل Azure وOpenRouter وغيرهما. </td>
    </tr>
    <tr>
        <td> <img src="./docs/zotero/assets/zotero-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/zotero/README_cn.md">Zotero</a></td>
        <td> <a href="https://www.zotero.org">Zotero</a> أداة مجانية وسهلة الاستخدام تساعدك على جمع الأبحاث وتنظيمها وتعليقها والاستشهاد بها ومشاركتها. ويمكنها استخدام DeepSeek كخدمة ترجمة.</td>
    </tr>
    <tr>
        <td> <img src="https://b3log.org/images/brand/siyuan-128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/SiYuan/README.md">SiYuan</a> </td>
        <td> SiYuan نظام إدارة معرفة شخصي يركز على الخصوصية ويدعم الاستخدام دون اتصال بالكامل بالإضافة إلى مزامنة بيانات مشفّرة من طرف إلى طرف.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/ArvinLovegood/go-stock/raw/master/build/appicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/ArvinLovegood/go-stock/blob/master/README.md">go-stock</a> </td>
        <td>go-stock عارض بيانات الأسهم الصينية مبني بـ Wails مع NativeUI ومدعوم بنماذج اللغة الكبيرة.</td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/102771702?s=200&v=4" alt="Wordware" width="64" height="auto" /> </td>
        <td> <a href="docs/wordware/README.md">Wordware</a> </td>
        <td><a href="https://www.wordware.ai/">Wordware</a> مجموعة أدوات تمكن أي شخص من بناء وتكرار ونشر مجموعة أدوات الذكاء الاصطناعي باستخدام اللغة الطبيعية فقط.</td>
    </tr>
    <tr>
        <td> <img src="https://framerusercontent.com/images/xRJ6vNo9mUYeVNxt0KITXCXEuSk.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/langgenius/dify/">Dify</a> </td>
        <td> <a href="https://dify.ai/">Dify</a> منصة تطوير تطبيقات LLM تدعم نماذج DeepSeek لإنشاء المساعدين وسير العمل ومولدات النصوص والمزيد. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/enricoros/big-AGI/refs/heads/v2-dev/public/favicon.ico" alt="Big-AGI" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/enricoros/big-AGI/blob/v2-dev/README.md">Big-AGI</a> </td>
        <td><a href="https://big-agi.com/">Big-AGI</a> هي مجموعة ذكاء اصطناعي رائدة مصممة لتسهيل الوصول إلى الذكاء الاصطناعي المتقدم للجميع.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/LiberSonora/LiberSonora/blob/main/assets/avatar.jpeg?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/LiberSonora/LiberSonora/blob/main/README_en.md">LiberSonora</a> </td>
        <td> LiberSonora، التي تعني "صوت الحرية"، هي مجموعة أدوات كتب صوتية قوية مفتوحة المصدر مدعومة بالذكاء الاصطناعي تتضمن ميزات مثل استخراج الترجمات الذكي، توليد عناوين بالذكاء الاصطناعي، الترجمة متعددة اللغات، مع دعم تسريع GPU ومعالجة دفعية دون اتصال.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/ripperhe/Bob/master/docs/_media/icon_128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://bobtranslate.com/">Bob</a></td>
        <td> <a href="https://bobtranslate.com/">Bob</a> أداة ترجمة وOCR لنظام macOS جاهزة للاستخدام في أي تطبيق — مباشرة!</td>
    </tr>
    <tr>
        <td> <img src="https://agenticflow.ai/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://agenticflow.ai/">AgenticFlow</a> </td>
        <td> <a href="https://agenticflow.ai/">AgenticFlow</a> منصة بدون كود حيث يبني المسوقون سير عمل ذكاء اصطناعي وكيل لأتمتة الانطلاق للسوق، مدعومة بمئات التطبيقات اليومية كأدوات لوكلاء الذكاء الاصطناعي.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/ZGGSONG/STranslate/raw/main/img/favicon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://stranslate.zggsong.com/en/">STranslate</a></td>
        <td> <a href="https://stranslate.zggsong.com/en/">STranslate</a>（Windows） أداة ترجمة OCR جاهزة مطورة بـ WPF </td>
    </tr>
    <tr>
        <td> <img src="https://devinci.onicai.com/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://devinci.onicai.com/">DeVinci</a></td>
        <td> <a href="https://devinci.onicai.com/">DeVinci</a> تطبيق دردشة ذكاء اصطناعي لامركزي شامل للدردشة الخاصة مع نماذج LLM مفتوحة المصدر.</td>
    </tr>
     <tr>
        <td> <img src="https://github.com/user-attachments/assets/5e16beb0-993e-47bf-807e-7c8804b313a2" alt="Asp Client" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Anwar-alhitar/Deepseek.Asp.Client/blob/master/README.md">ASP Client</a> </td>
        <td><a href="https://github.com/Anwar-alhitar/Deepseek.Asp.Client/blob/master/README.md">Deepseek.ASPClient</a> غلاف ASP.NET خفيف لواجهة Deepseek AI، مصمم لتبسيط معالجة النصوص المدفوعة بالذكاء الاصطناعي في تطبيقات .NET.. </td>
    </tr>
    <tr>
        <td> <img src="https://www.gptaiflow.tech/logo.png" alt="gpt-ai-flow-logo" width="64" height="auto" /> </td>
        <td> <a href="https://www.gptaiflow.tech/docs/product/api-keys-setup#setup-deepseek-api-keys">GPT AI Flow</a></td>
        <td>
            السلاح الإنتاجي النهائي المبني من المهندسين لعشاق الكفاءة (أنفسهم): <a href="https://www.gptaiflow.tech/">GPT AI Flow</a>
            <ul>
                <li>`Shift+Alt+Space` تنشيط مركز الذكاء المكتبي</li>
                <li>تخزين محلي مشفر</li>
                <li>محرك تعليمات مخصص</li>
                <li>استدعاء عند الطلب بدون ربط اشتراك</li>
            </ul>
        </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/b09f17a8-936d-4dac-8b24-1682d52c9a3c" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/alecm20/story-flicks">Story-Flicks</a></td>
        <td>بجملة واحدة فقط، يمكنك بسرعة إنشاء مقاطع فيديو قصيرة عالية الدقة للقصص، مع دعم نماذج مثل DeepSeek.</td>
    </tr>
    <tr>
        <td> <img src="https://prompt.16x.engineer/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/16x_prompt/README.md">16x Prompt</a> </td>
        <td> <a href="https://prompt.16x.engineer/">16x Prompt</a> أداة برمجة ذكاء اصطناعي مع إدارة السياق. تساعد المطورين على إدارة سياق الكود المصدري وصياغة التعليمات للمهام البرمجية المعقدة على قواعد الكود الحالية.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/Alpha派/assets/favicon1.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/Alpha派/README.md"> Alpha Pai </a> </td>
        <td> مساعد بحث ذكاء اصطناعي / بوابة المعلومات المالية من الجيل القادم مدفوعة بالذكاء الاصطناعي.<br>وكيل للمستثمرين لحضور الاجتماعات وتدوين الملاحظات، بالإضافة إلى توفير خدمات البحث والأسئلة والأجوبة للمعلومات المالية والتحليل الكمي لأبحاث الاستثمار.</td>
    </tr>
        <td> <img src="https://docs.xark-argo.com/img/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.xark-argo.com">argo</a> </td>
        <td>قم بتنزيل وتشغيل نماذج Ollama وHuggingface محلياً مع RAG على Mac/Windows/Linux. يدعم أيضاً واجهة برمجة تطبيقات LLM.</td>
    </tr>
    <tr>
        <td> <img src="https://www.petercat.ai/images/favicon.ico" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.petercat.ai">PeterCat</a> </td>
        <td> نظام تكوين وكيل أسئلة وأجوبة تفاعلي، حلول نشر ذاتية الاستضافة، ومجموعة تطوير تطبيقات شاملة وسهلة الاستخدام، تتيح لك إنشاء روبوتات أسئلة وأجوبة ذكية لمستودعات GitHub الخاصة بك.</td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/labring/FastGPT/refs/heads/main/.github/imgs/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://fastgpt.cn/en">FastGPT</a> </td>
        <td>
            FastGPT منصة قاعدة معرفة ذكاء اصطناعي مفتوحة المصدر مبنية على نماذج اللغة الكبيرة (LLMs)، تدعم نماذج متنوعة بما في ذلك DeepSeek وOpenAI. نوفر قدرات جاهزة للاستخدام لمعالجة البيانات، استدعاء النماذج، استرجاع RAG، وتنسيق سير عمل الذكاء الاصطناعي المرئي، مما يمكنك من بناء تطبيقات ذكاء اصطناعي متطورة بسهولة.
        </td>
   </tr>
   <tr>
        <td> <img src="./docs/ruzhiai_note/assets/play_store_512.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/ruzhiai_note/README.md">RuZhi AI Notes</a> </td>
        <td>RuZhi AI Notes أداة إدارة معرفة ذكية مدعومة بالذكاء الاصطناعي، توفر خدمات إدارة وتطبيق معرفة شاملة تشمل البحث والاستكشاف بالذكاء الاصطناعي، تحويل نتائج الذكاء الاصطناعي إلى ملاحظات، إدارة وتنظيم الملاحظات، عرض ومشاركة المعرفة. متكاملة مع نموذج DeepSeek لتوفير مخرجات أكثر استقراراً وجودة أعلى.</td>
    </tr>
    <tr>
        <td> <img src="https://cdn.link-ai.tech/doc/CoW%20logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/zhayujie/chatgpt-on-wechat">Chatgpt-on-Wechat</a> </td>
        <td> Chatgpt-on-Wechat(CoW) إطار عمل روبوت دردشة مرن يدعم التكامل السلس لنماذج LLM متعددة، بما في ذلك DeepSeek وOpenAI وClaude وQwen وغيرها، في منصات أو برمجيات مكتبية شائعة الاستخدام مثل حسابات WeChat الرسمية وWeCom وFeishu وDingTalk والمواقع. كما يدعم مجموعة واسعة من الإضافات المخصصة. </td>
    </tr>
    <tr>
        <td> <img src="https://athenalab.ai/assets/favicon/favicon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://athenalab.ai/">Athena</a> </td>
        <td>أول ذكاء اصطناعي عام مستقل في العالم مع هندسة معرفية متقدمة وقدرات استدلال شبيهة بالبشر، مصمم لمواجهة التحديات الحقيقية المعقدة.</td>
    </tr>
    <tr>
        <td> <img src="https://maxkb.cn/images/favicon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/1Panel-dev/MaxKB">MaxKB</a> </td>
        <td> <a href="https://maxkb.cn/">MaxKB</a> روبوت دردشة RAG مرن وجاهز للاستخدام. </td>
    </tr>
    <tr>
        <td> <img src="./docs/TigerGPT/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://ttm.financial/gpt">TigerGPT</a> </td>
        <td>TigerGPT هو أول مساعد استثماري ذكاء اصطناعي مالي من نوعه مبني على OpenAI، طوره مجموعة Tiger. يهدف TigerGPT إلى توفير دعم اتخاذ قرارات استثمارية ذكي للمستثمرين. في 18 فبراير 2025، دمج TigerGPT رسمياً نموذج DeepSeek-R1 لتوفير خدمات أسئلة وأجوبة عبر الإنترنت تدعم الاستدلال العميق للمستخدمين. </td>
    </tr>
    <tr>
        <td> <img src="./docs/HIX.AI/assets/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://hix.ai">HIX.AI</a> </td>
        <td>جرب DeepSeek مجاناً واستمتع بدردشة ذكاء اصطناعي غير محدودة على HIX.AI. استخدم DeepSeek R1 للدردشة بالذكاء الاصطناعي، الكتابة، البرمجة والمزيد. اختبر دردشة الذكاء الاصطناعي من الجيل القادم الآن!</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/sharmt1411/askanywhere/blob/main/icon/Depth_8,_Frame_0explore-%E8%A7%92%E6%A0%87.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/sharmt1411/askanywhere">Askanywhere</a> </td>
        <td>حدد النص في أي مكان وابدأ محادثة مع Deepseek</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/OJZen/1chat/raw/refs/heads/main/doc/assets/icon.ico?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/OJZen/1chat">1chat</a> </td>
        <td>تطبيق iOS يتيح لك الدردشة مع نموذج DeepSeek-R1 محلياً.</td>
    </tr>
    <tr>
        <td> <img src="https://chatlabsai.com/assets/logo/logo.png" alt="iOS AI Chatbot" width="64" height="auto" /> </td>
        <td> <a href="https://chatlabsai.com">Access 250+ text, image LLMs in one app</a> </td>
        <td> 1AI iOS Chatbot يتكامل مع أكثر من 250 نموذج نص وصورة وصوت يتيح للمستخدمين الدردشة مع أي نموذج في العالم بما في ذلك نماذج Deepseek R1 وDeepseek V3.</td>
    </tr>
    <tr>
        <td> <img src="./docs/PopAi/assets/logo.svg" alt="PopAi" width="64" height="auto" /> </td>
        <td> <a href="https://popai.pro">PopAi</a> </td>
        <td>PopAi تطلق DeepSeek R1! استمتع بأداء سريع البرق وبدون تأخير مع PopAi. قم بالتبديل بسلاسة بين البحث عبر الإنترنت تشغيل/إيقاف.</td>
    </tr>
    <tr>
        <td> <img src="https://pot-app.com/logo/icon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://pot-app.com/">Pot</a></td>
        <td> <a href="https://pot-app.com/">Pot</a> 🌈 برنامج متعدد المنصات لترجمة النصوص والتعرف عليها. </td>
    </tr>
    <tr>
        <td><img src="https://github.com/Byaidu/PDFMathTranslate/raw/main/docs/images/banner.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/Byaidu/PDFMathTranslate">PDFMathTranslate</a></td>
        <td>PDF Math Translate أداة ترجمة ثنائية اللغة شاملة مبنية على الذكاء الاصطناعي تحافظ على تخطيط مستندات PDF بالكامل.</td>
    </tr>
    <tr>
        <td><img src="https://github.com/Richasy/Bili.Copilot/raw/master/assets/StoreLogo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/Richasy/Bili.Copilot">Bili.Copilot</a></td>
        <td>Bilibili عميل سطح مكتب Windows من طرف ثالث، تطبيق أصلي مبني بـ Windows App SDK.</td>
    </tr>
    <tr>
        <td><img src="https://www.tensorbounce.com/logo.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://www.tensorbounce.com/">LawAgent</a></td>
        <td>LawAgent منتج ذكاء اصطناعي قانوني طوره فريق Tensorbounce، يدمج قاعدة معرفة مع قدرات AI Agent. يتميز بمستودع ضخم من عشرات الملايين من نقاط البيانات الرسمية المتعلقة بالقانون كما يتيح تكوينات قاعدة معرفة مخصصة. الوضع المهني يستفيد من قدرات الاستدلال لـ DeepSeek-R1 لمساعدة المستخدمين في التحليل القانوني، مراجعة العقود، توليد المستندات، ترجمة الملفات، وسيناريوهات قانونية أخرى.</td>
    </tr>
    <tr>
        <td width=80> <img src="docs/AlphaBot/assets/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://alphabot.x-pai.com/">AlphaBot</a> </td>
        <td> AlphaBot مساعد تحليل أسهم ذكي يدمج بيانات متعددة المصادر مع تقنية تحليل الذكاء الاصطناعي لتوفير التحليل الفني والتنبؤات وتقييم المخاطر، مساعداً المستثمرين على اتخاذ قرارات تداول مبنية على البيانات. يدعم نشر بنقرة واحدة، عمليات سهلة، يدعم منصات Windows/Linux/MacOS وغيرها</td>
     <tr>
        <td><img src="https://h1.appinn.me/file/1741929316827_21.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://github.com/jiqi136/DS-AI">Multi-platform connected DeepSeek</a></td>
        <td>يستفيد من محرك الذكاء الاصطناعي ثلاثي القنوات المدعوم من DeepSeek الرسمي وسحابة علي بابا وبركان دويين، حيث يتطور ذكاؤه باستمرار. بالإضافة إلى ذلك، يستخدم وضعاً هجيناً يجمع بين "البحث عبر الإنترنت + التفكير العميق".</td>
    </tr>
    <tr>
    <td><img src="docs/remio/assets/remio_icon.png" alt="Icon" width="64" height="auto" /></td>
    <td><a href="https://www.remio.ai/">remio</a></td>
    <td>remio مركز معرفة شخصي مدعوم بالذكاء الاصطناعي يبني قواعد معرفة شخصية من خلال التقاط تلقائي لمحتوى الويب المتصفح، تحليل الملفات المحلية، ودمج الملاحظات الشخصية. يمكن البحث والأسئلة والأجوبة بالللغة الطبيعية داخل قاعدة معرفتك الشخصية للحصول على رؤى فورية مع توفير مساعدة كتابة ذكية—تتكيف مع أسلوبك لتبسيط الصياغة والتحسين وإكمال المحتوى بسهولة. مصمم مع تخزين محلي أولاً، remio يعطي الأولوية لخصوصية البيانات مع تمركز المعلومات المجزأة لتحقيق أقصى إنتاجية.</td>
    </tr> 
    <tr>
    <td><img src="docs/DocKit/assets/dockit.png" alt="Icon" width="64" height="auto" /></td>
    <td><a href="https://dockit.geekfun.club/">DocKit</a></td>
    <td>DocKit عميل GUI سطح مكتب مدعوم بالذكاء الاصطناعي مصمم لقاعدة بيانات NoSQL، يدعم Elasticsearch وOpenSearch عبر Mac وWindows وLinux. من خلال التكامل مع نماذج كبيرة مثل DeepSeek، يمكن لـ DocKit مساعدة المطورين على كتابة استعلامات DSL معقدة، وتوفير تجربة أفضل لإدارة البيانات والتحليل. </td>
    </tr> 
    <tr>
        <td> <img src="docs/zenfeed/assets/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/glidea/zenfeed">zenfeed</a> </td>
        <td> تمكين RSS بالذكاء الاصطناعي، تصفية تلقائية وتلخيص ودفع المعلومات المهمة للتغلب على حمولة المعلومات الزائدة. </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="data">أطر تطبيقات بيانات الذكاء الاصطناعي</span>

<table>
    <tr>
        <td width="80"> <img src="https://github.com/user-attachments/assets/a327d72f-755f-4256-8a37-32a518a55df3" alt="Icon" width="64" height="auto" /> </td>
        <td width="120"> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/dbgpt/README.md"> DB-GPT </a> </td>
        <td> 🤖 DB-GPT إطار عمل تطوير تطبيقات بيانات ذكاء اصطناعي أصلي مفتوح المصدر مع AWEL(لغة تعبير سير العمل الوكيل) ووكلاء.
الهدف هو بناء بنية تحتية في مجال النماذج الكبيرة، من خلال تطوير قدرات تقنية متعددة مثل إدارة متعددة النماذج (SMMF)، تحسين تأثير Text2SQL، إطار عمل RAG والتحسين، تعاون إطار عمل متعدد الوكلاء، AWEL (تنسيق سير عمل الوكيل)، إلخ. مما يجعل تطبيقات النماذج الكبيرة مع البيانات أبسط وأكثر ملاءمة.

 </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="rag">أطر RAG</span>

<table>
    <tr>
        <td width="80"> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/33142505/77093e84-9f7c-4716-9168-bac962fa1372" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/ragflow/README.md"> RAGFlow </a> </td>
        <td> محرك RAG (توليد معزز بالاسترجاع) مفتوح المصدر مبني على الفهم العميق للمستندات. يوفر سير عمل RAG مبسط للشركات من أي حجم، يجمع بين نماذج اللغة الكبيرة (LLM) لتوفير قدرات إجابة على الأسئلة موثوقة، مدعومة باقتباسات راسخة من بيانات معقدة التنسيق متنوعة. </td>
    </tr>
    <tr>
        <td width="80"> <img src="https://raw.githubusercontent.com/pingcap/tidb.ai/main/frontend/app/public/nextra/icon-dark.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/autoflow/README.md"> Autoflow </a> </td>
        <td> <a href="https://github.com/pingcap/autoflow">AutoFlow</a> أداة قاعدة معرفة مفتوحة المصدر مبنية على GraphRAG (توليد معزز بالاسترجاع المبني على الرسم البياني)، مبنية على <a href="https://www.pingcap.com/ai?utm_source=tidb.ai&utm_medium=community">TiDB</a> Vector وLlamaIndex وDSPy. توفر واجهة بحث شبيهة بـ Perplexity وتتيح تكامل سهل لنافذة البحث المحادثي لـ AutoFlow في موقعك من خلال تضمين مقطع JavaScript بسيط. </td>
    </tr>
    <tr>
        <td width="80"> <img src="https://assets.zilliz.com/Zilliz_Logo_Mark_White_20230223_041013_86057436cc.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/zilliztech/deep-searcher"> DeepSearcher </a> </td>
        <td> DeepSearcher يجمع بين نماذج LLM قوية (DeepSeek، OpenAI، إلخ) وقواعد بيانات متجهة (Milvus، إلخ) لأداء بحث وتقييم واستدلال مبني على بيانات خاصة، موفراً إجابات عالية الدقة وتقارير شاملة.  </td>
    </tr>
    <tr>
        <td width="80"> <img src="https://raw.githubusercontent.com/OpenSPG/openspg/089188f3e7b0392221f5a8e8f1a3629b6352a6f9/LOGO.png" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://github.com/OpenSPG/KAG/blob/master/README.md"> KAG </a> </td>
        <td> KAG إطار عمل استدلال منطقي وأسئلة وأجوبة مبني على محرك <a href="https://github.com/OpenSPG/openspg">OpenSPG</a> ونماذج اللغة الكبيرة، يُستخدم لبناء حلول استدلال منطقي وأسئلة وأجوبة لقواعد معرفة نطاق عمودي. KAG يمكنه التغلب بفعالية على غموض حساب التشابه المتجه التقليدي لـ RAG ومشكلة الضوضاء في GraphRAG المقدمة من OpenIE. KAG يدعم الاستدلال المنطقي وأسئلة وأجوبة الحقائق متعددة القفزات، إلخ.</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="fhe">أطر التشفير الكامل المتجانس (FHE)</span>

<table>
    <tr>
        <td> <img src="./docs/fhe.mind-network/mind-network-log.png" alt="Icon" width="200" height="auto" /> </td>
        <td> <a href="https://github.com/mind-network/mind-sdk-deepseek-rust"> Mind FHE Rust SDK </a> </td>
        <td> <p>مجموعة تطوير برمجيات مفتوحة المصدر لتشفير الذكاء الاصطناعي باستخدام التشفير المتجانس الكامل (FHE) والتكامل مع شبكة Mind للتوافق بين الوكلاء. يعتبر FHE <b>الكأس المقدسة للتشفير</b>، حيث يمكن من إجراء العمليات الحسابية مباشرة على البيانات المشفرة دون الحاجة لفك التشفير. مع FHE، يمكن للوكلاء حماية خصوصيتهم أثناء استخدام Deepseek، مع ضمان سلامة النموذج وتوافق النتائج - <b>كل ذلك دون كشف بياناتهم</b> - من خلال الاتصال بشبكة Mind. تم تنفيذ <a href="https://github.com/mind-network/mind-sdk-deepseek-rust">الشفرة المصدرية</a> لمجموعة التطوير بلغة <b>Rust</b> النقية والحزمة متوفرة أيضاً على <a href="https://crates.io/crates/mind_sdk_deepseek">crates.io</a>.</p> </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="solana">أطر Solana</span>

<table>
    <tr>
        <td> <img src="./docs/solana-agent-kit/assets/sendai-logo.png" alt="Icon" width="128" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/solana-agent-kit/README.md"> Solana Agent Kit </a> </td>
        <td>An open-source toolkit for connecting AI agents to Solana protocols. Now, any agent, using any Deepseek LLM, can autonomously perform 60+ Solana actions: </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="sythetic">تنسيق البيانات الاصطناعية</span>

<table>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/bespokelabsai/curator/main/docs/Bespoke-Labs-Logomark-Red-crop.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/curator/README.md"> Curator </a> </td>
        <td> An open-source tool to curate large scale datasets for post-training LLMs. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/8455694b-c52e-40ec-847e-adf6a5ac064f" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Kiln-AI/Kiln"> Kiln </a> </td>
        <td>Generate synthetic datasets and distill R1 models into custom fine-tunes. </td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/192579850?s=200&v=4" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/DataEval/dingo"> Dingo </a> </td>
        <td>Dingo: A Comprehensive Data Quality Evaluation Tool. </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="im">ملحقات تطبيقات المراسلة الفورية</span>

<table>
    <tr>
        <td> <img src="https://github.com/InternLM/HuixiangDou/releases/download/v0.1.0rc1/huixiangdou.jpg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/huixiangdou/README_cn.md">HuixiangDou<br/>(wechat,lark)</a> </td>
        <td>مساعد خبرة نطاق شخصي داخل ويتشات وفيشو خاص بك، متخصص في الإجابة على الأسئلة.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/RockChinQ/LangBot/blob/master/res/logo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/RockChinQ/LangBot">LangBot<br/>（QQ, Lark, WeCom）</a> </td>
        <td>إطار عمل بوتات IM قائم على LLM، يدعم منصات متعددة بما في ذلك QQ وLark وWeCom.</td>
    </tr>
    <tr>
        <td> <img src="https://nonebot.dev/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/KomoriDev/nonebot-plugin-deepseek">NoneBot<br/>（QQ, Lark, Discord, TG, etc.）</a> </td>
        <td>مبني على إطار عمل NoneBot، يوفر وظائف الدردشة الذكية والتفكير العميق، يدعم منصات متعددة بما في ذلك QQ وLark وDiscord وTG.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/Soulter/AstrBot/raw/refs/heads/master/dashboard/src/assets/images/logo-normal.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Soulter/AstrBot/">AstrBot<br/>（QQ, WeChat, WeCom, Lark, TG, etc.）</a> </td>
        <td>بوت دردشة متعدد المنصات يدعم الذكاء الاصطناعي وواجهة مستخدم سهلة الاستخدام، يدعم الذاكرة الطويلة المدى وRAG ووحدات LLM وتكامل الإضافات.</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="office">إضافات أوفيس</span>

<table>
    <tr>
        <td> <img src="https://www.44886.com/view/img/bukeng.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.bukenghezi.com/">BKOffice</a> </td>
        <td>إضافة أوفيس تدعم مجموعة Word وExcel وPPT (تدعم أيضاً مجموعة WPS)، تضيف أكثر من 300 وظيفة إلى أوفيس.</td>
    </tr>
      <tr>
        <td> <img src="https://www.aippt.cn/_nuxt/logo_cn.eYEokZzA.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.aippt.cn/">AiPPT</a> </td>
        <td>AiPPT.com، اختيار أكثر من 20 مليون مستخدم، جملة واحدة، دقيقة واحدة، نقرة واحدة لإنشاء PPT.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/office-sec/OfficeAI/blob/main/logo/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/office-sec/OfficeAI">OfficeAI Assistant</a> </td>
        <td>OfficeAI Assistant إضافة أوفيس مجانية توفر وظائف مثل سؤال وجواب الذكاء الاصطناعي، تدقيق الذكاء الاصطناعي، تنسيق الذكاء الاصطناعي، إنشاء الذكاء الاصطناعي، ومعالجة البيانات الذكاء الاصطناعي داخل أوفيس. يمكنها تحسين كفاءة أوفيس وهي متوافقة مع كل من Microsoft Office وWPS Office.</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="browser">ملحقات المتصفح</span>

<table>
    <tr>
        <td><img src="./docs/deepshare/assets/logo_200.png" alt="Icon" width="64" height="auto" /></td>
        <td><a href="./docs/deepshare/README.md">Tiny AI Bee</a></td>
        <td>Tiny AI Bee إضافة متصفح مجانية وغير مسجلة بضغطة واحدة لمشاركة محادثات الذكاء الاصطناعي،
            تخصصت في حل مشكلة إرسال آلاف الكلمات من سؤال وجواب الذكاء الاصطناعي إلى أصدقائك، مما يؤدي إلى تمرير هواتفهم أو إنشاء لقطات شاشة طويلة وفتحها مضبوطة، غير سهلة القراءة.
            تلبي احتياجات المستخدمين لمشاركة حكمتهم المبررة مع الذكاء الاصطناعي مع غيرهم
        </td>
    </tr>
    <tr>
        <td><img src="docs/OpenXLab/migo/logo.svg" alt="Icon" width="64" height="auto" /></td>
        <td><a href="https://chromewebstore.google.com/detail/cjapgnecnkblehipjghhegiccobeloka?utm_source=item-share-cb">Migo</a></td>
        <td>Migo توفر وظائف معالجة النصوص الشاملة والبحث عن المعلومات وسؤال وجواب المعرفة، مناسبة لمختلف سيناريوهات العمل والبحث عبر الإنترنت (مثل Feishu وarXiv وOverleaf وغيرها).</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/9d3f42b8-fcd0-47ab-8b06-1dd0554dd80e" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/immersive_translate/README.md"> Immersive Translate </a> </td>
        <td> Immersive Translate إضافة متصفح لترجمة الصفحات الويب ثنائية اللغة. </td>
    </tr>
    <tr>
        <td> <img src="https://lh3.googleusercontent.com/K9i0qJb8phasC5wWf5tU68rhnfvX4swsE0hrhJP-WB3WV7MwE5KpMUIJvHKNHHRE6GKNIvIdTNSWoDMl_NggrmUsaw=s120" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/immersive_reading_guide/README.md"> Immersive Reading Guide </a> </td>
        <td> لا شريط جانبي!!! تلخيص ذكي للصفحات الويب بالذكاء الاصطناعي، طرح الأسئلة... </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/8a301619-a3de-489b-81fd-69aaa7c1c561" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/chatgpt_box/README.md"> ChatGPT Box </a> </td>
        <td> ChatGPT Box هو تكامل ChatGPT في المتصفح، مجاني بالكامل. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/c3d9d100-247a-41cc-97c1-10b01ed25e70" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/hcfy/README.md"> hcfy (划词翻译) </a> </td>
        <td> hcfy (划词翻译) إضافة متصفح لتكامل خدمات الترجمة المتعددة. </td>
    </tr>
    <tr>
        <td> <img src="https://static.eudic.net/web/trans/en_trans.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/Lulu Translate/README.md"> Lulu Translate </a> </td>
        <td> الإضافة توفر وظائف الترجمة عن طريق تحديد الفأرة، والترجمة بالفقرة، وترجمة المستندات PDF. يمكنها استخدام محركات الترجمة المختلفة مثل DeepSeek AI وBing وGPT وGoogle وغيرها.</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/Bistutu/FluentRead/raw/refs/heads/main/public/icon/192.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://fluent.thinkstu.com/"> FluentRead </a> </td>
        <td>إضافة متصفح مفتوحة المصدر ثورية للترجمة تمكن الجميع من الحصول على تجربة قراءة شبيهة بالأصلية</td>
    </tr>
    <tr>
        <td> <img src="https://www.ncurator.com/_next/image?url=%2Ffavicon.ico&w=96&q=75" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.ncurator.com/"> Ncurator </a> </td>
        <td>مساعد قاعدة معرفة ذكاء اصطناعي للأسئلة والأجوبة - دع الذكاء الاصطناعي يساعدك في تنظيم وتحليل المعرفة</td>
    </tr>
    <tr>
        <td> <img src="https://github.com/oinzen/RSSFlow-doc/blob/main/docs/images/en/icon64.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://rssflow.oinchain.com"> RssFlow </a> </td>
        <td>إضافة متصفح ذكية لقارئ RSS مع دعم تلخيص RSS مدعوم بالذكاء الاصطناعي وعروض تغذية متعددة الأبعاد. يدعم تكوين نموذج DeepSeek لفهم محتوى محسّن. </td>
    </tr>
    <tr>
        <td> <img src="./docs/refinereader/assets/refinereader-128.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://refinereader.cuihuaer.com"> Refine Reader </a> </td>
        <td>إضافة Chrome تستخدم الذكاء الاصطناعي (DeepSeek، OpenAI، إلخ) لمساعدتك على فهم وتلخيص المقالات بسرعة. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/Hedwi/deepchat/refs/heads/main/images/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://chromewebstore.google.com/detail/deepchat-power-of-deepsee/femhcibnncinlabdboehojdhfcihpkpl?hl=en"> DeepChat </a> </td>
        <td>إضافة Chrome تتيح للمستخدمين الدردشة مع DeepSeek من خلال فتح شريط جانبي على أي موقع. بالإضافة لذلك، توفر قائمة عائمة تحت أي نص محدد على أي موقع تتيح للمستخدمين توليد ملخصات نصية، فحص مشاكل القواعد النحوية، وترجمة المحتوى.</td>
    </tr>
     <tr>
        <td> <img src="https://www.typral.com/_next/image?url=%2Ffavicon.ico&w=96&q=75" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.typral.com/"> Typral </a> </td>
        <td>مساعد كاتب ذكاء اصطناعي سريع - دع الذكاء الاصطناعي يساعدك على تحسين المقال والورقة والنص بسرعة...</td>
    </tr>
    <tr>
        <td> <img src="https://static.trancy.org/assets/trancy_logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.trancy.org/"> Trancy </a> </td>
        <td>ترجمة ثنائية اللغة غامرة، ترجمات فيديو ثنائية اللغة، امتداد ترجمة اختيار جملة/كلمة</td>
    </tr>
    <tr>
        <td> <img src="https://ziziyi.com/svg/anything_copilot.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/baotlake/anything-copilot"> Anything Copilot </a> </td>
        <td>Anything Copilot إضافة متصفح تمكن من الوصول السلس لأدوات الذكاء الاصطناعي الرئيسية مباشرة من الشريط الجانبي. </td>
    </tr>
    <tr>
        <td> <img src="https://cliprun.com/apple-touch-icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://cliprun.com/"> Cliprun </a> </td>
        <td>منصة تشغيل كود Python وملعب. انقر بزر الماوس الأيمن على كود Python في DeepSeek لتشغيله فوراً في متصفحك. </td>
    </tr>
    <tr>
        <td> <img src="http://cdn.docky.ai/assets/logo.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/docky-ai/README.md"> Docky AI </a> </td>
        <td>Docky AI إضافة متصفح قوية تتيح لك إجراء محادثات في الوقت الفعلي مع نماذج ذكاء اصطناعي متعددة من خلال شريط جانبي. يدعم التواصل المتزامن مع نماذج متعددة ويمكنه مساعدتك في قراءة صفحات الويب والكتابة والترجمة وإنشاء الصور</td>
    </tr>
</table>


<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="vscode">امتدادات VS Code</span>

<table>
    <tr>
        <td> <img src="https://github.com/continuedev/continue/blob/main/docs/static/img/logo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/continue/README.md"> Continue </a> </td>
        <td> Continue طيار آلي مفتوح المصدر في IDE. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/cline/assets/favicon.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/cline/README.md"> Cline </a> </td>
        <td> التقي بـ Cline، مساعد ذكاء اصطناعي يمكنه استخدام CLI والمحرر الخاص بك. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/Sitoi/ai-commit/refs/heads/main/images/logo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Sitoi/ai-commit/blob/main/README.md"> AI Commit </a> </td>
        <td> استخدم الذكاء الاصطناعي لتوليد رسائل git commit في VS Code. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/titusTong/seekCodeCopilot/blob/main/assets/SeekCodeCopilotLogo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/titusTong/seekCodeCopilot/blob/main/README.md"> SeekCode Copilot </a> </td>
        <td> مساعد برمجة ذكي لـ vscode يدعم تكوين نماذج DeepSeek المنشورة محلياً </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/intellism/vscode-comment-translate/blob/master/doc/image/icon.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/intellism/vscode-comment-translate/blob/master/README.md"> Comment Translation </a> </td>
        <td> هذا الامتداد يساعد المطورين على ترجمة التعليقات والنصوص وتلميحات الكود ورسائل الخطأ وأسماء المتغيرات في كودهم. </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="vs">امتدادات Visual Studio</span>

<table>
    <tr>
        <td> <img src="https://merryyellow.gallerycdn.vsassets.io/extensions/merryyellow/comment2gpt/2.0.5/1739475434185/Microsoft.VisualStudio.Services.Icons.Default" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://marketplace.visualstudio.com/items?itemName=MerryYellow.Comment2GPT"> Comment2GPT </a> </td>
        <td> استخدم OpenAI ChatGPT وGoogle Gemini وAnthropic Claude وDeepSeek وOllama من خلال تعليقاتك </td>
    </tr>
    <tr>
        <td> <img src="https://merryyellow.gallerycdn.vsassets.io/extensions/merryyellow/codelens2gpt/2.0.5/1739475875714/Microsoft.VisualStudio.Services.Icons.Default" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://marketplace.visualstudio.com/items?itemName=MerryYellow.CodeLens2GPT"> CodeLens2GPT </a> </td>
        <td> استخدم OpenAI ChatGPT وGoogle Gemini وAnthropic Claude وDeepSeek وOllama من خلال CodeLens </td>
    </tr>
    <tr>
        <td> <img src="https://merryyellow.gallerycdn.vsassets.io/extensions/merryyellow/uca-lite/1.4.2/1739392928984/Microsoft.VisualStudio.Services.Icons.Default" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://marketplace.visualstudio.com/items?itemName=MerryYellow.UCA-Lite"> Unity Code Assist Lite </a> </td>
        <td> مساعدة كود لسكريبت Unity </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="neovim">امتدادات neovim</span>

<table>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/c316f70a-0a3c-4a32-b148-4df15e609acc" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/avante.nvim/README.md"> avante.nvim </a> </td>
        <td> avante.nvim طيار آلي مفتوح المصدر في IDE. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/d66dfc62-8e69-4b00-8549-d0158e48e2e0" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/llm.nvim/README.md"> llm.nvim </a> </td>
        <td> إضافة نموذج لغة كبيرة مجانية (LLM) تتيح لك التفاعل مع LLM في Neovim. تدعم أي LLM، مثل Deepseek وGPT وGLM وKimi أو نماذج LLM محلية (مثل ollama). </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/d66dfc62-8e69-4b00-8549-d0158e48e2e0" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/codecompanion.nvim/README.md"> codecompanion.nvim </a> </td>
        <td> برمجة مدعومة بالذكاء الاصطناعي، بسلاسة في Neovim. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/user-attachments/assets/d66dfc62-8e69-4b00-8549-d0158e48e2e0" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/minuet-ai.nvim/README.md"> minuet-ai.nvim </a> </td>
        <td> Minuet يوفر إكمال كود أثناء الكتابة من نماذج LLM شائعة بما في ذلك Deepseek وOpenAI وGemini وClaude وOllama وCodestral والمزيد. </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="jetbrains">امتدادات JetBrains</span>

<table>
    <tr>
        <td> <img src="https://plugins.jetbrains.com/files/21520/412905/icon/pluginIcon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://ide.unitmesh.cc/quick-start"> AutoDev </a> </td>
        <td>‍AutoDev مساعد برمجة ذكاء اصطناعي مفتوح المصدر في IDE لـ JetBrain. </td>
    </tr>
    <tr>
        <td> <img src="https://plugins.jetbrains.com/files/21410/561595/icon/pluginIcon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://plugins.jetbrains.com/plugin/21410-onegai-copilot"> Onegai Copilot </a> </td>
        <td>Onegai Copilot مساعد برمجة ذكاء اصطناعي في IDE لـ JetBrain. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/continuedev/continue/blob/main/docs/static/img/logo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/blob/main/docs/continue/README.md"> Continue </a> </td>
        <td> Continue طيار آلي مفتوح المصدر في IDE. </td>
    </tr>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/a18792721831/studyplugin/535b9cab69da0f97b42dcaebb00bb0d4ed15c8a6/translate/src/main/resources/META-INF/pluginIcon.svg" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://plugins.jetbrains.com/plugin/18336-chinese-english-translate">Chinese-English Translate</a> </td>
        <td> Chinese-English Translate خدمات ترجمة متعددة في IDE لـ JetBrain. </td>
    </tr>
    <tr>
        <td> <img src="https://plugins.jetbrains.com/files/24851/659002/icon/pluginIcon.svg" alt="Icon" width="64" height="auto"/> </td>
        <td> <a href="https://plugins.jetbrains.com/plugin/24851-ai-git-commit">AI Git Commit</a> </td>
        <td> هذه الإضافة تستخدم الذكاء الاصطناعي لتوليد رسائل commit تلقائياً بناءً على التغييرات في كودك. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/YiiGuxing/TranslationPlugin/blob/master/pluginIcon.svg?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://intellij-translation.yiiguxing.top/#/en/">IntelliJ Translation Plugin</a> </td>
        <td> إضافة ترجمة لـ IDEs مبنية على IntelliJ تدمج خدمات ترجمة متعددة، بما في ذلك مترجم OpenAI (متوافق مع DeepSeek وDoubao وOllama، إلخ)، تتيح ترجمة مباشرة لنصوص الكود مثل التعليقات والوثائق داخل IDE في أي وقت. </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="discord">بوتات Discord</span>

<table>
    <tr>
        <td> <img src="https://geneplore.com/img/geneplore_color_logo_circular.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/Geneplore AI/README.md"> Geneplore AI </a> </td>
        <td> Geneplore AI يدير واحد من أكبر بوتات Discord للذكاء الاصطناعي، الآن مع Deepseek v3 وR1. </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="codeeditor">محررات كود الذكاء الاصطناعي الأصلية</span>

<table>
    <tr>
        <td> <img src="https://global.discourse-cdn.com/flex020/uploads/cursor1/original/2X/a/a4f78589d63edd61a2843306f8e11bad9590f0ca.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://www.cursor.com/"> Cursor </a> </td>
        <td>‍محرر كود ذكاء اصطناعي مبني على VS Code</td>
    </tr>
    <tr>
        <td> <img src="https://exafunction.github.io/public/images/windsurf/windsurf-app-icon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://codeium.com/windsurf"> WindSurf </a> </td>
        <td>محرر كود ذكاء اصطناعي آخر مبني على VS Code من Codeium</td>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="emacs">Emacs</span>

<table>
    <tr>
        <td> <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/EmacsIcon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/karthink/gptel"> gptel </a> </td>
        <td>عميل LLM بسيط لـ Emacs</td>
    </tr>
    <tr>
        <td> <img src="https://upload.wikimedia.org/wikipedia/commons/0/08/EmacsIcon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/milanglacier/minuet-ai.el"> Minuet AI </a> </td>
        <td>ارقص مع الذكاء في كودك 💃</td>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="security">الأمان</span>

<table>
    <tr>
        <td> <img src="https://github.com/lukehinds/awesome-deepseek-integration/blob/codegate/docs/codegate/assets/codegate.png"  alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/stacklok/codegate/"> CodeGate </a> </td>
        <td> CodeGate: توليد كود ذكاء اصطناعي آمن</td>
    </tr>
    <tr>
        <td> <img src="./docs/tencent/hunyuan.png"  alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/tencent/AI-Infra-Guard"> AI-Infra-Guard </a> </td>
        <td> فريق أمان Hunyuan لشركة Tencent - أداة تقييم أمان البنية التحتية للذكاء الاصطناعي مصممة لاكتشاف والكشف عن المخاطر الأمنية المحتملة في أنظمة الذكاء الاصطناعي.</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="providers">المزودون</span>

<table>
    <tr>
        <td> <img src="./docs/aimlapi/aimlapi_logo.png"  alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://docs.aimlapi.com/api-references/text-models-llm?utm_source=awesome-deepseek-integrations&utm_medium=github&utm_campaign=integration"> AI/ML API </a> </td>
        <td> توفر AI/ML API للمستخدمين وصولاً على مستوى المؤسسات إلى أكثر من 200 نموذج باستخدام واجهة برمجة تطبيقات واحدة. يتضمن ذلك Deepseek R1 وV3، إلى جانب النماذج المغلقة ومفتوحة المصدر. كل ذلك مع وقت تشغيل 99٪ ودعم بشري على مدار الساعة طوال أيام الأسبوع.</td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

###  <span id="others">أخرى</span>

<table>
    <tr>
        <td> <img src="https://raw.githubusercontent.com/mlflow/mlflow/refs/heads/master/assets/icon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://mlflow.org/docs/latest/tracing/integrations/deepseek"> MLflow </a></td>
        <td> منصة MLOps / LLMOps مفتوحة المصدر لبناء واختبار ونشر ومراقبة تطبيقات الذكاء الاصطناعي مع DeepSeek. </td>
    </tr>
    <tr>
        <td style="font-size: 64px">🤖</td>
        <td> <a href="https://github.com/wangrongding/wechat-bot/blob/main/README.md"> Wechat-Bot </a> </td>
        <td> روبوت WeChat مبني على WeChaty مع دمج DeepSeek وخدمات الذكاء الاصطناعي الأخرى. </td>
    </tr>
    <tr>
        <td style="font-size: 64px">&#128032;</td>
        <td> <a href="https://github.com/lunary-ai/abso/blob/main/README.md"> Abso </a> </td>
        <td> مجموعة أدوات TypeScript للتفاعل مع أي مزود LLM باستخدام تنسيق OpenAI. </td>
    </tr>
    <tr>
        <td> <img src="https://i.imgur.com/IsQYInJ.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/djcopley/ShellOracle/"> ShellOracle </a> </td>
        <td> أداة طرفية لتوليد أوامر shell ذكية. </td>
    </tr>
    <tr>
        <td> <img src="https://avatars.githubusercontent.com/u/178783630?s=200&v=4" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/bolna-ai/bolna/"> Bolna </a> </td>
        <td> استخدم DeepSeek كنموذج LLM لوكلاء الذكاء الاصطناعي الصوتي التفاعلي </td>
    </tr>
    <tr>
        <td> <img src="https://pics.fatwang2.com/56912e614b35093426c515860f9f2234.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/fatwang2/siri-ultra"> Siri Ultra </a> </td>
        <td> مشروع GitHub مع 1000 نجمة، يدعم الاتصال بالإنترنت والمحادثات متعددة الدورات ونماذج سلسلة DeepSeek </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/deepseek-ai/awesome-deepseek-integration/assets/59196087/c1e47b01-1766-4f7e-bfe6-ab3cb3991c30" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/deepseek-ai/awesome-deepseek-integration/tree/main/docs/siri_deepseek_shortcut"> siri_deepseek_shortcut </a> </td>
        <td> Siri مجهزة بواجهة برمجة تطبيقات DeepSeek </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/n8n-io/n8n/blob/master/assets/n8n-logo.png?raw=true" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/rubickecho/n8n-deepseek"> n8n-nodes-deepseek </a> </td>
        <td> عقدة مجتمع N8N تدعم التكامل المباشر مع واجهة برمجة تطبيقات DeepSeek في سير العمل. </td>
    </tr>
    <tr>
        <td> <img src="https://framerusercontent.com/images/TSKshn2UFdTyvUi85EDMIXrXgs.png?scale-down-to=512" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Portkey-AI/gateway"> Portkey AI </a> </td>
        <td> Portkey هي واجهة برمجة تطبيقات موحدة للتفاعل مع أكثر من 1600 نموذج LLM، وتقدم أدوات متقدمة للتحكم والرؤية والأمان في تطبيقات DeepSeek الخاصة بك. متوفر SDK لبايثون و Node. </td>
    </tr>
    <tr>
        <td> <img src="https://framerusercontent.com/images/8rF2JOaZ8l9AvM4H6ezliw44aI.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/BerriAI/litellm"> LiteLLM </a> </td>
        <td> SDK بايثون، خادم وسيط (بوابة LLM) لاستدعاء أكثر من 100 واجهة برمجة تطبيقات LLM بتنسيق OpenAI. يدعم DeepSeek AI مع تتبع التكلفة أيضاً. </td>
    </tr>
    <tr>
        <td> <img src="https://i.postimg.cc/k5Z4YWjt/Screenshot-2025-01-23-at-6-08-01-PM.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/mem0ai/mem0"> Mem0 </a> </td>
        <td> يعزز Mem0 مساعدي الذكاء الاصطناعي بطبقة ذاكرة ذكية، مما يتيح التفاعلات الشخصية والتعلم المستمر بمرور الوقت. </td>
    </tr>
    <tr>
        <td> <img src="https://simplismart-public-assets.s3.ap-south-1.amazonaws.com/logos/Logo+Icon+Light.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://simplismart.ai/"> Simplismart AI </a> </td>
        <td> يمكّن Simplismart من نشر GenAI بسلاسة مع أسرع استدلال لنماذج LLM والانتشار والكلام. انشر Deepseek بسهولة على سحابة Simplismart أو مع السحابة الخاصة بك. </td>
    </tr>
    <tr>
        <td> <img src="https://www.promptfoo.dev/img/logo-panda.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="docs/promptfoo/README.md"> promptfoo </a> </td>
        <td> اختبر وقيّم موجهات LLM، بما في ذلك نماذج DeepSeek. قارن بين مزودي LLM المختلفين، واكتشف التراجعات، وقيّم الاستجابات. </td>
    </tr>
    <tr>
        <td>  </td>
        <td> <a href="https://github.com/AndersonBY/deepseek-tokenizer"> deepseek-tokenizer </a> </td>
        <td> مكتبة ترميز فعالة وخفيفة الوزن لنماذج DeepSeek، تعتمد فقط على مكتبة `tokenizers` دون تبعيات ثقيلة مثل `transformers`. </td>
    </tr>
    <tr>
        <td> <img src="https://langfuse.com/icon.svg" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://langfuse.com/docs/integrations/deepseek"> Langfuse </a> </td>
        <td> منصة مراقبة LLM مفتوحة المصدر تساعد الفرق على تصحيح الأخطاء وتحليل وتحسين تطبيقات DeepSeek الخاصة بهم بشكل تعاوني. </td>
    </tr>
    <tr>
        <td> CR </td>
        <td> <a href="https://github.com/hustcer/deepseek-review"> deepseek-review </a> </td>
        <td> 🚀 حسّن كودك، انشر بثقة - ارتقِ بسير عملك مع مراجعة كود Deepseek 🚀 </td>
    </tr>
    <tr>
        <td> <img src="http://gptlocalhost.com/wp-content/uploads/2025/01/icon_1024.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://youtu.be/T1my2gqi-7Q"> GPTLocalost </a> </td>
        <td> استخدم DeepSeek-R1 في Microsoft Word محلياً. بدون تكاليف استدلال. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/suqicloud/wp-ai-chat/raw/main/ic_logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/suqicloud/wp-ai-chat"> WordPress ai助手 </a> </td>
        <td> ربط واجهة برمجة تطبيقات Deepseek لموقع WordPress مع مساعد محادثة الذكاء الاصطناعي، وإنشاء المنشورات، وملخص المنشورات. </td>
    </tr>
    <tr>
        <td> <img src="docs/ComfyUI-Copilot/assets/logo 2.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/AIDC-AI/ComfyUI-Copilot"> ComfyUI-Copilot </a> </td>
        <td> مساعد ذكي مبني على إطار عمل Comfy-UI يبسط ويعزز عملية تصحيح أخطاء خوارزمية الذكاء الاصطناعي ونشرها من خلال التفاعلات باللغة الطبيعية. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/Optima-CityU/llm4ad/blob/main/assets/figs/logo_short.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/Optima-CityU/llm4ad">LLM4AD</a> </td>
        <td> LLM4AD هي منصة موحدة مفتوحة المصدر تعتمد على Python تستخدم نماذج اللغة الكبيرة (LLMs) للتصميم التلقائي للخوارزميات (AD). </td>
    </tr>
    <tr>
        <td>  </td>
        <td> <a href="https://github.com/JiauZhang/chatchat"> chatchat </a> </td>
        <td> واجهة برمجة تطبيقات بايثون لنماذج اللغة الكبيرة. </td>
    </tr>
    <tr>
        <td> <img src="https://serpapi.com/android-chrome-512x512.png" alt="Icon" height="auto" />   </td>
        <td> <a href="https://serpapi.com/blog/connect-deepseek-api-with-the-internet-google-search-and-more/#connect-deepseek-with-google-search-result"> SerpApi </a> </td>
        <td> ربط واجهة برمجة تطبيقات DeepSeek مع نتائج البحث مثل Google. </td>
    </tr>
    <tr>
        <td> <img src="https://github.com/yincongcyincong/telegram-deepseek-bot/blob/main/static/logo.png" alt="Icon" width="64" height="auto" /> </td>
        <td> <a href="https://github.com/yincongcyincong/telegram-deepseek-bot">telegram-deepseek-bot</a> </td>
        <td> telegram-deepseek-bot هو روبوت Telegram مدمج مع قدرات DeepSeek AI. </td>
    </tr>
    <tr>
        <td>  </td>
        <td> <a href="https://github.com/eqld/nlsh">nlsh</a> </td>
        <td> nlsh هي أداة سطر أوامر مدعومة بالذكاء الاصطناعي لتوليد أوامر shell مدركة للسياق مع دعم LLM متعدد الخلفيات. يدعم بناء جملة خاص بـ shell، وأدوات نظام للقراءة فقط، ونقاط نهاية استدلال مخصصة. </td>
    </tr>
</table>

<p style="text-align: right;"><a href="#table-of-contents">^ Back to Contents ^</a></p>

### تاريخ النجوم

[![Star History Chart](https://api.star-history.com/svg?repos=deepseek-ai/awesome-deepseek-integration&type=Date)](https://star-history.com/#deepseek-ai/awesome-deepseek-integration&Date)
