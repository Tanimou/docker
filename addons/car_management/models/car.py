from odoo import api, fields, models


class Carcar(models.Model):
    _name = 'car.car'
    _rec_name='CarModel'
    _description = "All information about your car"
    _inherit=['mail.thread','mail.activity.mixin']
    
    CarModel=fields.Char('CarModel',required=True)
    Manufacturer=fields.Char('Manufacturer',required=True)
    NumPlace=fields.Integer('NumPlace',required=True)
    FuelType=fields.Selection([('Diesel','Diesel'),('Gasoline','Gasoline'),('Hybrid','Hybrid'),('Electric','Electric')],string='FuelType',required=True)
    #create a relation between car and driver
    EmployeeName=fields.Many2one('hr.employee','Driver',required=False)
    image=fields.Image(string="Image",required=True)

    def detailchauffeuraction(self):
       
        return{
            'name':'Driver Details',
            'type':'ir.actions.act_window',
            'view_mode':'form',
            'res_model':'hr.employee',
            'res_id':self.EmployeeName.id,
            'target':'new'
          
        }
        
    def car_location(self):
        return{'type': 'ir.actions.act_url',
               #'url':'https://tanimou.github.io/carmapview/'
               'url':'localhost:8069/car_map',
               'target':'self'}