{{+bindTo:partials.standard_devtools_article}}

# <!--@Integrating with DevTools-->与开发者工具集成

<!--@The Chrome DevTools are built to be extensible. So if the DevTools are missing a 
feature you need, you may be able to find an existing extension, or write one 
yourself. Or you can integrate DevTools capabilities into your application.-->
Chrome 开发者工具建立时考虑到了可扩展性，所以如果开发者工具没有提供
您需要的某个特性，您也许能找到现有的扩展程序，或者自己写一个。
您还可以将开发者工具的功能集成到您的应用程序中。

<!--@There are two basic ways to build a custom solution using the DevTools:-->
使用开发者工具建立自定义解决方案的基本方式有两种：

* **<!--@DevTools Extension-->开发者工具扩展程序**<!--@. A [Chrome 
  extension](http://developer.chrome.com/extensions/) that plugs into the 
  DevTools to add functionality and extend its UI.-->
。嵌入开发者工具的 [Chrome 扩展程序](/extensions/)。
* **<!--@Debugging Protocol Client-->调试协议客户端**<!--@. A third-party application that uses the Chrome [ 
  remote debugging protocol](debugger-protocol.html) to 
  plug into the low-level debugging support in Chrome.-->
。使用 Chrome 浏览器[远程调试协议](debugger-protocol.html)的第三方
应用程序，嵌入 Chrome 浏览器中的低级调试支持。

<!--@The following sections discuss both approaches.-->
下面的部分讨论了这两种方式。

## <!--@DevTools Chrome extensions-->Chrome 开发者工具扩展程序

<!--@The DevTools UI is a web application embedded inside Chrome. 
DevTools extensions use the [Chrome extensions 
system](http://developer.chrome.com/extensions/) to add features to the 
DevTools. A DevTools extension can add new panels to the DevTools, add new 
panes to the Elements and Sources panel sidebar, examine the resources and 
network events, as well as evaluate JavaScript expressions in the browser tab 
that's being inspected.-->
开发者工具的用户界面是一个嵌入在 Chrome 浏览器中的网页应用程序，
开发者工具扩展程序通过 [Chrome 扩展程序系统](/extensions/)向开发者工具
添加功能。开发者工具扩展程序可以向开发者工具添加新面板、在 Elements
（元素）和 Sources（源代码）面板的侧边栏中添加窗格、审查资源和网络事件，
还可以在审查的浏览器标签页中运行 JavaScript 表达式。

<!--@If you want to develop a DevTools extension:-->
如果您想开发开发者工具扩展程序：

* <!--@If you haven't developed a Chrome extension before, see [Overview of Chrome 
  Extensions](http://developer.chrome.com/extensions/overview.html).-->
如果您以前没有开发过 Chrome 扩展程序，
请参见 [Chrome 扩展程序概述](/extensions/overview)。
* <!--@See [Extending DevTools](http://developer.chrome.com/extensions/devtools.html) 
  for the specifics of creating a Chrome DevTools extension.-->
有关创建 Chrome 开发者工具扩展程序的具体内容请参见
[扩展开发者工具](/extensions/devtools)。

<!--@For a list of sample DevTools extensions, see <a href="sample-extensions.md">Sample 
DevTools Extensions</a>. These samples include many open source extensions that 
can be used for reference.-->
有关开发者工具扩展程序的示例，请参见[开发者工具扩展程序示例](sample-extensions)。这些示例包含了很多开源的扩展程序，可以用来参考。

## <!--@Debugging protocol clients-->调试协议客户端

<!--@Third-party applications, such as IDEs, editors, continuous integration 
harnesses, and test frameworks can integrate with the Chrome debugger in order 
to debug code, live-preview code and CSS changes, and control the browser. 
Clients use the [Chrome debugging 
protocol](debugger-protocol.html) to interact with an 
instance of Chrome, which can be running on the same system or remotely. -->
第三方应用程序，例如 IDE、编辑器、持续集成套件还有测试框架可以
与 Chrome 调试器集成，以便调试代码、实时预览代码和 CSS 更改，还能控制浏览器。
客户端使用 [Chrome 调试协议](debugger-protocol)与 Chrome 浏览器实例交互，
Chrome 浏览器可以在同样的计算机上或远程运行。

<!--@Note: Currently, the Chrome debugging protocol supports only _one_ client per 
page. So you can use the DevTools to inspect a page, or use a third-party 
client, but not both at the same time.-->
注意：目前 Chrome 调试协议一个网页只支持
_一个_
客户端，所以您可以使用
开发者工具审查网页，也可以使用第三方客户端，但是不同同时使用。

<!--@There are two ways to integrate with the debugging protocol:-->
与调试协议集成的方式有两种：

* <!--@Applications that run in Chrome (such as web-based IDEs) can create a Chrome 
  extension using the debugger module, 
  [chrome.debugger](http://developer.chrome.com/extensions/debugger.html). This 
  module lets the extension interact with the debugger directly, bypassing the 
  DevTools UI. See [Using the debugger extension 
  API](debugger-protocol.html#extension) for more 
  information.-->
Chrome 浏览器中运行的应用程序（例如基于网页的 IDE）可以使用
调试器模块 [chrome.debugger](/extensions/debugger) 创建 Chrome 扩展程序。
该模块允许扩展程序跳过开发者工具用户界面，直接与调试器交互，
有关更多信息请参见[使用调试器扩展程序 API](debugger-protocol#extension)。
* <!--@Other applications can use the 
  [wire protocol](debugger-protocol.html#remote) to 
  integrate directly with the debugger. This protocol involves exchanging JSON 
  messages over a WebSocket connection.-->
其他应用程序可以使用[线路协议](debugger-protocol#remote)直接与调试器集成，
这种协议需要通过 WebSocket 连接交换 JSON 消息。

<!--@For some example integrations, see <a href="debugging-clients.md">Sample Debugging 
Protocol Clients</a>.-->
有关一些集成的例子，请参见[调试协议客户端示例](debugging-clients)。

{{/partials.standard_devtools_article}}
