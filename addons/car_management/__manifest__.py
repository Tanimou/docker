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
    'depends': ['base','hr','contacts'],
    'data': ['security/ir.model.access.csv','wizard/driverdetails.xml','views/menu.xml','views/FormView.xml','views/CalendarView.xml'],#used to import all xml files
    'demo': [],#demo database
    'installable': True,
    'auto_install': False,
    'application': True,
    'assets': {},
    'license': 'LGPL-3',
}
