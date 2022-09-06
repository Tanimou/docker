# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
{
    'name': 'Car Management',
    'version': '1.0.0',
    'summary': 'An application for car management',
    'description': """This module is an application for car management. It supports the following features:
    -Creation of cars""",
    'author': 'Progistack',
    'category': 'car',
    'sequence': -100,
    'depends': ['base','hr','contacts','mail','web'],
    'data': ['security/ir.model.access.csv','wizard/driverdetails.xml','views/menu.xml','views/FormView.xml','views/CalendarView.xml','views/carmap.xml'],#used to import all xml files
    'demo': [],#demo database
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {
    'web.assets_backend': ['car_management/web/static/src/js/main.18.js'],
  #  'web.assets_frontend': ['car_management/static/src/js/main.62.js'],

    
    },
    'license': 'LGPL-3',
}
