{{+bindTo:partials.standard_devtools_article}}

# <!--@Command Line API Reference-->命令行 API 参考

<!--@The Command Line API is a collection of functions for performing common tasks with the Chrome Developer Tools. These include convenience functions for selecting and inspecting elements in the DOM, stopping and starting the profiler, and monitoring DOM events. This API complements the [Console API](console-api.md), the Command Line API is only available from within the console itself.-->
命令行 API 由一些函数组成，用于在 Chrome 开发者工具中进行常见任务，这些方便
的函数包括在 DOM 中选择和审查元素、启动和停止性能分析器以及监控 DOM 事件。
该 API 与 [控制台 API](console-api) 互补，命令行 API 仅在控制台内可用。


## $_ ##

<!--@Returns the value of the most recently evaluated expression. In the following example, a simple expression is evaluated. The `$_` property is then evaluated, which contains the same value:-->
返回最近运行的表达式的值。在下面的例子中，运行了一个简单的表达式，
然后计算 `$_` 属性的值，包含同样的值：

<img src="commandline-api-files/last_expression.png" class="screenshot"/>

<!--@In the next example, the evaluated expression is a call to the [`$$()`](#selector_1) method, which returns an array of elements that match the CSS selector. It then evaluates `$_.length` to get the length of the array (17), which becomes the most recently evaluated expression.-->
下一个例子中，运行的表达式是 [`$$()`](#selector_1) 方法的调用，返回匹配
指定 CSS 选择器的元素数组。然后对 `$_.length` 求值，获取数组长度（17），
成为最近运行的表达式。

<img src="commandline-api-files/last_expression_2.png" class="screenshot"/>



## $0 - $4 ##

<!--@Dev Tools remembers the last five DOM elements (or JavaScript heap objects) that you've selected in the  tab (or Profiles panel). It makes those objects available as **`$0`**, **`$1`**, **`$2`**, **`$3`**, and **`$4`**. **`$0`** returns the most recently selected element or JavaScript object, **`$1`** returns the second most recently selected one, and so on.-->
开发者工具会记住您在标签页（或性能分析面板）中选择的最后五个 DOM 元素
（或 JavaScript 堆对象），并且可以通过 **`$0`**、**`$1`**、**`$2`**、
**`$3`** 和 **`$4`** 访问。**`$0`** 返回最后选择的元素或 JavaScript 对象，
**`$1`** 返回倒数第二个选择的内容，依次类推。

<!--@In the following example, an element with the ID `gc-sidebar` is selected in the Elements tab. In the Console window `$0` has been evaluated, which displays the same element.-->
在下面的例子中，在元素标签页中选择了 ID 为 `gc-sidebar` 的元素。在控制台
窗口中对 `$0` 求值，显示同一个元素。

![Example of $0](commandline-api-files/$0.png)

<!--@The image below shows the `gc-content` element selected in the same page. The **`$0`** now refers to newly selected element, while **`$1`** now returns the previously selected one (`gc-sidebar`).-->
下图显示同一网页中选择的 `gc-content` 元素，**`$0`** 现在指向新选择的元素，
而 **`$1`** 返回之前选择的元素（`gc-sidebar`）。

![image alt text](commandline-api-files/$1.png)



## $(selector) ##

<!--@Returns reference to the first DOM element with the specified CSS selector.This function is an alias for [`document.querySelector()`](http://docs.webplatform.org/wiki/css/selectors_api/querySelector) function.-->
返回匹配指定 CSS 选择器的第一个 DOM 元素引用，
该函数是 [`document.querySelector()`](http://docs.webplatform.org/wiki/css/selectors_api/querySelector) 函数
的别名。

<!--@The following example saves a reference to the first `<img>` element in the document and calls displays its `src` property:-->
以下例子将获取文档中第一个 `<img>` 元素引用，并显示它的 `src` 属性：

    $('img').src;

![image alt text](commandline-api-files/$img_src.png)



## $$(selector) ##

<!--@Returns an array of elements that match the given CSS selector. This command is equivalent to calling [`document.querySelectorAll()`](http://docs.webplatform.org/wiki/css/selectors_api/querySelectorAll).-->
返回匹配指定 CSS 选择器的元素数组，该命令等价于 [`document.querySelectorAll()`](http://docs.webplatform.org/wiki/css/selectors_api/querySelectorAll)。

<!--@The following example uses `$$()` to create an array of all `<img>` elements in the current document and displays the value of each element's `src` property.-->
以下例子使用 `$$()` 创建当前文档中所有 `<img>` 元素的数组，
并显示每个元素的 `src` 属性。

    var images = $$('img');
    for (each in images) {
        console.log(images[each].src);
    }

![Example of using $$() to select all images in the document and display their sources.](commandline-api-files/$$img_src.png)

<!--@Note: Press Shift+Enter in the console to start a new line without executing the script.-->
注：在控制台中按下 Shift+Enter 可以开始新的一行，而不会执行脚本。



## $x(path) ##

<!--@Returns an array of DOM elements that match the given XPath expression. For example, the following returns all the `<p>` elements that contain `<a>` elements:-->
返回匹配指定 XPath 表达式的 DOM 元素数组。例如，以下语句返回所有
包含 `<a>` 元素的 `<p>` 元素：

    $x("//p[a]")

![Example of using an Xpath selector](commandline-api-files/$xpath.png)



## clear() ##

<!--@Clears the console of its history.-->
清除控制台的历史记录。

    clear();

<!--@Also see -->请参见[<!--@Clearing the console-->清除控制台](console.md#clearing-the-console-history)<!--@.-->。



## copy(object) ##

<!--@Copies a string representation of the specified object to the clipboard.-->
将指定对象的字符串表达形式复制到剪贴板。

    copy($0);


## debug(function)

<!--@When the function specified is called, the debugger will be invoked and will break inside the function on the Sources panel allowing you to be able to step through the code and debug it.-->
调用指定的函数时，启动调试器并中断执行，在源代码面板中进入函数内部，允许您单步执行代码并调试它。

    debug(getData);


![Breaking inside a function with debug()](commandline-api-files/debug.png)

<!--@Use [undebug(fn)](#undebugfunction) to stop breaking on the function, or use the UI to disable all breakpoints.-->
调用 [undebug(fn)](#undebugfunction) 后，不会再该函数上中断，也可以通过
用户界面禁用所有断点。

## dir(object)

<!--@Displays an object-style listing of all the properties of the specified object. This method is an alias for the Console API's-->
以对象列表的形式显示指定对象的所有属性，该方法是控制台 API [`console.dir()`](console-api#consoledirobject) <!--@method.-->方法的别名。

<!--@The following example shows the difference between evaluating `document.body` directly in the command line, and using `dir()` to display the same element.-->
以下例子展现了直接在命令行中执行 `document.body` 以及使用 `dir()` 显示
同一元素的区别。

    document.body;
    dir(document.body);

![Logging document.body with and without dir() function](commandline-api-files/document.body.png)

<!--@For more information, see the-->有关更多信息，请参见控制台 API 中的 [`console.dir()`](console-api#consoledirobject) <!--@entry in the Console API.-->项。


## dirxml(object)

<!--@Prints an XML representation of the specified object, as seen in the Elements tab. This method is equivalent to the [`console.dirxml()`](console-api#consoledirxmlobject) method.-->
以 XML 形式显示指定对象，如元素面板中所示。该方法等价于 [`console.dirxml()`](console-api#consoledirxmlobject) 方法。


## inspect(object/function)

<!--@Opens and selects the specified element or object in the appropriate panel: either the Elements panel for DOM elements and the Profiles panel for JavaScript heap objects.-->
打开并在相应的面板中选择指定元素或对象：DOM 元素在元素面板中，JavaScript 堆
对象在性能分析面板中。

<!--@The following example opens the first child element of `document.body` in the Elements panel:-->
以下例子在元素面板中打开 `document.body` 的第一个子节点：

    inspect(document.body.firstChild);

![Inspecting an element with inspect()](commandline-api-files/inspect.png)

<!--@When passing a function to inspect, when the function is called it will open it up in the Sources panel for you to inspect.-->
在 inspect 中传递函数时，函数调用之后会在源代码面板中打开它让您审查。


## getEventListeners(object) ##

<!--@Returns the event listeners registered on the specified object. The return value is an object that contains an array for each registered event type ("click" or "keydown", for example). The members of each array are objects that describe the listener registered for each type. For example, the following lists all the event listeners registered on the `document` object.-->
返回指定对象上注册的事件监听器。返回值是一个对象，每一种注册的事件类型（例如
“click”或“keydown”）都包含一个数组。数组的成员也是对象，描述对应类型注册的
监听器。例如，以下代码列出 `document` 对象上注册的所有事件监听器。

    getEventListeners(document);

![Output of using getEventListeners()](commandline-api-files/geteventlisteners_short.png)

<!--@If more than one listener is registered on the specified object, then the array contains a member for each listener. For instance, in the following example there are two event listeners registered on the `#scrollingList` element for the "mousedown" event:-->
如果指定对象上注册了多个监听器，数组包含每一个监听器对应的成员。例如，
下面的例子中，`#scrollingList` 元素上注册了两个“mousedown”事件的监听器：

![](commandline-api-files/geteventlisteners_multiple.png)

<!--@You can further expand each of these objects to explore their properties:-->
您可以进一步展开其中的每一个对象，浏览它们的属性：

![Expanded view of listener object](commandline-api-files/geteventlisteners_expanded.png)



## keys(object)

<!--@Returns an array containing the names of the properties belonging to the specified object. To get the associated values of the same properties, use [values()](#valuesobject).-->
返回一个数组，包含属于指定对象的属性名称。要获取这些属性的对应值，
请使用 [values()](#valuesobject)。

<!--@For example, suppose your application defined the following object:-->
例如，假设您的应用程序定义了以下对象：

    var player1 = {
        "name": "Ted",
        "level": 42
    }

<!--@Assuming `player1` was defined in the global namespace (for simplicity), typing `keys(player1)` and `values(player1)` in the Console would result in the following:-->
假设 `player1` 在全局命名空间中定义（为了简单），在控制台中
输入 `keys(player1)` 和 `values(player1)` 后会显示以下内容：

<img src="commandline-api-files/keys-values2.png" style="max-width:100%" alt="Example of keys() and values() methods">



## monitor(function)

<!--@When the function specified is called, a message is logged to the console that indicates the function name along with the arguments that are passed to the function when it was called.-->
指定的函数调用时，在控制台中记录消息，显示函数名以及调用时传递给该函数的参数。

    function sum(x, y) {
        return x + y;
    }
    monitor(sum);

<img src="commandline-api-files/monitor.png" style="max-width:100%" alt="Example of monitor() method">

<!--@Use [unmonitor(function)](#unmonitorfunction) to cease monitoring.-->
使用 [unmonitor(function)](#unmonitorfunction) 取消监视。


## monitorEvents(object[, events])

<!--@When one of the specified events occurs on the specified object, the Event object is logged to the console. You can specify a single event to monitor, an array of events, or one of the generic events "types" that are mapped to a predefined collection of events. See examples below.-->
指定对象上发生指定的某一个事件时，对应的 Event 对象会在控制台中记录。
您可以指定要监控的一个事件、事件数组或某一种通用事件“类型”，映射为预定义的
一组事件。请参见下面的例子。

<!--@The following monitors all `resize` events on the `window` object.-->
下列语句监控 `window` 对象上的所有 `resize` 事件。

    monitorEvents(window, "resize");

![Monitoring window resize events](commandline-api-files/monitor-resize.png)

<!--@The following defines an array to monitor both "resize" and "scroll" events on the `window` object:-->
下列语句监控 `window` 对象上的 `resize` 和 `scroll` 事件：

    monitorEvents(window, ["resize", "scroll"])

<!--@You can also specify one of the available event "types", strings that map to predefined sets of events. The table below lists the available event types and their associated event mappings:-->
您还可以指定某一种可用的事件“类型”，也就是映射为预定义的一组事件的字符串。
下表列举了可用的事件类型及其对应的事件映射：

|<!--@Event type-->事件类型|<!--@Corresponding mapped events-->对应的事件
-----|---------------
**mouse**| "`mousedown`", "`mouseup`", "`click`", "`dblclick`", "`mousemove`", "`mouseover`", "`mouseout`", "`mousewheel`"
**key** | "`keydown`", "`keyup`", "`keypress`", "`textInput`"
**touch** | "`touchstart`", "`touchmove`", "`touchend`", "`touchcancel`"
**control**| "`resize`", "`scroll`", "`zoom`", "`focus`", "`blur`", "`select`", "`change`", "`submit`", "`reset`"

<!--@For example, the following uses the "key" event type all corresponding key events on an input text field ("`#msg`").-->
例如，以下语句使用“key”事件类型监控文本框（`#msg`）上的所有键盘事件。

    monitorEvents($("#msg"), "key");

<!--@Below is sample output after typing two characters in the text field:-->
以下是在文本框中键入两个字符后的示例输出：

![Monitoring key events](commandline-api-files/monitor-key-events.png)

<img src="commandline-api-files/monitor-key-events.png" class="screenshot" alt="">



## profile([name])

<!--@Starts a JavaScript CPU profiling session with an optional name. To complete the profile call [`profileEnd()`](#profileendname).-->
启动 JavaScript CPU 性能分析会话，可以指定名称。要结束性能分析，
请调用 [`profileEnd()`](#profileendname)。

<!--@To start profiling:-->
如果要开始性能分析：

    profile("我的性能分析报告")

<!--@To stop profiling and display the results in the Profiles panel:-->
如果要结束性能分析，并在性能分析面板中显示结果：

    profileEnd("我的性能分析报告")

<!--@Profiles can also be nested. For example, this will work in any order:-->
性能分析也可以嵌套。例如，以下代码任意改变顺序都能正常工作：

    profile('A');
    profile('B');
    profileEnd('A');
    profileEnd('B');

<!--@For more examples, see [Controlling the CPU profiler](console.md#controlling-the-cpu-profiler).-->
有关更多例子，请参见[控制 CPU 性能分析器](console.md#controlling-the-cpu-profiler)。



## profileEnd([name])

<!--@Stops the current profiling session started with the [profile()](#profilename) method and displays the results in the Profiles panel.-->
结束通过 [profile()](#profilename) 开始的性能分析会话，并在性能分析面板中
显示结果。


## table(data[, columns])

<!--@Log object data with table by passing in a data object in with optional column headings. For example, to display a list of names using a table in the console you would do:-->
传递数据对象以及可选的列标头，以表格形式记录对象数据。
例如，如果要在控制台中以表格形式显示姓名列表，您可以执行：

    var names = {
        0: { firstName: "John", lastName: "Smith" },
        1: { firstName: "Jane", lastName: "Doe" }
    };

    table(names);

<img src="commandline-api-files/table.png" style="max-width:100%" alt="Example of table() method">


## undebug(function)

<!--@Stops the debugging of the specified function so that when the function is called the debugger will no longer be invoked.-->
停用指定函数的调试，函数调用时不再启动调试器。

    undebug(getData);


## unmonitor(function)

<!--@Stops the monitoring of the specified function. Used in concert with [monitor(fn)](#monitorfunction).-->
停止对指定函数的监视，与 [monitor(fn)](#monitorfunction) 一起使用。

    unmonitor(getData);


## unmonitorEvents(object[, events])

<!--@Stops monitoring events for the specified object and events. For example, the following stops all event monitoring on the `window` object:-->
停止监控指定对象上的事件。例如，以下语句停止监控 `window` 对象上的所有事件：

    unmonitorEvents(window);

<!--@You can also selectively stop monitoring specific events on an object. For example, following code starts monitoring all mouse events on the currently selected element, and then stops monitoring "mousemove" events (perhaps to reduce noise in the console output).-->
您还可以选择性地停止监控对象上的某些事件。例如，以下代码开始监控当前选定元素
上的所有鼠标事件，然后停止监控“mousemove”事件（可以减少控制台输出中的
无用信息）。

    monitorEvents($0, "mouse");
    unmonitorEvents($0, "mousemove");

<!--@Also see [Monitoring events](console.md#monitoring-events).-->
请参见[监控事件](console.md#monitoring-events)。



## values(object)

<!--@Returns an array containing the values of all properties belonging to the specified object.-->
返回包含指定对象所有属性值的数组。

    values(object);

{{/partials.standard_devtools_article}}
