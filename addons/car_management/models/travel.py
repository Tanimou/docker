from odoo import api, fields, models

class CarTravel(models.Model):
    _name="car.travel"
    _description="All information about your travel"
    #create a relation between travel and car
    car=fields.Many2one('car.car',string='Car',required=True)
    CarModel=fields.Char(related='car.CarModel')
    StartPoint=fields.Char('StartPoint',required=True)
    DestinationPoint=fields.Char('DestinationPoint',required=True)
    StartDate=fields.Datetime('StartDate',required=True)
    EndDate=fields.Datetime('EndDate',required=True)
    Duration=fields.Integer('Duration',required=True)
    #get NumPlace from car
    NumPlace=fields.Integer(related='car.NumPlace')
    Info=fields.Text('Info',required=True)
    State=fields.Selection([('booked','Booked'),('in_progress','In Progress'),('done','Done'),('cancelled','Cancelled')],default='booked',string='Status')
    
    def action_book(self):
        self.State='booked'
        return True
    def action_progress(self):
        self.State='in_progress'
        return True
    
    def action_terminate(self):
        self.State='done'
        return True
    
    def action_cancel(self):
        self.State='cancelled'
        return True
    