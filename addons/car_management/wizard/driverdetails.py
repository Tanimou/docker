from odoo import api, fields, models


class DriverDetails(models.TransientModel):
    _name='driver.wizard'
    _description='Wizard to see  driver"s details'
    
    EmployeeName=fields.Many2one('hr.employee','Driver',required=False)
    CarModel=fields.Many2one('car.car','Car',required=False)
    Manufacturer=fields.Many2one('car.car','Car',required=False)
    NumPlace=fields.Many2one('car.car','Car',required=False)
    FuelType=fields.Many2one('car.car','Car',required=False)
    image=fields.Many2one('car.car','Car',required=False)
    #CarModel2=fields.Char(related='car.CarModel')
   # @api.onchange('EmployeeName')
    def changedriver(self):
        active_id=self._context.get('active_id')
        upd_var=self.env['car.car'].browse(active_id)
        vals={'EmployeeName':self.EmployeeName}
        upd_var.write(vals)
        return {'type': 'ir.actions.client',
                'tag': 'reload'}
        #   self.EmployeeName=self.EmployeeName
    def changecar(self):
        active_id=self._context.get('active_id')
        upd_var=self.env['car.car'].browse(active_id)
        upd_var2=self.env['car.travel'].browse(active_id)
        vals2={'CarModel':self.CarModel.CarModel}
        vals={'CarModel':self.CarModel.CarModel,'Manufacturer':self.CarModel.Manufacturer,'NumPlace':self.CarModel.NumPlace,'FuelType':self.CarModel.FuelType,'image':self.CarModel.image}
           
        upd_var.write(vals)
        upd_var2.write(vals2)
        return {'type': 'ir.actions.client',
                'tag': 'reload'}
                
   