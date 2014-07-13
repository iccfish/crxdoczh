{{+bindTo:partials.standard_devtools_article}}

# <!--@Sample Debugging Protocol Clients-->调试协议客户端示例

<!--@There are a number third-party clients for the Chrome debugging protocol. This section presents a sample.-->
有一些 Chrome 调试协议的第三方客户端，这一部分展示了这些示例。

## Brackets

<!--@Brackets is a web-based IDE that uses the Chrome debugging protocol to enable 
debugging and live HTML/CSS development.<br/>-->
Brackets 是一个基于网页的 IDE，使用 Chrome 调试协议进行
调试和实时 HTML/CSS 开发。<br/>
<img src="debugging-clients-files/brackets.png" width="632px" alt=""/> 

<!--@More information:-->更多信息：

* <!--@[Official site](http://brackets.io/).-->[官方网站](http://brackets.io/)。
* <!--@This [blog post from Mark 
  DuBois](http://www.markdubois.info/weblog/2013/03/adobe-brackets-revisited/) 
  gives an overview of working in Brackets.-->
[Mark DuBois 的这篇博文](http://www.markdubois.info/weblog/2013/03/adobe-brackets-revisited/)
提供了使用 Brackets 的概述。
* <!--@Download from-->从 [download.brackets.io](http://download.brackets.io/)<!--@.--> 下载。
* <!--@Source code available on-->源代码可以在 [GitHub](https://github.com/adobe/brackets)<!--@.--> 上获取。

## Light Table

<!--@Light Table is a new IDE that takes a novel approach to arranging the 
developer's workspace. Light Table is currently in alpha. It's not open source, 
but the alpha version is available for free at this time.-->
Light Table 是一种新的 IDE，采用全新的方式布置开发者的工作空间。
Light Table 目前处于 Alpha 测试中，它不是开源的，但是目前 Alpha 版本可以免费获取。

<img src="debugging-clients-files/lighttable.png" width="551px" alt=""/> 

<!--@More information:-->更多信息：

* <!--@Read the [blog post](http://www.chris-granger.com/2013/04/28/light-table-040/) 
  describing new features in 0.4.0, including DevTools integration.-->
阅读这篇[博文](http://www.chris-granger.com/2013/04/28/light-table-040/)，
描述 0.4.0 中的新特性，包括开发者工具集成。
* <!--@Download from the [official site.](http://www.lighttable.com/)-->
从[官方网站](http://www.lighttable.com/)下载。

## NodeJS

<!--@A number of modules have been developed to make use of the Chrome debugger from 
Node scripts. -->
有人开发了一些模块，以便在 Node 脚本中利用 Chrome 调试器。

### chrome-remote-interface

<!--@The `chrome-remote-interface` module wraps the debugger protocol with a Node-style 
JavaScript API.-->
`chrome-remote-interface` 模块将调试器协议包装在 Node 风格的 JavaScript API 中。

<img src="debugging-clients-files/chrome-remote.png" alt=""/> 

<!--@More information:-->更多信息：<br/>

*   <!--@Install using `npm`:-->
使用 `npm` 安装：

        npm install -g chrome-remote-interface

*   <!--@Source code available on -->源代码可以在 
    [GitHub](https://github.com/cyrus-and/chrome-remote-interface) 上获取。

### crconsole

<!--@The `crconsole` module provides a command-line interface to the Chrome console. It 
uses the `chrome-remote-interface` module to communicate with the Chrome debugger 
protocol.-->
`crconsole` 提供了 Chrome 控制台的命令行接口，
它使用 `chrome-remote-interface` 模块与 Chrome 调试器协议通信。

<!--@More information:-->更多信息：

*   <!--@Install using `npm`:-->
使用 `npm` 安装：
  
        npm install -g crconsole

*   <!--@Source code available on-->源代码可以在 [GitHub](https://github.com/sidorares/crconsole)<!--@.--> 上获取。

## Sublime Text

<!--@The Sublime Web Inspector project adds Chrome debugger integration to the 
popular Sublime Text editor. You can install it from the Sublime Text package 
manager.-->
Sublime Web Inspector 项目将 Chrome 调试器与流行的 Sublime 文本编辑器集成
在一起，您可以在 Sublime Text 包管理器中安装它。

<img src="debugging-clients-files/sublime.png" alt=""/> 

<!--@More information:-->更多信息：

* <!--@See the [official page](http://sokolovstas.github.io/SublimeWebInspector/) for 
  an overview and installation instructions.-->
有关概述和安装指南请参见[官方网页](http://sokolovstas.github.io/SublimeWebInspector/)。
* <!--@Source code available on -->源代码可以在
  [GitHub](https://github.com/sokolovstas/SublimeWebInspector)<!--@.--> 上获取。

## Telemetry

<!--@Telemetry is a performance testing framework used by the Chromium project to 
test multiple versions of the Chrome browser. It uses the debugging protocol to 
remotely control instances of Chrome.-->
Telemetry 是 Chromium 项目中使用的性能测试框架，用于测试
多个版本的 Chrome 浏览器。它使用调试协议远程控制 Chrome 浏览器实例。

<!--@More information:-->更多信息：

* <!--@[Introduction to Telemetry on 
  Chromium.org.](http://www.chromium.org/developers/telemetry)-->
[chromium.org 上的 Telemetry 简介](http://www.chromium.org/developers/telemetry)。

## Vim

<!--@Chrome.vim is an experimental plugin for the Vim editor that provides some basic 
Chrome operations as Vim commands.-->
Chrome.vim 是一个实验性的 Vim 编辑器插件，以 Vim 命令的形式提供一些
基本的 Chrome 浏览器操作。

<!--@More information:-->更多信息：

* [https://github.com/mklabs/vimfiles/tree/master/custom-bundle/vim-chrome](https://github.com/mklabs/vimfiles/tree/master/custom-bundle/vim-chrome) 

## WebDriver

<!--@The Selenium browser automation tools use WebDriver API to abstract interactions 
with different browsers. The WebDriver implementation for Chrome uses the Chrome 
debugging protocol.-->
Selenium 浏览器自动化工具使用 WebDriver API 抽象描述与不同浏览器之间的交互。
用于 Chrome 浏览器的 WebDriver 实现使用 Chrome 远程调试协议。

<!--@More information:-->更多信息：

* <!--@[Selenium WebDriver project.](http://docs.seleniumhq.org/projects/webdriver/) -->
[Selenium WebDriver 项目](http://docs.seleniumhq.org/projects/webdriver/)。

<!--@If you know of more, please let us know using the Feedback tool at the top right 
of this page!-->
<!--# ??? -->

## WebStorm

<!--@WebStorm is a commercial IDE that supports debugging and live-editing in Chrome. 
WebStorm uses a [Chrome extension 
](http://www.jetbrains.com/webstorm/webhelp/using-jetbrains-chrome-extension.html)to 
integrate with the Chrome debugger.-->
WebStorm 是一个商用 IDE，支持在 Chrome 浏览器中调试和实时编辑。
WebStorm 使用 [Chrome 扩展程序](http://www.jetbrains.com/webstorm/webhelp/using-jetbrains-chrome-extension.html)
与 Chrome 调试器交互。

<img src="debugging-clients-files/webstorm.png" alt=""/> 

<!--@More information:-->更多信息：

* <!--@Download from-->从 [JetBrains](http://www.jetbrains.com/webstorm/)<!--@.--> 下载。
* <!--@[Screencast describing the latest debugging 
  features.](http://tv.jetbrains.net/videocontent/improved-javascript-debugger-in-webstorm-7)-->
[描述最新调试特性的屏幕录像](http://tv.jetbrains.net/videocontent/improved-javascript-debugger-in-webstorm-7)。

{{/partials.standard_devtools_article}}
