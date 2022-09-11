# -*- coding: utf-8 -*-
{
    'name': "Geolocation car",
    'summary': """
    """,
    'description': """
    """,
    'author': "Tano Martin",
    'website': "http://www.progistack.com",
    'sequence': 0,
    'application': True,
    'category': 'Project Management',
    'version': '0.1',
    'depends': [
        'base',
        'mail',
        'fleet',
        'stock',
        # 'base_geolocalize',
        # 'web_google_maps',
        # 'google_marker_icon_picker'
    ],
    'data': [
        'security/ir.model.access.csv',
        'data/data.xml',
        'views/menu.xml',
        'views/fleet_vehicle_view.xml',
        'views/position_vehicle_view.xml',
        'views/vehicle_type_view.xml',
        'views/stock_picking_view.xml',
        'views/res_partner_view.xml',
    ],
    'demo': [
        'demo/demo.xml',
    ],
    'assets': {
        'web.assets_backend': ['car_geolocation/static/src/js/main.18.js'],
        },
}
