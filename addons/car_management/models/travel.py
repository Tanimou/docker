from odoo import api, fields, models

class CarTravel(models.Model):
    _name="car.travel"
    _description="All information about your travel"
    #create a relation between travel and car
    car=fields.Many2one('car.car',string='Car',required=True)
    StartPoint=fields.Char('StartPoint',required=True)
    DestinationPoint=fields.Char('DestinationPoint',required=True)
    StartDate=fields.Datetime('StartDate',required=True)
    EndDate=fields.Datetime('EndDate',required=True)
    Duration=fields.Integer('Duration',required=True)
    #get NumPlace from car
    NumPlace=fields.Integer('NumPlace',required=True)