"""Shared menu identifiers for toolbar contributors."""

ADMIN_MENU_IDENTIFIER = "admin-menu"
"""
The *Site* menu (that usually shows the project's domain name, *example.com* by default).
``ADMIN_MENU_IDENTIFIER`` allows you to get hold of this object easily using
:meth:`cms.toolbar.toolbar.CMSToolbar.get_menu`.
"""
LANGUAGE_MENU_IDENTIFIER = "language-menu"
"""
The *Language* menu. ``LANGUAGE_MENU_IDENTIFIER`` allows you to get hold of this object
easily using :meth:`cms.toolbar.toolbar.CMSToolbar.get_menu`.
"""

HELP_MENU_IDENTIFIER = "help-menu"
"""
The *Help* menu. ``HELP_MENU_IDENTIFIER`` allows you to get hold of this object easily
using :meth:`cms.toolbar.toolbar.CMSToolbar.get_menu`.
"""
HELP_MENU_BREAK = "Help Menu Break"
ADMIN_SITES_BREAK = "Admin Sites Break"
ADMINISTRATION_BREAK = "Administration Break"
CLIPBOARD_BREAK = "Clipboard Break"
USER_SETTINGS_BREAK = "User Settings Break"
TOOLBAR_DISABLE_BREAK = "Toolbar disable Break"
SHORTCUTS_BREAK = "Shortcuts Break"
