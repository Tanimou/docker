from odoo import api, fields, models


class Carcar(models.Model):
    _name = 'car.car'
    _description = "All information about your car"

    CarModel=fields.Char('CarModel',required=True)
    Manufacturer=fields.Char('Manufacturer',required=True)
    NumPlace=fields.Integer('NumPlace',required=True)
    FuelType=fields.Selection([('Diesel','Diesel'),('Gasoline','Gasoline'),('Hybrid','Hybrid'),('Electric','Electric')],string='FuelType',required=True)
    #create a relation between car and driver
    EmployeeName=fields.Many2one('hr.employee','Driver',required=True)
