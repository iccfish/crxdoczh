{{+bindTo:partials.standard_devtools_article}}

# <!--@Console API Reference-->控制台 API 参考

<!--@The Console API provides web applications with methods for writing information to the console, creating JavaScript profiles, and initiating a debugging session.-->
控制台 API 为网上应用提供了一些方法，用于在控制台中写入信息、
进行 JavaScript 性能分析，还能开始调试会话。



## console.assert(expression, object) ##

<!--@If the specified expression is `false`, the message is written to the console along with a stack trace. In the following example, the assert message is written to the console only when the `document` contains fewer than five child nodes:-->
如果指定表达式为 `false`，指定消息会写入控制台，并包含堆栈跟踪。在下面的
例子中，只有当 `#myList` 包含的子节点小于十个时断言消息才会写入控制台。

    var list = document.querySelector('#myList');
    console.assert(list.childNodes.length < 10, "列表项目总数 >= 10");

![Example of console.assert()](console-files/assert-failed-list.png)


## console.clear() ##

<!--@Clears the console.-->
清除控制台。

    console.clear();

<!--@Also see [Clearing the console](console.md#clearing-console-history).-->
请参见[清除控制台](console.md#clearing-console-history)。

<!--@However, if Preserve Logs is on, console.clear() will not do anything in case there's some iframe which calls console.clear() and can make your debugging process harder. "Clear console" in the context menu will still work, and actually clear the console.-->
然而，如果启用了保留日志的选项，console.clear() 并不会进行任何操作，以免
某些内嵌框架调用 console.clear()，使您的调试过程更麻烦。右键菜单中的
”Clear console“（清除控制台）仍然可以使用，而且确实会清除控制台。


## console.count(label) ##

<!--@Writes the the number of times that `count()` has been invoked at the same line and with the same label.-->
在一行中显示以相同标签调用 `count()` 的次数以及对应的标签。

<!--@In the following example `count()` is invoked each time the `login()` function is invoked.-->
在下面的例子中每次调用 `login()` 函数时调用 `count()`。

    function login(user) {
        console.count("Login called");
        // login() code...
    }

![Example of using console.count()](console-files/count.png)

<!--@In this example, `count()` is invoked with different labels, each of which is incremented separately.-->
在这个例子中，使用不同的标签调用 `count()`，每一个都会分别计数。

    function login(user) {
        console.count("Login called for user '" +  user + "'");
        // login() code...
    }

![Example of using console.count() with different string](console-files/count-unique.png)


## console.debug(object [, object, ...]) ##

<!--@This method is identical to [`console.log()`](#consolelogobject-object).-->
该方法等价于 [`console.log()`](#consolelogobject-object)。


## console.dir(object) ##

<!--@Prints a JavaScript representation of the specified object. If the object being logged is an HTML element, then the properties of its DOM representation are displayed, as shown below:-->
以 JavaScript 表示形式显示指定对象。如果记录的对象是 HTML 元素，对应
的 DOM 属性会显示出来，如下所示：

    console.dir(document.body);

![Example of using console.dir() with an HTML element()](console-files/consoledir-body.png)

<!--@You can also use the object formatter (`%O`) in a `console.log()` statement to print out an element's JavaScript properties:-->
您还可以在 `console.log()` 语句中使用对象格式化指示符（`%0`）显示元素
的 JavaScript 属性：

    console.log("document body: %O", document.body);

![Using the object formatter on a DOM element](console-files/consolelog-object-formatter.png)

<!--@Calling `console.dir()` on a JavaScript object is equivalent to calling `console.log()` on the same object&mdash;they both print out the object's JavaScript properites in a tree format.-->
在 JavaScript 对象上调用 `console.dir()` 等价于在同一对象上
调用 `console.log()`——它们都以树的形式显示对象的 JavaScript 属性。

<!--@Compare this with the behavior of `console.log()`, which displays the element in an XML format as it would appear in the Elements panel:-->
比较下列语句中 `console.log()` 行为上的区别，它以 XML 格式像元素面板中那样
显示元素：

    console.log(document.body);

![Using console.log() on an element](console-files/consolelog-body.png)


## console.dirxml(object) ##

<!--@Prints an XML representation of the specified object, as it would appear in the Elements panel. For HTML elements, calling this method is equivalent to calling `console.log()`.-->
以 XML 方式显示指定对象，就像元素面板中显示的那样。对于 HTML 元素来说，调用
该方法等价于调用 `console.log()`。

    var list = document.querySelector("#myList");
    console.dirxml();

<!--@%O is a shortcut for dir
%o acts either as dir or dirxml depending on the object type (non-dom or dom)-->
%O 是 dir 的快捷方式，%o 根据对象类型（非 DOM 还是 DOM）以 dir 或 dirxml 方
式显示。


## console.error(object [, object, ...])

<!--@Similar to [`console.log()`](#consolelogobject-object), `console.error()` and also includes a stack trace from where the method was called.-->
与 [`console.log()`](#consolelogobject-object) 类似，此外 `console.error()` 还会包含
调用方法时的堆栈跟踪。

    function connectToServer() {
        var errorCode = 1;
        if (errorCode) {
            console.error("Error: %s (%i)", "Server is  not responding", 500);
        }
    }
    connectToServer();

![Example of console.error()](console-files/error-server-not-resp.png)


## console.group(object[, object, ...]) ##

<!--@Starts a new logging group with an optional title. All console output that occurs after calling this method and calling `console.groupEnd()` appears in the same visual group.-->
开始新的日志分组，可以指定标题。调用该方法之后以及调用 `console.groupEnd()` 前
出现的所有控制台输出都会在同一分组中显示。

    console.group("Authenticating user '%s'", user);
    console.log("User authenticated");
    console.groupEnd();

![Console group example](console-files/log-group-simple.png)

<!--@You can also nest groups:-->
您还可以嵌套分组：

    // New group for authentication:
    console.group("Authenticating user '%s'", user);
    // later...
    console.log("User authenticated", user);
    // A nested group for authorization:
    console.group("Authorizing user '%s'", user);
    console.log("User authorized");
    console.groupEnd();
    console.groupEnd();

![Nested logging group examples](console-files/nestedgroup-api.png)


## console.groupCollapsed(object[, object, ...]) ##

<!--@Creates a new logging group that is initially collapsed instead of open, as with `console.group()`.-->
创建新的日志分组，一开始是折叠的而不是像 `console.group()` 那样是展开的。

    console.groupCollapsed("Authenticating user '%s'", user);
    console.log("User authenticated");
    console.groupEnd();
    console.log("A group-less log trace.");

![Creating a collapsed group](console-files/groupcollapsed.png)


## console.groupEnd() ##

<!--@Closes the most recently created logging group that previously created with `console.group()` or `console.groupCollapsed()`. See [console.group()](#consolegroupobject-object) and [console.groupCollapsed()](#consolegroupcollapsedobject-object) for examples.-->
关闭之前使用 `console.group()` 或 `console.groupCollapsed()` 创建的
日志分组。有关例子请参见 [console.group()](#consolegroupobject-object) 和 [console.groupCollapsed()](#consolegroupcollapsedobject-object)。


## console.info(object [, object, ...]) ##

<!--@This method is identical to [`console.log()`](#consolelogobject-object).-->
该方法等价于 [`console.log()`](#consolelogobject-object)。


## console.log(object [, object, ...]) ##

<!--@Displays a message in the console. You pass one or more objects to this method, each of which are evaluated and concatenated into a space-delimited string. The first parameter you pass to `log()` may contain _format specifiers_, a string token composed of the percent sign (`%`) followed by a letter that indicates the formatting to be applied.-->
在控制台中显示消息。您可以向该方法传递一个或多个对象，每一个都会求值并连接成
以空格分隔的字符串。您传递给 `log()` 的第一个参数可以包含
_格式化指示符_
，也就是由百分号（`%`）加上字母组成的字符串记号，表示要应用的格式。

<!--@Dev Tools supports the following format specifiers:-->
开发者工具支持以下格式化指示符：

<!--@Format Specifier-->格式化指示符|<!--@Description-->描述
----------------|------------
`%s`            |<!--@Formats the value as a string.-->以字符串的形式显示值。
`%d` <!--@or-->或 `%i`   |<!--@Formats the value as an integer.-->以整数的形式显示值。
`%f`            |<!--@Formats the value as a floating point value.-->以浮点数的形式显示值。
`%o`            |<!--@Formats the value as an expandable DOM element (as in the Elements panel).-->以可展开的 DOM 元素（如元素面板中所示）显示值。
`%O`            |<!--@Formats the value as an expandable JavaScript object.-->以可展开的 JavaScript 对象显示值。
`%c`            |<!--@Formats the output string according to CSS styles you provide.-->根据您提供的 CSS 样式显示输出字符串。

<!--@Basic example:-->
基本例子：

    console.log("应用启动");

<!--@An example that uses string (`%s`) and integer (`%d`) format specifiers to insert the values contained by the variables `userName` and `userPoints`:-->
以下是使用字符串（`%s`）和整型（`%d`）格式化指示符
插入 `userName` 和 `userPoints` 变量值的例子：

    console.log("User %s has %d points", userName, userPoints);

![Console output styled with %c](console-files/log-format-specifier.png)

<!--@An example of using the element formatter (`%o`) and object formatter (`%O`) on the same DOM element:-->
以下是在同一 DOM 元素上使用元素格式化指示符（`%o`）和对象格式化指示符
（`%O`）的例子：

    console.log("%o, %O", document.body, document.body);

![Console output styled with %c](console-files/log-object-element.png)

<!--@The following example uses the **`%c`** format specifier to colorize the output string:-->
以下例子使用 **`%c`** 格式化指示符设置输出字符串的颜色：

    console.log("%cUser %s has %d points", "color:orange; background:blue; font-size: 16pt", userName, userPoints);

![Console output styled with %c](console-files/log-format-styling.png)


## console.profile([label]) ##

<!--@When the Chrome DevTools is open, calling this function starts a JavaScript CPU profile with an optional label.To complete the profile, call `console.profileEnd()`. Each profile is added to the Profiles tab.-->
Chrome 开发者工具打开时，调用该函数可以启动 JavaScript 性能分析器，还可以
指定标签。要结束性能分析，请调用 `console.profileEnd()`。每一次性能分析报告
都会添加到性能分析标签页。

<!--@In the following example a CPU profile is started at the entry to a function that is suspected to consume excessive CPU resources, and ended when the function exits.-->
以下例子中，在消耗大量 CPU 资源的可疑函数入口处开始 CPU 性能分析，在函数
退出时结束。

    function processPixels() {
      console.profile("Processing pixels");
      // 处理完像素之后
      console.profileEnd();
    }


## console.profileEnd() ##

<!--@Stops the current JavaScript CPU profiling session, if one is in progress, and prints the report to the Profiles panel.-->
结束当前的 JavaScript CPU 性能分析会话（如果正在进行的话），并在性能分析面板
显示报告。

    console.profileEnd()

<!--@See [console.profile()](#consoleprofilelabel) for example use.-->
有关使用案例请参见 [console.profile()](#consoleprofilelabel)。


## console.time(label) ##

<!--@Starts a new timer with an associated label. When `console.timeEnd()` is called with the same label, the timer is stopped the elapsed time displayed in the Console. Timer values are accurate to the sub-millisecond.-->
启动计时器，并关联某个标签。以相同标签调用 `console.timeEnd()` 时，计时器
停止，并在控制台中显示流逝的时间。计时器的值精确到亚毫秒级别。

    console.time("初始化数组");
    var array= new Array(1000000);
    for (var i = array.length - 1; i >= 0; i--) {
        array[i] = new Object();
    };
    console.timeEnd("初始化数组");

![Example of using console.time() and timeEnd()](console-files/time-duration.png)

<!--@Note: The string you pass to the `time()` and `timeEnd()` methods must match for the timer to finish as expected.-->
注意：您传递给 `time()` 和 `timeEnd()` 方法的字符串必须匹配，这样计时器才能
正常停止。


## console.timeEnd(label) ##

<!--@Stops the timer with the specified label and prints the elapsed time.-->
停止具有指定标签的计时器，并显示流逝的时间。

<!--@For example usage, see [console.time()](#consoletimelabel).-->
有关具体用法，请参见 [console.time()](#consoletimelabel)。


## console.timeline(label)

<!--@Starts a Timeline recording with an optional label.-->
开始时间线记录，可以指定标签。


## console.timelineEnd()

<!--@Stops the Timeline recording if one is in progress.-->
如果正在进行时间线记录的话停止记录。


## console.timeStamp([label]) ##

<!--@This method adds an event to the Timeline during a recording session. This lets you visually correlate your code generated time stamp to other events, such as screen layout and paints, that are automatically added to the Timeline.-->
该方法在时间线记录会话中添加一个事件，这样可以使您将代码生成的时间戳和其他
自动添加到时间线中的事件联系起来，例如屏幕布局和绘制。

<!--@See [Marking the Timeline](console.md#marking-the-timeline) for an example of using `console.timeStamp()`.-->
有关使用 `console.timeStamp()` 的例子，请参见
[标记时间线](console.md#marking-the-timeline)。


## console.trace(object) ##

<!--@Prints a stack trace from the point where the method was called, including links to the specific lines in the JavaScript source. A counter indicates the number of times that `trace()` method was invoked at that point, as shown in the screen shot below.-->
打印调用方法所在位置的堆栈跟踪，包括跳转到 JavaScript 源代码中对应行号的
链接。如下面的屏幕截图所示，计数器表示在该位置调用过 `trace()` 方法的次数。

![Example of a stack trace with counter](console-files/console-trace.png)

<!--@It is also possible to pass in arguments to trace(). For example:-->
还可以向 trace() 传递参数，例如：

![Example of a stack trace with arguments](console-files/console-trace-args.png)


## console.warn(object [, object, ...]) ##

<!--@This method is like [`console.log()`](#consolelogobject-object) but also displays a yellow warning icon along with the logged message.-->
该方法与 [`console.log()`](#consolelogobject-object) 类似，但是记录的消息旁
会显示黄色的警告图标。

    console.warn("User limit reached! (%d)", userPoints);

![Example of console.warn()](console-files/log-warn.png)


## debugger ##

<!--@The global `debugger` function causes Chrome to stop program execution and start a debugging session at the line where it was called. It is equivalent to setting a "manual" breakpoint in the Sources tab of Chrome DevTools.-->
全局的 `debugger` 函数使 Chrome 浏览器停止程序执行，并在调用所在行开始
调试会话，等价于在 Chrome 开发者工具的源代码标签页中设置“手动”断点。

<!--@Note: The `debugger` command is not a method of the `console` object.-->
注：`debugger` 命令不是 `console` 对象的方法。

<!--@In the following example the JavaScript debugger is opened when an object's `brightness()` function is invoked:-->
在以下例子中，调用对象的 `brightness()` 函数时打开 JavaScript 调试器：

    brightness : function() {
        debugger;
        var r = Math.floor(this.red*255);
        var g = Math.floor(this.green*255);
        var b = Math.floor(this.blue*255);
        return (r * 77 + g * 150 + b * 29) >> 8;
    }

![Example of using debugger command](console-files/debugger.png)

{{/partials.standard_devtools_article}}
