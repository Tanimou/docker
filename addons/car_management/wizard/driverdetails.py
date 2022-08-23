from odoo import api, fields, models


class DriverDetails(models.TransientModel):
    _name='driver.wizard'
    _description='Wizard to see  driver"s details'
    
    EmployeeName=fields.Char('chauffeur')