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
    'depends': [],
    'data': ['views/menu.xml','views/viewscardetails.xml','views/viewsticketdetails.xml','views/viewstraveldetails.xml'],#used to import all xml files
    'demo': [],#demo database
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}
