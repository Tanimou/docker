from odoo import api, fields, models

class CarTickets(models.Model):
    _name = 'car.ticket'
    _description = "All information about your ticket"
    

    ClientName=fields.Many2one('res.partner','Client Name',required=True)
    Info=fields.Many2one('car.travel','Info',required=True)
    Date=fields.Date('Date',required=True)
    Price=fields.Integer('Price',required=True)
    Car=fields.Many2one('car.car','Car',required=True)
    DestinationPoint=fields.Char(related='Info.DestinationPoint')
    StartTime=fields.Datetime('StartTime',required=True)
 