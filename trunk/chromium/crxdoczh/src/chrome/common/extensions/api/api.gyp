# Copyright (c) 2012 The Chromium Authors. All rights reserved.
# Use of this source code is governed by a BSD-style license that can be
# found in the LICENSE file.

{
  'targets': [
    {
      'target_name': 'api',
      'type': 'static_library',
      'sources': [
        '<@(schema_files)',
      ],
      # TODO(jschuh): http://crbug.com/167187 size_t -> int
      'msvs_disabled_warnings': [ 4267 ],
      'includes': [
        '../../../../build/json_schema_bundle_compile.gypi',
        '../../../../build/json_schema_compile.gypi',
      ],
      'variables': {
        'chromium_code': 1,
        'schema_files': [
          'alarms.idl',
          'activity_log_private.json',
          'adview.json',
          'app_current_window_internal.idl',
          'app_runtime.idl',
          'app_window.idl',
          'audio.idl',
          'autotest_private.idl',
          'bluetooth.idl',
          'bookmark_manager_private.json',
          'bookmarks.json',
          'braille_display_private.idl',
          'browsing_data.json',
          'chromeos_info_private.json',
          'cloud_print_private.json',
          'command_line_private.json',
          'content_settings.json',
          'context_menus.json',
          'cookies.json',
          'debugger.json',
          'developer_private.idl',
          'desktop_capture.idl',
          'diagnostics.idl',
          'dial.idl',
          'dns.idl',
          'downloads.idl',
          'echo_private.json',
          'downloads_internal.idl',
          'enterprise_platform_keys_private.json',
          'events.json',
          'experimental_accessibility.json',
          'experimental_discovery.idl',
          'experimental_history.json',
          'experimental_identity.idl',
          'file_browser_private.json',
          'location.idl',
          'system_memory.idl',
          'extension.json',
          'feedback_private.idl',
          'file_browser_handler_internal.json',
          'file_system.idl',
          'font_settings.json',
          'history.json',
          'i18n.json',
          'identity.idl',
          'identity_private.idl',
          'idle.json',
          'idltest.idl',
          'infobars.json',
          'input_ime.json',
          'log_private.idl',
          'management.json',
          'manifest_types.json',
          'mdns.idl',
          'media_galleries.idl',
          'media_galleries_private.idl',
          'media_player_private.json',
          'metrics_private.json',
          'music_manager_private.idl',
          'networking_private.json',
          'notifications.idl',
          'omnibox.json',
          'page_capture.json',
          'permissions.json',
          'preferences_private.json',
          'power.idl',
          'push_messaging.idl',
          'image_writer_private.idl',
          'runtime.json',
          'serial.idl',
          'sessions.json',
          'signed_in_devices.idl',
          'socket.idl',
          'sockets_udp.idl',
          'storage.json',
          'sync_file_system.idl',
          'system_indicator.idl',
          'system_cpu.idl',
          'system_display.idl',
          'system_storage.idl',
          'system_private.json',
          'tab_capture.idl',
          'tabs.json',
          'terminal_private.json',
          'test.json',
          'top_sites.json',
          'usb.idl',
          'virtual_keyboard_private.json',
          'wallpaper.json',
          'wallpaper_private.json',
          'web_navigation.json',
          'web_request.json',
          'webstore_private.json',
          'webview.json',
          'windows.json',
        ],
        'cc_dir': 'chrome/common/extensions/api',
        'root_namespace': 'extensions::api',
      },
      'dependencies': [
        '<(DEPTH)/skia/skia.gyp:skia',
        '<(DEPTH)/sync/sync.gyp:sync',
      ],
      'conditions': [
        ['OS=="android"', {
          'sources!': [
            'autotest_private.idl',
            'bookmark_manager_private.json',
            'browsing_data.json',
            'chromeos_info_private.json',
            'command_line_private.json',
            'developer_private.idl',
            'dial.idl',
            'downloads_internal.idl',
            'echo_private.json',
            'enterprise_platform_keys_private.json',
            'experimental_accessibility.json',
            'experimental_discovery.idl',
            'experimental_dns.idl',
            'experimental_history.json',
            'experimental_identity.idl',
            'experimental_idltest.idl',
            'extension.json',
            'file_browser_handler_internal.json',
            'font_settings.json',
            'i18n.json',
            'identity.idl',
            'identity_private.idl',
            'idle.json',
            'infobars.json',
            'input_ime.json',
            'media_player_private.json',
            'music_manager_private.idl',
            'networking_private.json',
            'power.idl',
            'system_indicator.idl',
            'system_private.json',
            'terminal_private.json',
            'test.json',
            'top_sites.json',
            'webview.json',
          ],
        }],
        ['OS!="chromeos"', {
          'schema_files!': [
            'file_browser_handler_internal.json',
            'log_private.idl',
            'virtual_keyboard_private.json',
            'wallpaper.json',
            'wallpaper_private.json',
          ],
        }],
      ],
    },
  ],
}
