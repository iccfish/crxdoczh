# Introduction #

Chromium's extension docs server 'server2' cannot be used without modification to serve translated docs. Not only does quota issues arise, but there are also other subtle issues. However, writing a complete new server from scratch is not feasible, either. The goal is to reuse as much of server2 as possible while serving the translated docs as well as (or even better than) the official docs in a stable way.


# Goals #

## Stability ##
This is the most important. The translation was (when this wiki was first created) originally hosted on Google Sites and there are no worries about service disruptions or quotas exceeded because of too many visitors. However, hosting on Google App Engine means that these issues must be taken into consideration.

## Consistency with the official documentation ##
It is almost impossible to maintain four different branches of docs in the original site hosted on Google Sites with reasonable effort. This is one important reason why it is migrated to Google App Engine. It is important to stay consistent with the official documentation so that visitors will not be confused and misled.

## Good or (hopefully) even better experience compared with the official documentation ##
There is no doubt that the new docs of Chrome Extensions provide much better experience to visitors that the old (build.py). We try to build the translation the same way and hope it will perform as well as the official docs.

Whenever possible, we will correct any broken links, legacy content, etc. in the official documentation and back port these fixes when appropriate and there is time.


# Proposed alternatives #

There are other alternative ways. For example, rendering all HTML pages locally and serving static content would be much easier.

## Prerendering and serving static content ##
This is the easiest. Running `preview.py -r <path>` is quite handy.

However, it was later discovered that generating docs took TOO MUCH time (several seconds to render only one page). It is possible to only render modified pages after merging a new patch from Chromium but it is not easy to determine which pages are modified. For example, any modifications in examples/ might lead to changes to a lot of API pages (Sample extensions that uses this API). Modifications in top level templates also suffers because it would take too much time to regenerate docs only for some small changes.

## Prerendering samples, serving other things dynamically ##
Fetching sample files consumes much resources since it requires a lot of urlfetches. It was tested that prerendering samples locally did not take much time.

## Using several servers to do different parts of the job ##
For example, rendering samples on one server (say, crxdoczh-samples.appspot.com), extensions/apps docs on a second (say crxdoczh-render.appspot.com) and serve requests on a third (our main server). Use memcache or data store to minimize resource usage and schudule updates periodically.

This sounds great but requires more effort to implement. However, it was decided that this approach was the most appropriate for the case, because:
  * TODO


# The main server #

The main server (master?) fetches pages from docs rendering server (slave-render?) and serves them to visitors. For best performance, it memcaches all rendered pages. To save outgoing bandwidth (free quota is only 1GB, but should be enough with the current number of page views every day), examples and images (or some images since images might also have a localized version) will be redirected to the corresponding URLs from the official server and there might be some method to reduce the size of rendered HTML pages (start working on these if quota is no longer enough in the future).


# The mirror server #

There must be at least one mirror for the time being in case the main server ran out of quota (most likely instance hours or outgoing bandwidth). It would be better if users were prompted or even automatically redirected (with a notice) to the mirror when such thing came. 'crxdoczh2' was chosen for the app id of the mirror.


# The rendering server #

It renders extensions/apps docs. To avoid abuse, the app id of the server is not disclosed and it requires a special API key to get access. Be careful before committing changes of the server (or hopefully checked with a presubmit script).

For testing, it still supports serving ordinary docs but requires admin login.

# The samples server #

It fetches samples from SVN and Github repositories, as samples\_data\_source.py does in server2. However, it returns JSON data of these samples and the rendering server use it directly. This server also requires an API key to access.

It is also possible (if quota is enough) that the two servers are served in one app to avoid duplicate urlfetches (both need to fetch api/**).**


TODO. Add more when have time