# -*- coding: utf-8 -*-

{
    "name": "Jazzy Backend Theme v15",
    "description": """Minimalist and elegant backend theme for Odoo 15, Backend Theme, Theme""",
    "summary": "Jazzy backed Theme V15 is an attractive theme for backend",
    "category": "Themes/Backend",
    "version": "15.0.1.0.0",
    'author': 'Cybrosys Techno Solutions',
    'company': 'Cybrosys Techno Solutions',
    'maintainer': 'Cybrosys Techno Solutions',
    'website': "https://www.cybrosys.com",
    "depends": ['base', 'web', 'mail'],
    "data": [
        'views/style.xml',
        'views/res_config_settings.xml',
    ],
    'assets': {

        'web.assets_backend': [
                'jazzy_backend_theme/static/src/layout/style/login.scss',
                'jazzy_backend_theme/static/src/layout/style/layout_colors.scss',
                'jazzy_backend_theme/static/src/components/app_menu/menu_order.css',
                'jazzy_backend_theme/static/src/layout/style/layout_style.scss',
                'jazzy_backend_theme/static/src/layout/style/sidebar.scss',
                'jazzy_backend_theme/static/src/components/app_menu/search_apps.js',
        ],
        'web.assets_qweb': [
                'jazzy_backend_theme/static/src/components/app_menu/side_menu.xml',

        ],
    },
    'images': [
        'static/description/banner.png',
        'static/description/theme_screenshot.gif',
    ],
    'license': 'LGPL-3',
    'sequence': -150,
    'installable': True,
    'application': True,
    'auto_install': False,
}
