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
        # Disable schema compiler to generate model extension API code.
        # Only register the extension functions in extension system.
        'non_compiled_schema_files': [
          'adview.json',
          'browsing_data.json',
          'chromeos_info_private.json',
          'extension.json',
          'idltest.idl',
          'infobars.json',
          'media_player_private.json',
          'music_manager_private.idl',
          'principals_private.idl',
          'streams_private.idl',
          'top_sites.json',
        ],
        'conditions': [
          ['OS!="android"', {
            'schema_files': [
              'activity_log_private.json',
              'alarms.idl',
              'app_current_window_internal.idl',
              'app_runtime.idl',
              'app_window.idl',
              'audio.idl',
              'autotest_private.idl',
              'bluetooth.idl',
              'bookmark_manager_private.json',
              'bookmarks.json',
              'braille_display_private.idl',
              'cast_channel.idl',
              'cloud_print_private.json',
              'command_line_private.json',
              'content_settings.json',
              'context_menus.json',
              'cookies.json',
              'debugger.json',
              'desktop_capture.json',
              'developer_private.idl',
              'dial.idl',
              'dns.idl',
              'downloads.idl',
              'downloads_internal.idl',
              'echo_private.json',
              'enterprise_platform_keys_private.json',
              'events.json',
              'experimental_accessibility.json',
              'feedback_private.idl',
              'file_browser_private.idl',
              'file_system.idl',
              'file_system_provider.idl',
              'font_settings.json',
              'gcm.json',
              'hangouts_private.idl',
              'hid.idl',
              'history.json',
              'hotword_private.idl',
              'i18n.json',
              'identity.idl',
              'identity_private.idl',
              'idle.json',
              'image_writer_private.idl',
              'input_ime.json',
              'location.idl',
              'management.json',
              'manifest_types.json',
              'mdns.idl',
              'media_galleries.idl',
              'media_galleries_private.idl',
              'metrics_private.json',
              'networking_private.json',
              'notifications.idl',
              'omnibox.json',
              'page_capture.json',
              'permissions.json',
              'preferences_private.json',
              'power.idl',
              'push_messaging.idl',
              'reading_list_private.json',
              'runtime.json',
              'serial.idl',
              'sessions.json',
              'signed_in_devices.idl',
              'socket.idl',
              'sockets_tcp.idl',
              'sockets_tcp_server.idl',
              'sockets_udp.idl',
              'storage.json',
              'sync_file_system.idl',
              'system_cpu.idl',
              'system_display.idl',
              'system_indicator.idl',
              'system_memory.idl',
              'system_network.idl',
              'system_private.json',
              'system_storage.idl',
              'tab_capture.idl',
              'tabs.json',
              'terminal_private.json',
              'test.json',
              'types.json',
              'usb.idl',
              'virtual_keyboard_private.json',
              'web_navigation.json',
              'web_request.json',
              # Despite the name, this API does not rely on any
              # WebRTC-specific bits and as such does not belong in
              # the enable_webrtc=0 section below.
              'webrtc_audio_private.idl',
              'webrtc_logging_private.idl',
              'webstore_private.json',
              'webview.json',
              'windows.json',
            ],
          }, {  # OS=="android"
              'schema_files': [
                # These should be eliminated. See crbug.com/305852.
                'activity_log_private.json',
                'alarms.idl',
                'app_runtime.idl',
                'app_window.idl',
                'context_menus.json',
                'downloads.idl',
                'events.json',
                'feedback_private.idl',
                'file_system.idl',
                'manifest_types.json',
                'omnibox.json',
                'permissions.json',
                'runtime.json',
                'storage.json',
                'sync_file_system.idl',
                'tab_capture.idl',
                'tabs.json',
                'types.json',
                'web_navigation.json',
                'web_request.json',
                'windows.json',
              ],
          }],
          ['chromeos==1', {
            'schema_files': [
              'diagnostics.idl',
              'file_browser_handler_internal.json',
              'first_run_private.json',
              'log_private.idl',
              'screenlock_private.idl',
              'wallpaper.json',
              'wallpaper_private.json',
            ],
          }],
          ['enable_webrtc==1', {
            'schema_files': [
              'cast_streaming_rtp_stream.idl',
              'cast_streaming_session.idl',
              'cast_streaming_udp_transport.idl',
            ],
          }],
        ],
        'cc_dir': 'chrome/common/extensions/api',
        'root_namespace': 'extensions::api',
      },
      'dependencies': [
        '<(DEPTH)/skia/skia.gyp:skia',
        '<(DEPTH)/sync/sync.gyp:sync',
      ],
      'conditions': [
        ['chromeos==1', {
          'dependencies': [
            '<(DEPTH)/chrome/chrome.gyp:drive_proto',
          ],
        }],
      ],
    },
  ],
}
