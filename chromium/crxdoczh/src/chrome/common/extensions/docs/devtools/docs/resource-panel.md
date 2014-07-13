{{+bindTo:partials.standard_devtools_article}}

# <!--@Managing application storage-->管理应用程序存储

<!--@The Resources panel lets you inspect your application's local data sources, including IndexedDB or Web SQL databases, local and session storage, cookies, and Application Cache resources. You can also quickly inspect your application's visual resources, including images, fonts and and style sheets.-->Resources（资源）面板允许您审查应用程序的本地数据源，
包括 IndexedDB 或 Web SQL 数据库、本地和会话存储、Cookie 和
应用程序缓存资源。您还可以迅速审查应用程序的可视资源，包括图片、字体和样式表。


<!--@The Resources panel reveals your application's local data stores, including IndexedDB and WebSQL databases, local and session storage, cookies and Application Cache resources. -->
资源面板反映了应用程序的本地数据存储，包括 IndexedDB 和 WebSQL 数据库、
本地和会话存储、Cookie 和应用程序缓存资源。

## IndexedDB

<!--@You can inspect IndexedDB databases and object stores, page through an object store's records, and clear an object store of its records.-->
您可以审查 IndexedDB 数据库和对象存储区，翻阅对象存储区的记录，还能清除
对象存储区中的记录。

* **<!--@To view a list of available database-->如果要查看可用数据库列表**<!--@, expand the IndexedDB category.-->
，请展开 IndexedDB 分类。
* **<!--@To view a database's object stores-->如果要查看数据库的对象存储区**<!--@, select it from the list of available databases.-->
，请从可用数据库列表中选择。

<img src="resources-files/indexeddb.png"/> 

**<!--@To page through records in the object store-->如果要翻阅对象存储区中的记录**<!--@, click the Previous and Next page buttons. You can also specify the record where paging starts by specifying the record's key.-->
，请单击 Previous（上一页）和 Next（下一页）按钮。您还可以通过记录键指定从哪条记录开始浏览。

<img src="resources-files/next-previous-page.png"/>

**<!--@To clear the object store-->如果要清除对象存储区**<!--@, do one of the following:-->
，请使用以下某种方式：

* <!--@Click the-->单击面板底部的 **Clear object store**<!--@ button-->
（清除对象存储区）按钮 <img src="../images/clear.png" /><!--@ at the bottom of the panel.-->。
* <!--@Right-click or Control-click the object store and select **Clear** from the context menu.-->
右键单击或按住 Control 键单击（Mac）对象存储区，并选择右键菜单中的 **Clear**
（清除）。

**<!--@To view properties of a database-->如果要查看数据库属性**<!--@, select it from the list of databases.-->
，请从数据库列表中选择。

<img src="resources-files/database-properties.png"/> 

## Web SQL

<!--@You can inspect the content of Web SQL databases, and run SQL commands against 
their contents.-->
您可以审查 Web SQL 数据库的内容，还能针对内容运行 SQL 命令。

* **<!--@To view the available Web SQL databases-->要查看可用的 Web SQL 数据库**<!--@, expand the Web SQL item in the tree control.-->
，请展开树形控件中的 Web SQL 项。
* **<!--@To view available tables in a database-->要查看数据库中可用的表格**<!--@, expand the database tree item.-->
，请展开数据库项。
* **<!--@To view a table's records-->要查看表格记录**<!--@, select the table. It's properties appear in the right-hand pane.-->
，请选择表格，它的属性就会显示在右侧窗格中。
* **<!--@To refresh the view of the database-->要刷新数据库视图**<!--@, click the Refresh button-->
，请单击面板底部的 Refresh（刷新）按钮 <img src="../images/refresh.png" /><!--@ at the bottom of the panel. -->。

<!--@You can query a Web SQL database's tables with SQL commands and view 
query results in a tabular format. As you type out a command or table name, code hints are provided for the names of supported SQL commands and clauses, and the names of tables that the database contains.-->
您可以使用 SQL 命令查询 Web SQL 数据库表，并以表格形式查看查询结果。当您输入
命令或表格名称时，会有代码提示，提供支持的 SQL 命令和语句名称，以及数据库
包含的表格名称。

**<!--@To run a SQL command against a database-->如果要针对数据库运行 SQL 命令**<!--@:-->：

1. <!--@Select the database containing the table you want to query.-->
选择您要查询的表格所在的数据库。
2. <!--@At the prompt that appears in the right-hand panel, enter the SQL statement you want to execute.-->
在右侧面板中出现的提示符下输入您想要执行的 SQL 语句。

<img src="resources-files/sql.png" />

## Cookie<!--@s-->

<!--@You can view detailed information about cookies that have been created by an HTTP header or with JavaScript. You can also clear individual cookies, groups of cookies from the same origin, or clear all cookies from a specific domain.-->
您可以查看通过 HTTP 标头或使用 JavaScript 创建的 Cookie 详情，
您还可以清除某些 Cookie、分组查看同一来源的 Cookie，或清除指定域名下
所有的 Cookie。

<img src="resources-files/cookies.png" />

<!--@When you expand the Cookies category, it displays a list of domains of the main document and those of all loaded frames. Selecting one of these "frame groups" displays all cookies, for all resources, for all frames in that group. There are two consequences of this grouping to be aware of:-->
当您展开 Cookies 分类时，它会显示主文档及所有加载框架的域名列表，
从这些“框架组”中选择其中一个，就会显示对应分组中所有资源、所有框架的 Cookie。
这样的分组方式有两点需要注意：

* <!--@Cookies from different domains may appear in the same frame group. -->
来自不同域名的 Cookie 可能会显示在同一框架组中。
* <!--@The same cookie may appear in several frame groups.-->
同样的 Cookie 可能会出现在多个框架组中。

<!--@The following fields are displayed for each cookie in the selected frame group:-->
选定框架组中的每一个 Cookie 都会显示以下字段：

* **Name**<!--@ — The cookie's name.-->——Cookie 名称。
* **Value**<!--@ — The cookie's value.-->——Cookie 值。
* **Domain**<!--@ — The domain that the cookie applies to.-->——Cookie 应用于哪个域名。
* **Path**<!--@ — The path that the cookie applies to.  -->——Cookie 应用于什么路径。
* **Expires / Maximum Age**<!--@— The cookie's expiration time, or maximum age. For session cookies, this field is always "Session".-->——Cookie 的过期时间或最长周期，如果是会话 Cookie，该字段始终为“Session”。
* **Size**<!--@ — The size of the cookie's data in bytes.-->——Cookie 数据大小，以字节为单位。
* **HTTP**<!--@ — If present, indicates that cookies should be used only over HTTP, and JavaScript modification is not allowed.-->——如果存在，表示该 Cookie 只能通过 HTTP 使用，不允许通过 JavaScript 修改。
* **Secure**<!--@ — If present, indicates that communication for this cookie must be over an encrypted transmission.-->——如果存在，表示该 Cookie 必须通过加密的传输协议传递。

<!--@You can clear (delete) a single cookies, all cookies in the selected frame group, or cookies from a specific domain. Recall the same cookie may appear in more than one frame group, as discussed previously. If the same cookie for a given domain is referenced in two frame groups, deleting all cookies for that domain will affect both groups.-->
您可以清除（删除）单个 Cookie、选定框架组中的所有 Cookie 或
来自某个域名的 Cookie。回忆一下，前面说过同样的 Cookie 可能会出现在一个以上
的框架组中。如果指定域名的同一个 Cookie 在两个框架组中引用，删除来自该域名
的 Cookie 会影响这两个框架组。

**<!--@To clear a single cookie-->要删除某一个 Cookie**<!--@, do one of the following:-->，请使用以下某种方式：

* <!--@Select a cookie in the table and click the Delete button at the bottom of the panel.-->
选择表格中的 Cookie，并单击面板底部的 Delete（删除）按钮。
* <!--@Right-click on a cookie and select Delete.-->
右键单击 Cookie 并选择 Delete（删除）。

**<!--@To clear all cookies from the selected frame group-->要删除选定框架组中的所有 Cookie**<!--@, do one of the following:-->，请使用以下某种方式：

* <!--@Click the Clear button-->单击资源面板底部的 Clear（清除）按钮 <img src="../images/clear.png" /><!--@ at the bottom of the Resources panel.-->。
* <!--@Right-click on the frame group and select **Clear** from the context menu.-->右键单击框架组，并选择右键菜单中的 **Clear**（清除）。
* <!--@Right-click on a cookie row in the table and select **Clear All**.-->
右键单击表格中的 Cookie 行，并选择 **Clear All**（全部删除）。

**<!--@To clear all cookies from a specific domain:-->要清除来自指定域名的所有 Cookie：**

1. <!--@Right+click (or Ctrl+click) a cookie in the table from the target domain.-->右键单击（或者在 Mac 中 Ctrl+单击）表格中来自目标域名的 Cookie。
2. <!--@From the context menu, seect **Clear All from _domain_**, where 
   _domain_ is the target domain. -->
选择右键菜单中的 **Clear All from _domain_**（清除来自
_域名_
的所有数据），其中 _domain_ 为目标域名。

<img src="resources-files/clear-all-cookies.png" />

<!--@Note the following about this operation:-->
进行该操作时请注意以下几点：

* <!--@Only cookies with exactly the same domain name are removed; sub- and top-level domains are unaffected. -->
只有域名完全相同的 Cookie 才会删除，子域名和顶级域名不会受到影响。
* <!--@It only works on domains visible in the cookies table.-->
只有 Cookie 表格中可见的域名才能使用该功能。

<!--@You can also refresh the table to reflect any changes to the page's cookies.-->
您还可以刷新表格，显示网页 Cookie 的更改。

**<!--@To refresh the cookies table-->要刷新 Cookie 表格**<!--@, click the refresh button-->，请单击资源面板底部的 Refresh（刷新）按钮 <img 
src="../images/refresh.png" /><!--@ at the bottom of the Resources panel. -->
。

## <!--@Application Cache-->应用程序缓存

<!--@You can examine resources that Chrome has cached according to the Application Cache manifest file specified by the current document. You can view the current status of the Application Cache (idle or downloading, for 
example), and the browser's connection status (online or offline).-->
您可以审查 Chrome 浏览器根据当前文档指定的应用程序缓存清单文件缓存的资源，
您可以查看应用程序缓存的当前状态（例如空闲或正在下载等）以及浏览器的连接状态
（在线或离线）。
<br/>
<img src="resources-files/app-cache.png" /> 

<!--@The table of cached resources includes the following properties for each resource:-->
缓存的资源列表中包含以下属性：

* **Resource**<!--@ — The URL of the resource.-->（资源）——资源 URL。
* **Type**<!--@ — The type of cached resource, which can have one of the following 
  values:-->
（类型）——缓存的资源类型，可以是下列值之一：
    * **Master**<!--@ — The resource was added to the cache because it's -->
    ——资源添加到缓存，因为
      [manifest](http://www.whatwg.org/specs/web-apps/current-work/multipage/semantics.html#attr-html-manifest) 
      <!--@attribute indicated that this was its cache.-->
      表示这是它的缓存。
    * **Explicit**<!--@ — The resource was explicitly listed in the application's 
      cache manifest file.-->
      ——资源在应用程序缓存清单文件中显式列出。
    * **Network**<!--@ — The resources was listed in the application's cache manifest 
      file as a network entry. -->
      ——资源在应用程序缓存清单文件中以网络项的形式列出。
    * **Fallback**<!--@ — The resource was specified as a fallback if a resource is inaccessible.-->
    ——如果无法访问资源，则使用缓存作为后备。
* **Size**<!--@ — Size of the cached resource.-->
——缓存资源的大小。

<!--@The Resources panel displays the current -->
资源面板显示应用程序缓存的当前[<!--@status-->状态](http://www.whatwg.org/specs/web-apps/current-work/#dom-appcache-status) 
<!--@of the application cache along with a colored status icon (green, yellow, or red). The following are the possible status values and their descriptions:-->
，再加上彩色的状态图标（绿色、黄色或红色）。以下是可能的状态值及其描述：

<!-- TODO: Fix formatting of cells -->
<table>
<tr>
<td><!--@Status-->状态</td>
<td><!--@Description-->描述</td>
</tr>
<tr>
<td><img src="resources-files/green.png"/> IDLE </td>
<td><!--@The application cache is idle.-->应用程序缓存处于空闲状态。</td>
</tr>
<tr>
<td><img src="resources-files/yellow.png"/>CHECKING </td>
<td><!--@The manifest is being fetched and checked for updates.-->正在获取清单文件，检查更新。</td>
</tr>
<tr>
<td><img src="resources-files/yellow.png"/>DOWNLOADING </td>
<td><!--@Resources are being downloaded to be added to the cache, due to a changed resource manifest.-->由于资源清单文件更改，正在下载资源并添加到缓存中。</td>
</tr>
<tr>
<td><img src="resources-files/green.png"/>UPDATEREADY </td>
<td><!--@There is a new version of the application cache available. -->应用程序缓存的新版本可用。</td>
</tr>
<tr>
<td><img src="resources-files/red.png"/>OBSOLETE </td>
<td><!--@The application cache group is obsolete.-->应用程序缓存组已过时。</td>
</tr>
</table>

## <!--@Local and session storage-->本地和会话存储

<!--@You can view and edit local and session storage key/value pairs you've created using the [Web Storage APIs](http://www.w3.org/TR/webstorage/). You can edit, delete, and create both local and session storage data.-->
您可以查看和编辑使用[网络存储 API](http://www.w3.org/TR/webstorage/)
创建的本地和会话存储键/值对，可以编辑、删除和创建本地和会话存储数据。

**<!--@To delete a key/value pair-->如果要删除键/值对**<!--@, do one of the following:-->，请使用以下某种方式：

* <!--@Select the item in the data table and do one of the following:-->
选择数据表中的项目，并使用以下某种方式：
    2. <!--@Click the Delete button.-->单击 Delete（删除）按钮。
    3. <!--@Press the Delete key on your keyboard.-->按下键盘上的 Delete 键。
* <!--@Right-click or Control-click on the data item and choose Delete from the context menu.-->
右键单击或按住 Control 键单击（Mac）数据项，并从右键菜单中选择 Delete（删除）。

**<!--@To add a new key/value pair:-->如果要添加新的键/值对：**

1. <!--@Double-click inside an empty Key table cell and enter the key name.-->
双击表格中空的键单元格，并输入键的名称。
2. <!--@Double-click inside the corresponding Value table cell and enter the key's value.-->
双击表格中对应的值单元格，并输入键值。

**<!--@To edit an existing key/value pair-->如果要编辑现有的键/值对**<!--@, do one of the following:-->，请使用以下某种方式：

* <!--@Double-click in the cell you want to edit.-->
双击您需要编辑的单元格。
* <!--@Right-click or Control-click the cell you want to edit and choose Edit from the context menu.-->
右键单击或按住 Control 键单击（Mac）您需要编辑的单元格，并从右键菜单中
选择 Edit（编辑）。

**<!--@To refresh the table with new storage data-->如果要刷新表格显示新的存储数据**<!--@, click the Refresh button at the bottom of the panel.-->
，单击面板底部的 Refresh（刷新）按钮 
<img src="../images/refresh.png" />
。

# <!--@Inspecting page resources-->审查网页资源

<!--@You can view all of your main document's resources, including images, scripts, and fonts, and those of any loaded frames. The top level category of page resources are the document's frames, which includes the main document, and its embedded frames.-->
您可以查看主文档以及加载框架的所有资源，包括图片、脚本和字体。
网页资源的顶层分类是文档的框架，包括主文档以及内嵌的框架。

<img src="resources-files/frame-resources.png" />

<!--@You can expand a frame to view its resources organized by type, expand a type to view all resources of that type, and select a resource to preview it in the panel on the right. Below is a preview of a font resource.-->
您可以展开框架，根据类型查看对应资源，展开某种类型查看对应类型的所有资源，
选中某个资源还可以在右侧面板预览它。如下是某个字体资源的预览。

<img src="resources-files/font-resource.png" />

<!--@Image previews include the dimensions, file size, MIME type, and URL of the image.-->
图片的预览包括尺寸、文件大小、MIME 类型以及图片 URL。

<img src="resources-files/image-inspect.png" />

<!--@Other tips:-->
其他提示：

* **<!--@To open a resource in the Network panel-->如果要在网络面板中打开资源**<!--@, right-click or control-click the resource and select **Reveal In Resources Panel**. From the same menu you can copy the resource's URL to the system clipboard, or open it in a new browser tab.-->
，右键单击或按住 Control 键单击（Mac）资源，选择 **Reveal In Network Panel**
（在网络面板中显示）。从同样的菜单中您还可以把资源 URL 复制到系统剪贴板，
或者在新的浏览器标签页中打开它。

<img src="resources-files/reveal-in-network.png" />

* **<!--@To view the bounding box of an embedded frame-->如果要查看内嵌框架的范围**<!--@, hover your mouse over a frame in the Resources panel:-->
，将鼠标悬停在资源面板中的某个框架上：

<img src="resources-files/frame-selected.png" />
{{/partials.standard_devtools_article}}
