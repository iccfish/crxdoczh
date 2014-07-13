{{+bindTo:partials.standard_devtools_article}}

# <!--@Evaluating network performance-->评估网络性能

<!--@The Network panel records information about each network operation in your application, including detailed timing data, HTTP request and response headers, cookies, WebSocket data, and more. The Network panel helps you answer questions about the network performance of your web application, such as:-->
Network（网络）面板记录了您的应用程序中每一次网络操作的有关信息，
包括详细的时间数据、HTTP 请求和响应标头、Cookie、WebSocket 数据等等。
网络面板可以帮助您了解网上应用的网络性能，例如：

* <!--@Which resource had the slowest time to first byte?-->
哪些请求接收第一个字节前等待了最长的时间？
* <!--@Which resources took the longest time to load (duration)?-->
哪些请求载入花费的时间（时长）最长？
* <!--@Who initiated a particular network request?-->
某个网络请求由谁发起？
* <!--@How much time was spent in the various network phases for a particular resource?-->
某一资源在不同的网络阶段分别花费了多少时间？



## <!--@About the Resource Timing API-->关于资源时间 API

<!--@The Network panel uses the [Resource Timing API](http://www.w3.org/TR/resource-timing), a JavaScript API that provides detailed network timing data for each loaded resource. For example, the API can tell you precisely when the HTTP request for an image started, and when the image's final byte was received. The following illustration shows the network timing data points that the Resource Timing API provides.-->
网络面板使用[资源时间 API](http://www.w3.org/TR/resource-timing/)——
为加载的每一项资源提供详细网络时间数据的 JavaScript API。
例如，该 API 可以准确地告诉您某个图片的 HTTP 请求什么时候开始、
什么时候接收到图片的最后一字节。下图展现了资源时间 API 提供的网络时间数据点。

<img src="network-files/resource-timing-overview.png" alt="Resource timing overview"/>

<!--@The API is available to any web page, not just DevTools. In Chrome, it's exposed as methods on the global `window.performance` object. The `performance.getEntries()` method returns an array of "resource timing objects", one for each requested resource on the page.-->
该 API 在任何网页，而不仅仅是开发者工具中都可以使用。在 Chrome 浏览器中，
它以全局 `window.performance` 对象方法的形式提供。
`performance.getEntries()` 方法返回“资源时间对象”组成的数组，
分别对应网页请求的每一项资源。

<!--@Try this: open the JavaScript console on the current page, enter the following at the prompt, and hit Return:-->
试一试：在当前网页中打开 JavaScript 控制台，在提示符下输入以下内容，并按回车键：

    window.performance.getEntries()[0]

<!--@This evaluates the first element in the array of resource timing objects and displays its properties in the console, as shown below.-->
该语句获取资源时间对象数组中的第一个元素，并在控制台中显示它的属性，如下所示。

<img src="network-files/getentries.png" alt="Performance resource timing"/>

<!--@Each timestamp is in microseconds, following the [High Resolution
Time](http://www.w3.org/TR/hr-time/#sec-high-resolution-time) specification. This API is [available in
Chrome](http://updates.html5rocks.com/2012/08/When-milliseconds-are-not-enough-performance-now) as the `window.performance.now()` method.-->
时间戳以毫秒表示，遵循[高精度时间](http://www.w3.org/TR/hr-time/#sec-high-resolution-time)
规范，[在 Chrome 浏览器中](http://updates.html5rocks.com/2012/08/When-milliseconds-are-not-enough-performance-now)
该 API 可以通过 `window.performance.now()` 方法访问。



## <!--@Network panel overview-->网络面板概述

<!--@The Network panel automatically records all network activity while DevTools is open. The first time you open the panel it may be empty. Reload the page to start recording, or simply wait for network activity to occur in your application.-->
开发者工具打开时，网络面板会自动记录所有网络活动。
您第一次打开该面板时可能是空的，重新加载网页便可开始记录，
或者等您的应用程序中产生网络活动。

<img src="network-files/network-overview.png" alt="Network overview"/>

<!--@Each requested resource is added as a row to the Network table, which contains the columns listed below. Note the following about the Network table:-->
请求的每一项资源都会在网络面板的表格中添加一行，包含下面这些信息。请注意网络请求表格的这几个问题：

* <!--@Not all columns listed below are visible by default; you can easily [show or hide columns](#adding-and-removing-table-columns).-->
默认情况下以下每一列并不是都可见的，您可以很方便地[显示或隐藏列](#adding-and-removing-table-columns)。
* <!--@Some columns contain a primary field and a secondary field (**Time** and **Latency**, for example). When viewing the Network table with [large resource rows](#changing-resource-row-sizes) both fields are shown; when using small resource rows only the primary field is shown.-->
一列中有可能包含主要字段和辅助字段（例如 **Time**（时间）与 **Latency**
（延迟））。使用[完整资源行](#changing-resource-row-sizes)
查看网页请求列表时，这两种字段都会显示，使用精简资源行时就只显示主要字段。
* <!--@You can [sort](#sorting-and-filtering) the table by a column's value by clicking the column header. The [the Timeline column](#timeline-view) behaves a bit differently: clicking its column header displays a menu of additional sort fields. See [Timeline view](#timeline-view) and [Sorting and filtering](#sorting-and-filtering) for more information.-->
您可以单击列标头按照某一列的值对表格进行[排序](#sorting-and-filtering)。
[Timeline（时间线）列](#timeline-view)的行为略有区别：单击列标头后显示一个菜单，
包含其他排序字段。有关更多信息，请参见[时间线视图](#timeline-view)和
[排序和过滤](#sorting-and-filtering)。

<table>
<thead>
<tr>
<th><!--@Field-->字段</th>
<th><!--@Description-->描述</th>
</tr>
</thead>
<tbody>
<tr>
<td><strong>Name</strong><!--@ and-->（名称）和 <strong>Path</strong>（路径）</td>
<td><!--@The name and URL path of the resource, respectively.-->分别为资源的名称和 URL 路径。</td>
</tr>
<tr>
<td><strong>Method</strong>（方法）</td>
<td><!--@The HTTP method used for the request (GET or POST, for example).-->请求使用的
HTTP 方法（例如 GET 或 POST）。</td>
</tr>
<tr>
<td><strong>Status</strong><!--@ and-->（状态）和 <strong>Text</strong>（消息）</td>
<td><!--@The HTTP status code and text message, respectively.-->分别为
HTTP 状态码和文字消息。</td>
</tr>
<tr>
<td><strong>Domain</strong>（域名）</td>
<td><!--@The domain of the resource request.-->资源请求的域名。</td>
</tr>
<tr>
<td><strong>Type</strong>（类型）</td>
<td><!--@The MIME type of the requested resource.-->请求资源的 MIME 类型。</td>
</tr>
<tr>
<td><strong>Initiator</strong>（发起方）</td>
<td><!--@The object or process that initiated the request. It can have one of the following values:-->
发起资源的对象或过程，可以是以下某一个值：
  <dl>
    <dt>Parser（分析器）</dt>
    <dd><!--@Chrome's HTML parser initiated the request.-->Chrome
    浏览器的 HTML 分析器发起该请求。</dd>
    <dt>Redirect（重定向）</dt>
    <dd><!--@A HTTP redirect initiated the request.-->HTTP
    重定向发起该请求。</dd>
    <dt>Script（脚本）</dt>
    <dd><!--@A script initiated the request.-->脚本发起该请求。</dd>
    <dt>Other（其他）</dt>
    <dd><!--@Some other process or action initiated the request, such as the user navigating to a page via a link, or by entering a URL in the address bar.-->其他过程或操作发起该请求，例如用户通过链接或者在地址栏中输入
    URL 导航到某个网页。</dd>
  </dl>
</td>
</tr>
<tr>
<td><strong>Cookies</strong></td>
<td><!--@The number of cookies transferred in the request. These correspond to the cookies shown in the <a href="#cookies">Cookies tab</a> when viewing details for a given resource.-->
请求中传输的 Cookie 数量，对应于查看资源详情时 <a href="#cookies">Cookies 标签页</a>中显示的 Cookie。</td>
</tr>
<tr>
<td><strong>Set-Cookies</strong></td>
<td><!--@The number of cookies set in the HTTP request.-->HTTP
请求中设置的 Cookie 数目。</td>
</tr>
<tr>
<td><strong>Size</strong><!--@ and-->（大小）和 <strong>Content</strong>（内容）</td>
<td><!--@Size is the combined size of the response headers (usually a few hundred bytes) plus the response body, as delivered by the server.
Content is the size of the resource's decoded content.
If the resource was loaded from the browser's cache rather than over the network, this field will contain the text (from cache).-->
大小是服务器传输的响应标头（通常为几百字节）加上响应正文大小，内容是资源解码后内容的大小。如果资源从浏览器缓存而不是通过网络加载，该字段会包含“(from cache)”（来自缓存）字样。</td>
</tr>
<tr>
<td><strong>Time</strong><!--@ and-->（时间）和 <strong>Latency</strong>（延迟）</td>
<td><!--@Time is total duration, from the start of the request to the receipt of the final byte in the response.
Latency is the time to load the first byte in the response.-->
时间是从请求开始到接收完响应的最后一字节所经过的总共时长，延迟是从请求开始到加载响应第一个字节的时间。</td>
</tr>
<tr>
<td><strong>Timeline</strong>（时间线）</td>
<td><!--@The Timeline column displays a <a href="#timeline-view">timeline view</a> of all network requests. Clicking the header of this column reveals a menu of additional sorting fields. See Timeline view and Sorting and filtering for details.-->
时间线一列显示所有网络请求的<a href="#timeline-view"
>时间线视图</a>。单击这一列的标头后显示菜单，包含其他排序字段。有关更多详情请参见<a href="#timeline-view"
>时间线视图</a>以及<a href="#sorting-and-filtering"
>排序和过滤</a>。
</td>
</tr>
</tbody>
</table>

### <!--@Preserving the network log upon navigation-->导航时保留网络日志

<!--@By default, the current network record log is discarded when you navigate to another page, or reload the current page. To preserve the recording log in these scenarios, click the black **Preserve log upon navigation** button <img src="../images/recording-off.png" alt="Don't preserve log on navigation"/> at the bottom of the Network panel; new records are appended to the bottom of the table. Click the same button again (now red <img src="../images/recording-on.png" alt="Preserve resources on navigation"/>) to disable log preservation.-->
默认情况下，当您导航至另一个网页或重新加载当前网页时，当前的网络记录日志会被丢弃。
如果要在这些情况下保留记录日志，请单击网络面板顶部
黑色的 **Preserve log upon navigation**
（导航时保留日志）按钮 <img src="../images/recording-off.png" alt="alt text"/>，
这样新记录就会附加到表格底部。再次单击该按钮（
现在是红色的了 <img src="../images/recording-on.png" alt="alt text"/>）
则不再保留日志。

### <a name="sorting-and-filtering"></a><!--@Sorting and filtering-->排序和过滤 ###

<!--@By default, resources in the Network table are sorted by the start time of each request (the network "waterfall"). You can sort the table by another column value by clicking the column header. Click the header again to change the sort order (ascending or descending).-->
默认情况下，网络请求列表中的资源按照每个请求的起始时间排序（网络“瀑布”）。
您可以单击列标头按照另一列的值排序，再次单击标头改变排序顺序（升序或降序）。

<img src="network-files/sorting.png" alt="Sort by"/>

<!--@The Timeline column is unique from the others in that, when clicked, it displays a menu of additional sort fields.-->
Timeline（时间线）这一列和其他列不同，单击时显示一个菜单，包含其他排序字段。

<img src="network-files/timeline-column.png" alt="Timeline column"/>

<!--@The menu contains the following sorting options:-->
该菜单包含以下排序选项：

* **Timeline**<!--@ — Sorts by the start time of each network request. This is the default sort, and is the same as sorting by the Start Time option).-->
（时间线）——根据网络请求的起始时间排序，这是默认的排序方式，和
 Start Time（起始时间）选项是一样的。
* **Start Time**<!--@ — Sorts by the start time of each network request (same as sorting by the Timeline option).-->
（起始时间）——根据网络请求的起始时间排序，和
 Timeline（时间线）选项是一样的。
* **Response Time**<!--@ — Sorts by each request's response time.-->
（响应时间）——根据请求的响应时间排序。
* **End Time**<!--@ — Sorts by the time when each request completed.-->
（结束时间）——根据请求完成的时间排序。
* **Duration**<!--@ — Sorts by the total time of each request.-->
（时长）——根据请求的总时间排序。
* **Latency**<!--@ — Sorts by the time between the start of the request and the beginning of the response (also known as the "time to first byte").-->
（延迟）——根据请求开始到响应开始（也称为接收到第一个字节的时间）
所经过的时间排序。

<!--@To filter the Network table to only show certain types of resources, click one of the content types along the bottom of the panel: **Documents**, **Stylesheets**, **Images**, **Scripts**, **XHR**, **Fonts**, **WebSockets**, and **Other**. In the following screenshot only CSS resources are shown. To view all content types, click the **All** filter button.-->
如果要过滤网络请求列表，只显示某些类型的资源，单击面板顶部某一种内容类型：
**Documents**（文档）、**Stylesheets**（样式表）、**Images**（图片）、
**Scripts**（脚本）、**XHR**、**Fonts**（字体）、**WebSockets** 和 **Other**
（其他）。如下屏幕截图中，只显示了 CSS 资源。要查看所有内容类型，
单击过滤器按钮 **All**（全部）。

<img src="network-files/filter-type.png" alt="Filter type"/>

### <a name="adding-and-removing-table-columns"></a><!--@Adding and removing table columns-->添加和删除表格列

<!--@You can change the default set of columns displayed by the Network table. To show or hide a column, Right+click or Control+click (Mac only) in the table header and select or deselect column names from the list.-->
您可以修改网络请求列表显示哪些列。要显示或隐藏某一列，右键单击
（或者在 Mac 上 Ctrl+单击）列表标头，选中或取消选中列表中列的名称。

<img src="network-files/add-remove-columns.png" alt="Add or remove columns"/>

### <a name="changing-resource-row-sizes"></a><!--@Changing resource row sizes-->更改资源行大小

<!--@You can view the Network table with large resource rows (the default), or small resource rows. Click the blue **Use small resource rows** toggle button <img src="../images/small-resource-rows.png" alt="Small resource rows"/> at the bottom of the panel to view small rows. Click the same button (now gray <img src="../images/large-resource-rows.png" alt="Large resource rows"/>) to view large resource rows again. Large rows enable some columns to display two text fields: a primary field and a secondary field (Time and Latency, for instance). When viewing small rows only the primary field is displayed.-->
您可以使用完整资源行（默认）或精简资源行查看网络请求列表。
单击面板顶部的蓝色的开关按钮 **Use small resource rows**
（使用精简资源行）<img src="../images/small-resource-rows.png" alt="Small resource rows"/> 查看
精简行，单击同一个按钮（现在是灰色的 <img src="../images/large-resource-rows.png" alt="Large resource rows"/>
）再次查看完整资源行。完整行模式下，有几列可以显示两个字段：
主要字段和辅助字段（例如 Time（时间）和 Latency（延迟））。
使用精简行模式查看时只显示主要字段。

<!--@In the following screenshot, the Network table is viewed with small resource rows and just the Timeline column.-->
以下屏幕截图中，以精简资源行模式查看网络请求列表，只有 Timeline（时间线）一列。

<img src="network-files/small-rows.png" alt="Resized resource rows">

### <a name="timeline-view"></a><!--@Timeline view-->时间线视图

<!--@The Timeline view in the Network panel graphs the time it took to load each resource, from the start of the HTTP request to the receipt of the final byte of the response. Each resource loading time is represented as a bar, color-coded according to the resource type. The length of the lighter-shaded part of each bar represents the request's latency, while the length of the darker-shaded part represents the time spent receiving the response data.-->
网络面板的时间线视图以图形方式表示每一项资源加载的时间，从 HTTP 请求开始到
响应的最后一字节。资源加载时间以条形图表示，根据资源类型使用不同的颜色。
条形图中颜色浅的部分表示请求延迟，颜色深的部分表示接收响应数据的时间。

<img src="network-files/network-timeline.png" alt="Network timeline view">

<!--@When you hover your mouse over a timeline row (but not over an actual bar) the request's latency and receipt time are displayed above the corresponding bar's light- and dark-shaded areas, respectively, as shown below.-->
当您将鼠标悬停在时间线的某一行上（但不是在条形图上）时，请求的延迟和接收时间
会分别显示在条形图对应的浅色和深色区域上，如上所示。

<img src="network-files/timeline-view-1.png" alt="Timeline view"/>

<!--@If you hover your mouse over the timeline bar itself, the complete timing data for the resource is presented in a pop-up. This is the same information that's presented in the [Timing details tab](#resource-network-timing) for a given resource.-->
如果您将鼠标悬停在时间线条形图上，就会弹出资源的完整时间数据，这一信息与
[Timing（时间）详情标签页](#resource-network-timing)中显示的一致。

<img src="network-files/timeline-view-hover.png" alt="Timeline view on hover"/>

<!--@The timeline indicates when the the [`DOMContentLoaded`](http://docs.webplatform.org/wiki/dom/events/DOMContentLoaded)
and [`load`](http://docs.webplatform.org/wiki/dom/events/load) events were fired with blue and red vertical lines, respectively. The `DOMContentLoaded` event is fired when the main document had been loaded and parsed. The `load` event is fired when all of the page's resources have been downloaded.-->
时间线分别用蓝色和红色竖线表示 [`DOMContentLoaded`](http://docs.webplatform.org/wiki/dom/Event/DOMContentLoaded) 和 
[`load`](http://docs.webplatform.org/wiki/dom/Element/load) 事件产生的时间。
主文档加载并分析完后产生 `DOMContentLoaded` 事件，
网页的所有资源下载完后产生 `load` 事件。

<img src="network-files/dom-lines.png" alt="DOM event lines"/>

<!--@Timeline bars are color-coded as follows:-->
时间线条形图根据以下规则使用不同的颜色：

<style>

#colortable {
  width: 50%;
  border: none;
}

#colortable td {
  border: none;
}

.doc { background: rgba(47, 102, 236, 0.6); width: 10%;}
.css { background: rgba(157, 231, 119, 0.6);width: 10%;}
.images { background: rgba(164, 60, 255, 0.6);width: 10%;}
.scripts { background: rgba(255, 121, 0, 0.6);width: 10%;}
.xhr { background: rgba(231, 231, 10, 0.6);width: 10%;}
.fonts { background: rgba(255, 82, 62,0.6);width: 10%;}
.other { background: rgba(187, 187, 188, 0.6);width: 10%;}
</style>

<!-- TODO: Fix formatting of cells -->
<table id="colortable">
<tr>
<td class="doc"></td>
<td>Documents（文档）</td>
</tr>
<tr>
<td class="css"></td>
<td>Stylesheets（样式表）</td>
</tr>
<tr>
<td class="images"></td>
<td>Images（图片）</td>
</tr>
<tr>
<td class="scripts"></td>
<td>Scripts（脚本）</td>
</tr>
<tr>
<td class="xhr"></td>
<td>XHR</td>
</tr>
<tr>
<td class="fonts"></td>
<td>Fonts（字体）</td>
</tr>
<tr>
<td class="other"></td>
<td>Other（其他）</td>
</tr>
</table>

### <!--@Saving and copying network information-->保存和复制网络信息 ##

<!--@<span class="kbd">Right-clicking</span> or <span class="kbd">Ctrl</span> + <span class="kbd">Click</span> (Mac only) within the Network table a context menu appears with several actions. Some of these actions apply to the resource row under the mouse click (like [copying HTTP request headers](#copying_requests_as_curl_commands)), while others apply to the entire network recording (such as [saving a Network recording as a HAR file](#saving_network_data)).-->
在网络请求列表中单击右键（或者在 Mac 上 <span class="kbd">Ctrl</span>+单击）弹出右键菜单，
包含几项操作。一部分操作适用于鼠标单击的资源行
（例如[复制 HTTP 请求标头](#copying-requests-as-curl-commands)），
另一部分操作针对整个网络记录
（例如[将网络记录保存为 HAR 文件](#saving-network-data)）。

<img src="network-files/right-click.png" alt="Right-click on Network"/>

<!--@The following menu actions apply to the selected resource:-->
以下菜单项应用于选定资源：

* **Open Link in New Tab**<!--@ — Opens the resource in a new tab. You can also double-click the resource name in the Network table.-->
（在新标签页中打开链接）——在新标签页中打开资源。
您也可以双击网络请求列表中的资源名称打开它。
* **Copy Link Address**<!--@ — Copies the resource URL to the system clipboard.-->
（复制链接地址）——将资源 URL 复制到系统剪贴板。
* **Copy Request Headers**<!--@ — Copies the HTTP request headers to the system clipboard.-->
（复制请求标头）——将 HTTP 请求标头复制到系统剪贴板。
* **Copy Response Headers**<!--@ — Copies the HTTP response headers to the system clipboard.-->
（复制响应标头）——将 HTTP 响应标头复制到系统剪贴板。
* **Copy as cURL**<!--@ — Copies the network request as a
  [cURL](http://curl.haxx.se/) command string to the system clipboard. See [Copying requests as cURL commands](#copying-requests-as-curl-commands).-->
（复制 cURL 命令）——将网络请求以 [cURL](http://curl.haxx.se/) 命令字符串的
形式表示并复制到系统剪贴板，请参见
[将请求复制为 cURL 命令](#copying-requests-as-curl-commands)。
* **Replay XHR**<!--@ — If the associated request is an XMLHTTPRequest, re-sends the original XHR.-->
（重放 XHR 请求）——如果对应请求是 XMLHttpRequest 请求，重新发送原始 XHR 请求。

#### <a name="copying-requests-as-curl-commands"></a><!--@Copying requests as cURL commands-->将请求复制为 cURL 命令

[cURL](http://curl.haxx.se/) <!--@is a command line tool for making HTTP transactions. The Network panel's **Copy as cURL** command recreates an HTTP request (including HTTP headers, SSL certificates, and query string parameters) and copies it as a cURL command string to the clipboard. You can then paste the string into a terminal window (on a system with cURL) to execute the same request.-->
是一个进行 HTTP 事务的命令行工具。网络面板的 **Copy as cURL**（复制 cURL 命令）
命令重新创建一个 HTTP 请求（包括 HTTP 标头、SSL 证书以及查询字符串参数），
并将它以 cURL 命令字符串的形式复制到剪贴板。您可以将它粘贴到终端窗口中
（在安装了 cURL 的系统上）执行同样的请求。

<!--@Below is an example cURL command line string taken from a XHR request on the Google News home page.-->
以下是 cURL 命令行字符串的一个例子，从 Google News 首页的某个 XHR 请求得到。

    curl 'http://news.google.com/news/xhrd=us' -H 'Accept-Encoding: gzip,deflate,:sdch' -H 'Host: news.google.com' -H 'Accept-Language: en-US,en;q=0.8' -H 'User-Agent: Mozilla/5.0 (Macintosh; Intel Mac OS X 10_8_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/29.0.1510.0 Safari/537.36' -H 'Accept: */*' -H 'Referer: http://news.google.com/nwshp?hl=en&tab=wn' -H 'Cookie: NID=67=eruHSUtoIQA-HldQn7U7G5meGuvZOcY32ixQktdgU1qSz7StUDIjC_Knit2xEcWRa-e8CuvmADminmn6h2_IRpk9rWgWMdRj4np3-DM_ssgfeshItriiKsiEXJVfra4n; PREF=ID=a38f960566524d92:U=af866b8c07132db6:FF=0:TM=1369068317:LM=1369068321:S=vVkfXySFmOcAom1K' -H 'Connection: keep-alive' --compressed

#### <a name="saving-network-data"></a><!--@Saving network data-->保存网络请求数据

<!--@You can save the data from a network recording as a HAR ([HTTP Archive](http://www.softwareishard.com/blog/har-12-spec/)) file, or copy the records as a HAR data structure to your clipboard. A HAR file contains a JSON data structure that describes the network "waterfall". Several [third-party](http://ericduran.github.io/chromeHAR/) [tools](https://code.google.com/p/harviewer/) can reconstruct the network waterfall from the data in the HAR file.-->
您可以将网络记录数据保存为 HAR
（[HTTP Archive](http://www.softwareishard.com/blog/har-12-spec/)）文件，
或者以 HAR 数据结构的形式将记录复制到剪贴板。
HAR 文件包含描述网络“瀑布”的 JSON 数据结构，
一些[第三方](http://ericduran.github.io/chromeHAR/)
[工具](https://code.google.com/p/harviewer/)
可以通过 HAR 文件中的数据重建网络瀑布。

**<!--@To save a recording:-->要保存记录：**

1. <!--@Right+click or Control+click on the Network table.-->
右键单击网络请求列表。
2. <!--@In the context menu that appears, choose one of the following actions:-->
在弹出的右键菜单中，选择以下某一项：
    * **Copy All as HAR**<!--@ — Copies the network recording to the system clipboard in the HAR format.-->
    （将所有请求复制为 HAR）——将网络请求以 HAR 格式复制到系统剪贴板。
    * **Save as HAR with Content**<!--@ — Saves all network data to a HAR file along with each page resource. Binary resources, including images, are encoded as Base64-encoded text.-->
    （将网络请求和内容一起另存为 HAR）——将所有网络数据以及每一项网页资源
    保存为 HAR 文件，包括图片在内的二进制资源编码为 base64 文本形式。

<!--@For more information,-->有关更多信息，请参见 [Web Performance Power Tool: HTTP Archive (HAR)](http://www.igvita.com/2012/08/28/web-performance-power-tool-http-archive-har/)<!--@.-->（网页性能高级工具：HTTP 档案（HAR））。



## <!--@Network resource details-->网络资源详情 #

<!--@When you click a resource name in the Network table a tabbed window appears that contains the following additional details:-->
当您单击网络请求列表中的资源名时，会弹出一个有标签页的窗口，
包含以下的额外信息：

* [<!--@HTTP request and response headers-->HTTP 请求和响应标头](#http-headers)
* [<!--@Resource preview-->资源预览](#resource-previews)
* [HTTP <!--@response-->响应](#http-response)
* [<!--@Cookie names and values-->Cookie 名称和值](#cookies)
* [WebSocket <!--@messages-->消息](#websocket-frames)
* [<!--@Resource network timing-->资源的网络时间](#resource-network-timing)

### <a name="http-headers"></a>HTTP <!--@headers-->标头

<!--@The Headers tab displays the resource's request URL, HTTP method, and response status code. Additionally, it lists the HTTP response and request headers and their values, and any query string parameters. You can view HTTP headers parsed and formatted, or in their source form by clicking the **View parsed**/**View source** toggle button, respectively, located next to each header's section. You can also view parameter values in their decoded or URL encoded forms by clicking the **View decoded**/**View URL encoded** toggle button next to each query string section.-->
Headers（标头）标签页显示资源的请求 URL、HTTP 方法以及响应状态码。
此外，它还会列出 HTTP 请求和响应标头以及对应的值，还有查询字符串参数。
您即可以查看 HTTP 标头分析和格式化后的样子，
也可以查看它们的原始形式，只要分别单击标头部分旁
的 **view parsed**（查看分析后的值）/**view source**（查看原始值）
开关按钮即可。您还可以单击查询字符串部分旁 **view decoded**
（查看解码后的值）/**view URL encoded**（查看 URL 编码后的值）
开关按钮以解码后的形式或 URL 编码后的形式查看参数值。

<img src="network-files/network-headers.png" alt="Network headers"/>

<!--@You can also [copy request and response headers](#saving-network-data) to your clipboard.-->
您还可以[将请求和响应标头复制到剪贴板](#saving-network-data)。

### <a name="resource-previews"></a><!--@Resource previews-->资源预览

<!--@The Preview tab displays a preview of the resource, when available. Previews are currently displayed for image and JSON resources, as shown below.-->
Preview（预览）标签页显示资源的预览（如果可用的话），
目前只有图片和 JSON 资源会显示预览，如下所示：

<img src="network-files/resource-preview-json.png" alt="Resource JSON preview"/>

<img src="network-files/network-image-preview.png" alt="Resource image preview"/>

<!--@You can view the resource's unformatted response on the [Response
tab](#http-response).-->
您还可以在 [Response（响应）标签页](#http-response)中查看资源格式化前的响应。

### <a name="http-response"></a>HTTP <!--@response-->响应

<!--@The Response tab contains the resource's unformatted content. Below is a screenshot of a JSON data structure that was returned as the response for a request.-->
Response（响应）标签页包含资源格式化前的内容。如下屏幕截图是某个请求返回
的 JSON 数据结构响应。

<img src="network-files/response.png" alt="Resource response preview"/>

<!--@You can also [view formatted previews](#resource-previews) of some resource types, including JSON data structures and images.-->
您还可以查看某些资源类型[格式化后的预览](#resource-previews)，
它们包括 JSON 数据结构和图片。

### <a name="cookies"></a>Cookies

<!--@The Cookies tab displays a table of all the cookies transmitted in the
resource's HTTP request and response headers. You can also clear all cookies.-->
Cookies 标签页显示资源 HTTP 请求和响应标头中传输的所有 Cookie。
您还可以在这里清除所有 Cookie。

<img src="network-files/cookies.png" alt="Resource cookies"/>

<!--@The Cookies table contain the following columns:-->
Cookie 列表包含下面这几列：

<!-- TODO: Fix formatting of cells -->
<table>
<tr>
<th width="20%"><!--@Property-->属性</th>
<th><!--@Description-->描述</th>
</tr>
<tbody>
<tr>
<td><strong>Name</strong>（名称）</td>
<td><!--@The cookie's name.-->Cookie 名称。</td>
</tr>
<tr>
<td><strong>Value</strong>（值）</td>
<td><!--@The cookie's value.-->Cookie 值。</td>
</tr>
<tr>
<td><strong>Domain</strong>（域名）</td>
<td><!--@The cookie's domain.-->Cookie 的域名。</td>
</tr>
<tr>
<td><strong>Path</strong>（路径）</td>
<td><!--@The cookie's URL path.-->Cookie 的 URL 路径。</td>
</tr>
<tr>
<td><strong>Expires / Max-Age</strong>（过期时间/最长周期）</td>
<td><!--@The value of the cookie's expires or max-age properties.-->
Cookie 的过期时间或最长周期属性。</td>
</tr>
<tr>
<td><strong>Size</strong>（大小）</td>
<td><!--@The size of the cookie in bytes.-->Cookie 大小，以字节为单位。</td>
</tr>
<tr>
<td><strong>HTTP</strong>（仅在 HTTP 协议中使用）</td>
<td><!--@This indicates that the cookie should only be set by the browser in the HTTP request, and cannot be accessed with JavaScript. -->
该标志表示 Cookie 只能在 HTTP 请求中由浏览器设置，而不能通过 JavaScript 访问。</td>
</tr>
<tr>
<td><strong>Secure</strong>（安全）</td>
<td><!--@The presence of this attribute indicates that the cookie should only be transmitted over a secure connection.-->
存在该属性则意味着 Cookie 只能通过安全连接传输。</td>
</tr>
</tbody>
</table>

### <a name="websocket-frames"></a>WebSocket <!--@frames-->帧

<!--@The Frames tab shows messages sent or received over a WebSocket connection. This tab is only visible when the selected resource initiated a WebSocket connection. The table contains the following columns:-->
Frames（帧）标签页显示通过 WebSocket 连接发送或接收的消息，
只有选定资源发起 WebSocket 连接时该标签页才可见。其中的表格包含以下几列：

<table>
<tr>
<th width="20%"><!--@Name-->名称</th>
<th><!--@Description-->描述</th>
</tr>
<tr>
<td>Data（数据）</td>
<td><!--@The message payload. If the message is plain text, it's displayed here. For binary opcodes, this field displays the opcode's name and code. The following opcodes are supported:-->
消息内容。如果消息是纯文本就直接显示在这里，如果是二进制操作码，则显示
操作码名称和代码。支持以下操作码：
  <dl>
    <dt>Continuation Frame</dt>
    <dt>Binary Frame</dt>
    <dt>Connection Close Frame</dt>
    <dt>Ping Frame</dt>
    <dt>Pong Frame</dt>
  </dl>
</tr>
<tr>
<td>Length（长度）</td>
<td><!--@The length of the message payload in bytes.-->消息内容的长度，以字节为单位。</td>
</tr>
<tr>
<td>Time（时间）</td>
<td><!--@The time stamp when the message was created.-->消息创建时的时间戳。</td>
</tr>
</table>

<!--@Messages are color-coded according to their type. Outgoing text messages are color-coded light-green; incoming text messages are white:-->
消息会根据类型使用不同的颜色，传出文本消息以浅绿色表示，传入文本消息以白色表示：

<p><img src="network-files/websocket-text2.png" alt="Websocket text"/> </p>

WebSocket <!--@opcodes are light-yellow:-->操作码以淡黄色表示：

<p><img src="network-files/frames-opcode.png" alt="Websocket opcodes"/> </p>

<!--@Errors are light-red.-->错误以浅红色表示。

**<!--@Notes about current implementation:-->当前实现的注意事项：**

* <!--@To refresh the Frames table after new messages arrive, click the resource name on the left.-->
新消息到达后如果要刷新帧列表，请单击左侧的资源名称。
* <!--@Only the last 100 WebSocket messages are preserved by the Frames table.-->
帧列表中只保留最后 100 条 WebSocket 消息。

### <a name="resource-network-timing"></a><!--@Resource network timing-->资源的网络时间

<!--@The Timing tab graphs the time spent on the various network phases involved loading the resource. This is the same data displayed when you hover over a resource bar in the [Timeline view](#timeline-view).-->
Timing（时间）标签页以图形方式表示加载资源的过程中不同网络阶段花费的时间，
这些数据和您在[时间线视图](#timeline-view)中将鼠标悬停在资源条形图上显示的一致。

<img src="network-files/timing.png" alt="Resource network timing graph"/>

<!--@The table below lists the network phases shown in the Timing tab and their descriptions.-->
下表列举了时间标签页中显示的网络阶段以及它们的描述。

<!-- TODO: Fix formatting of cells -->
<table>
<tr>
<th style="width:20%"><!--@Property-->属性</th>
<th><!--@Description-->描述</th>
</tr>
<tr>
<td><strong>Proxy</strong>（代理）</td>
<td><!--@Time spent negotiating with a proxy server connection.-->连接到代理服务器时花费的时间。</td>
</tr>
<tr>
<td><strong>DNS Lookup</strong>（DNS 查询）</td>
<td><!--@Time spent performing the DNS lookup. You want to minimize DNS look ups.-->进行 DNS 查询花费的时间。您应该尽可能减少 DNS 查询。</td>
</tr>
<tr>
<td><strong>Blocking</strong>（阻塞）</td>
<td><!--@Time the request spent waiting for an already established connection to become available for re-use.-->等待已建立的连接空闲而可以重复利用所花费的时间。</td>
</tr>
<tr>
<td><strong>Connecting</strong>（连接）</td>
<td><!--@Time it took to establish a connection, including TCP handshakes/retries, DNS lookup, and time connecting to a proxy or negotiating a secure-socket layer (SSL). -->
建立连接花费的时间，包括 TCP 握手/重试、DNS 查询以及连接到代理服务器或安全套接字层（SSL）协商的时间。</td>
</tr>
<tr>
<td><strong>Sending</strong>（发送）</td>
<td><!--@Time spent sending the request.-->发送请求花费的时间。</td>
</tr>
<tr>
<td><strong>Waiting</strong>（等待）</td>
<td><!--@Time spent waiting for the initial response.-->等待最初响应的时间。</td>
</tr>
<tr>
<td><strong>Receiving</strong>（接收）</td>
<td><!--@Time spent receiving the response data. -->接收数据花费的时间。</td>
</tr>
</table>



## <!--@Additional resources-->其他资源

<!--@To learn more optimizing the network performance of your application, see the following resources:-->
要了解更多有关优化应用程序网络性能的内容，请参见以下资源：

* <!--@Use-->使用 [PageSpeed Insights](https://developers.google.com/speed/pagespeed/insights/) <!--@to identify performance best practices that can be applied to your site, and [PageSpeed optimization tools](https://developers.google.com/speed/pagespeed/optimization) to automate the process of applying those best practices.-->
找出可以应用在您网站上的性能优化方法，
使用 [PageSpeed 优化工具](https://developers.google.com/speed/pagespeed/optimization)
自动应用这些最佳优化方法。
* [High Performance Networking in Google
  Chrome](http://www.igvita.com/posa/high-performance-networking-in-google-chrome/)<!--@ discusses Chrome network internals and how you can take advantage of them to make your site faster.-->
（Google Chrome 浏览器中的高性能网络）讨论了 Chrome 浏览器
网络栈的内部实现以及您如何利用它们使您的网站更快。
* [How gzip compression works](https://developers.google.com/speed/articles/gzip)<!--@ provides a high level overview gzip compression and why it's a good idea.-->
（gzip 压缩的工作方式）提供了 gzip 压缩的总体概述以及为什么应该使用它。
* [Web Performance Best Practices](https://developers.google.com/speed/docs/best-practices/rules_intro)<!--@ provides additional tips for optimizing the network performance of your web page or application.-->
（网页性能最佳实践）提供了优化网页或应用程序网络性能的其他提示。

{{/partials.standard_devtools_article}}
