# This is just a temporary solution to the ever increasing redirects.json in
# docs/templates/public/.../redirects.json.
#
# Keep it updated with https://src.chromium.org/svn/trunk/src/chrome/common/extensions/docs/templates/public/{apps,extensions}/redirects.json
REDIRECTS = {
  '/apps/app_csp.html': '/apps/contentSecurityPolicy.html',
  '/apps/experimental_systemInfo_storage.html': '/apps/system_storage.html',
  '/apps/in_app_payments.html': '/apps/google_wallet.html',
  '/apps/index.html': '/apps/about_apps.html',
  '/apps/systemInfo_cpu.html': '/apps/system_cpu.html',
  '/apps/systemInfo_display.html': '/apps/system_display.html',
  '/apps/systemInfo_memory.html': '/apps/system_memory.html',
  '/apps/webview_tag.html': '/apps/tags/webview.html',
  '/extensions/experimental.debugger.html': '/extensions/debugger.html',
  '/extensions/experimental_debugger.html': '/extensions/debugger.html',
  '/extensions/experimental.infobars.html': '/extensions/infobars.html',
  '/extensions/experimental_infobars.html': '/extensions/infobars.html',
  '/extensions/experimental.systemInfo_storage.html': '/extensions/system_storage.html',
  '/extensions/experimental_systemInfo_storage.html': '/extensions/system_storage.html',
  '/extensions/systemInfo_cpu.html': '/extensions/system_cpu.html',
  '/extensions/systemInfo_memory.html': '/extensions/system_memory.html',
}
