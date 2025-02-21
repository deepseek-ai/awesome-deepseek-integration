<h1 align="center">
    translate.js
</h1>
<h4 align="center">
    它是面向前端开发者使用的 AI i18n，两行js实现html全自动翻译。 <br/>
    交给AI，无需改动页面、无语言配置文件、无API Key、对SEO友好！
</h4> 

![image](assets/html_demo.gif)  


# 使用方式
### 1. 部署文本翻译API
首先部署文本翻译开放接口，它支持一次性批量翻译多个文本，同时内置多层缓存体系，最大化降低AI翻译的耗时。以使用户在使用时做到瞬间翻译无延迟的能力。  

##### 1.1 服务器规格
1核1G、20G系统盘、1MB带宽，操作系统为CentOS 7.4 （7.0~7.9都可）即可完美运行。

##### 1.2 安装
````
wget https://gitee.com/mail_osc/translate/raw/master/deploy/install_translate.service.sh -O install.sh && chmod -R 777 install.sh && sh ./install.sh
````

##### 1.3 配置 DeepSeek 参数

编辑 application.properties ，编辑命令：
````
vi /mnt/tomcat8/webapps/ROOT/WEB-INF/classes/application.properties
````
然后再最后面追加几行配置：  
````
# 大模型接口请求URL, 比如下面的是华为DeepSeek的请求URL的，另外像是GiteeAI的请求URL是 https://ai.gitee.com/v1/chat/completions 其他的平台的可自行获取填入
translate.service.deepSeek.url=https://infer-modelarts-cn-southwest-2.modelarts-infer.com/v1/infers/fd53915b-8935-48fe-be70-449d76c0fc87/v1/chat/completions
# 访问令牌
translate.service.deepSeek.key=QM8jrVl98lTluLhzCaO4i9PFv-caRk6U7kDL-H6CIyApytMG69jO33aasO1GnduQak8fGI7dtpmbsM98Qh3ywA
# 使用哪个模型，这里默认使用 DeepSeek-V3 即可，无需更改
translate.service.deepSeek.model=DeepSeek-V3
# AI单次的最大token数量,不设置默认是3000，这里可以默认用这个即可
translate.service.deepSeek.max_tokens=3000
````
最终的效果如下图所示：  
![image](assets/application_properties_demo.png)

##### 1.4 重启服务
````
pkill java
sudo /mnt/tomcat8/bin/startup.sh
````

##### 1.5 文本翻译API测试一下
![image](assets/texts_translate_api_demo.png)  
这里传入的 from 代表翻以前的语种语言，如果你知道是什么语言则填上，如果不知道不好判断，那就固定上图这样填写即可，DeepSeek会自动识别并进行翻译。
有关此翻译API接口的详细说明可参考： [http://api.zvo.cn/translate/service/20230807/translate.json.html](http://api.zvo.cn/translate/service/20230807/translate.json.html)



### 2. html中使用 translate.js 

**普通网站中点击某个语言进行切换**  
如下图所示，网站中的某个位置要有几种语言切换  
![](assets/site_demo.png)  
直接在其html代码末尾的位置加入以下代码：  

````
<!-- 增加某种语言切换的按钮。注意 ul上加了一个 class="ignore" 代表这块代码不会被翻译到 -->
<ul class="ignore">
	<li><a href="javascript:translate.changeLanguage('english');">English</a></li>|
	<li><a href="javascript:translate.changeLanguage('chinese_simplified');">简体中文</a></li>|
	<li><a href="javascript:translate.changeLanguage('chinese_traditional');">繁體中文</a></li>
</ul>

<!-- 引入多语言切换的js -->
<script src="https://res.zvo.cn/translate/translate.js"></script>
<script>
	//不出现默认的select的选择语言
	translate.selectLanguageTag.show = false; 
	//设置文本翻译API的主机，也就是我们上面第一步部署好的文本翻译API，有关此更多可参考 https://translate.zvo.cn/4068.html
	translate.request.api.host='http://121.36.23.238/'; 
	//翻译触发初始化
	translate.execute();
</script>
````

这只是一个最普通的场景使用，另外像是各框架了比如VUE、React、等等，各种管理后台，只要能运行js，都能使用它！

# 开源仓库
https://github.com/xnx3/translate  
交流QQ群： 240567964

# 它的能力

### 特性说明
* **使用极其简单。** 直接加入几行 JavaScript 代码即可让其拥有上百种语言切换能力。
* **不增加工作量。** 无需改造页面本身植入大量垃圾代码变得臃肿，也不需要配置各种语种的语言文件，因为它会直接扫描你的DOM自动识别并翻译显示，它不需要你到某某网站登录去申请什么key，它是开源开放的，拿来就能用。
* **极其灵活扩展。** 您可指定它[只翻译某些指定区域的元素](http://translate.zvo.cn/4063.html)、[自定义切换语言方式及美化](http://translate.zvo.cn/4056.html)、[某些id、class、tag不被翻译](https://translate.zvo.cn/4061.html)、[自定义翻译术语](https://translate.zvo.cn/4070.html) ...... 只要你想的，它都能做到。做不到的，你找我我来让它做到！
* **自动切换语种。** [自动根据用户的语言喜好及所在的国家切换到这个语种进行浏览](http://translate.zvo.cn/4065.html)
* **极速翻译能力。** [内置三层缓存、预加载机制，毫秒级瞬间翻译的能力。它并不是你理解的大模型蜗牛似的逐个字往外出的那样](http://translate.zvo.cn/4026.html)
* [**永久开源免费。** 采用Apache-2.0开源协议，您可永久免费使用](https://github.com/xnx3/translate/blob/master/LICENSE)。[另外你可以用它来做某些系统的三方插件直接售卖盈利](http://translate.zvo.cn/4036.html)、或者你是建站公司用它来做为一项高级功能盈利，我们都是完全认可并支持的，并不需要给我们任何费用！
* **搜索引擎友好。** 完全不影响你本身网站搜索引擎的收录。爬虫所爬取的网页源代码，它不会对其进行任何改动，你可完全放心。[另外我们还有高级版本让你翻译之后的页面也能被搜索引擎收录](http://translate.zvo.cn/236896.html)
* **支持私有部署。** [在某些政府机关及大集团内部项目中，对数据隐私及安全保密有强要求场景、或者完全不通外网的场景，可以自行私有部署翻译API服务](http://translate.zvo.cn/4052.html) 
* **全球网络节点**。美洲、亚洲、欧洲 ... 都有网络节点，它能自动适配最快节点，每间隔1分钟自动获取一次延迟最小的节点进行接入使用，使全球范围使用都可高效稳定。
* **HTML整体翻译**。[提供开放API接口，传入html文件（html源代码）及要翻译为的语言即可拿到翻译后的html源码。完美支持识别各种复杂及不规范html代码，
支持翻译前的微调，比如不翻译某个区域、图片翻译、js语法操作html文件中的元素进行增删改等。](https://translate.zvo.cn/4022.html)
* **源站翻译及域名分发**。[将您现有的网站，翻译成全新的小语种网站，小语种网站可以分别绑定域名并支持搜索引擎收录和排名。而您的源站无需任何改动。也就是你可以将你朋友的网站，翻译为小语种网站，绑定上自己的域名，提供对外访问。而你无需向你朋友取得任何的如账号等相关权限](https://translate.zvo.cn/236896.html)
* **浏览器翻译插件**。[提供整体的浏览器翻译插件的全套方案，您如果是开发者，完全可以拿去将界面美化包装一下，而后直接提交应用市场进行售卖盈利](https://translate.zvo.cn/4037.html)


### 微调指令
* **[设置默认翻译为的语种](http://translate.zvo.cn/4071.html)**，用户第一次打开时，默认以什么语种显示。
* **[自定义翻译术语](http://translate.zvo.cn/41555.html)**，如果你感觉某些翻译不太符合你的预期，可进行针对性的定义某些词或句子的翻译结果，进行自定义术语库
* **[翻译完后自动触发执行](http://translate.zvo.cn/4069.html)**，当翻译完成后会自动触发执行您的某个方法，以便您来做自定义扩展。
* **[指定翻译服务接口](http://translate.zvo.cn/4068.html)**，如果你不想用我们开源免费的翻译服务接口，使用您自己私有部署的、或者您自己二次开发对接的某个翻译服务，可通过此来指定自己的翻译接口。
* **[监控页面动态渲染的文本进行自动翻译](http://translate.zvo.cn/4067.html)**，如果页面用 JavaScript 的地方比较多，内容都是随时用JS来控制显示的，比如 VUE、React 等框架做的应用，它可以实时监控DOM中文字的变动，当发生变动后立即识别并进行翻译。
* **[设置本地语种（当前网页的语种）](http://translate.zvo.cn/4066.html)**，手动指定当前页面的语言。如果不设置，它会自动识别当前网页的文本，取当前网页文本中，出现频率最高的语种为默认语种。
* **[自动切换为用户所使用的语种](http://translate.zvo.cn/4065.html)**，用户第一次打开网页时，自动判断当前用户所使用的语种、以及所在的国家，来自动进行切换为这个语种。
* **[主动进行语言切换](http://translate.zvo.cn/4064.html)**，开放一个方法提供程序调用，只需传入翻译的目标语言，即可快速切换到指定语种
* **[只翻译指定的元素](http://translate.zvo.cn/4063.html)**，指定要翻译的元素的集合,可传入一个或多个元素。如果不设置此，默认翻译整个网页。
* **[翻译时忽略指定的id](http://translate.zvo.cn/4062.html)**，翻译时追加上自己想忽略不进行翻译的id的值，凡是在这里面的，都不进行翻译，也就是当前元素以及其子元素都不会被翻译。
* **[翻译时忽略指定的class属性](http://translate.zvo.cn/4061.html)**，翻译时追加上自己想忽略不进行翻译的class标签，凡是在这里面的，都不进行翻译，也就是当前元素以及其子元素都不会被翻译。
* **[翻译时忽略指定的tag标签](http://translate.zvo.cn/4060.html)**，翻译时追加上自己想忽略不进行翻译的tag标签，凡是在这里面的，都不进行翻译，也就是当前元素以及其子元素都不会被翻译。
* **[翻译时忽略指定的文字不翻译](http://translate.zvo.cn/283381.html)**，翻译时追加上自己想忽略不进行翻译的文字，凡是在这里面的，都不进行翻译。
* **[对网页中图片进行翻译](http://translate.zvo.cn/4055.html)**，在进行翻译时，对其中的图片也会一起进行翻译。
* **[鼠标划词翻译](http://translate.zvo.cn/4072.html)**，鼠标在网页中选中一段文字，会自动出现对应翻译后的文本
* **[获取当前显示的是什么语种](http://translate.zvo.cn/4074.html)**，如果用户切换为英语进行浏览，那么这个方法将返回翻译的目标语种。
* **[根据URL传参控制以何种语种显示](http://translate.zvo.cn/41929.html)**，设置可以根据当前访问url的某个get参数来控制使用哪种语言显示。
* **[离线翻译及自动生成配置](http://translate.zvo.cn/4076.html)**，其实它也就是传统 i18n 的能力，有语言配置文件提供翻译结果。
* **[手动调用接口进行翻译操作](http://translate.zvo.cn/4077.html)**，通过JavaScript调用一个方法，传入翻译文本进行翻译，并获得翻译结果
* **[元素的内容整体翻译能力配置](http://translate.zvo.cn/4078.html)**，对node节点的文本拿来进行整体翻译处理，而不再拆分具体语种，提高翻译语句阅读通顺程度
* **[翻译接口响应捕获处理](http://translate.zvo.cn/4079.html)**，对翻译API接口的响应进行捕获，进行一些自定义扩展
* **[清除历史翻译语种的缓存](http://translate.zvo.cn/4080.html)**，清除掉你上个页面所记忆的翻译语种，从而达到切换页面时不会按照上个页面翻译语种自动进行翻译的目的。
* **[网页ajax请求触发自动翻译](http://translate.zvo.cn/4086.html)**，监听当前网页中所有的ajax请求，当请求结束后，自动触发翻译
* **[设置只对指定语种进行翻译](http://translate.zvo.cn/4085.html)**，翻译时只会翻译在这里设置的语种，未在里面的语种将不会被翻译。
* **[识别字符串语种及分析](http://translate.zvo.cn/43128.html)**，对字符串进行分析，识别出都有哪些语种，每个语种的字符是什么、每个语种包含的字符数是多少
* **[重写一级缓存（浏览器缓存）](http://translate.zvo.cn/4082.html)**，你如果不想使用默认的 localStorage 的缓存，您完全可以对其重写，设置自己想使用的缓存方式
* **[设置使用的翻译服务 translate.service.use](http://translate.zvo.cn/4081.html)**，目前有自有的服务器提供翻译API方式、无自己服务器API的方式两种。
* **[启用企业级稳定翻译](http://translate.zvo.cn/4087.html)**，独立于开源版本的翻译通道之外，仅对少数用户开放，提供企业级的稳定、高速、以及更多网络分发节点。
* **[增加对指定标签的属性进行翻译](http://translate.zvo.cn/231504.html)**，可以增加对指定html标签的某个或某些属性进行翻译。比如element、vue 等框架，有些自定义的标签属性，想让其也正常翻译
* **[本地语种也进行强制翻译](http://translate.zvo.cn/289574.html)**，切换为中文时，即使本地语种设置的是中文，网页中只要不是中文的元素，都会被翻译为要显示的语种
* **[自定义通过翻译API进行时的监听事件](http://translate.zvo.cn/379207.html)**，当通过翻译API进行文本翻译时的整个过程进行监听，做一些自定义处理，比如翻译API请求前要做些什么、请求翻译API完成并在DOM渲染完毕后触发些什么。


