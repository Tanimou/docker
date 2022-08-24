from odoo import api, fields, models


class DriverDetails(models.TransientModel):
    _name='driver.wizard'
    _description='Wizard to see  driver"s details'
    
    EmployeeName=fields.Many2one('hr.employee','Driver',required=True)
    #CarModel=fields.Many2one('car.car','Car',required=True)
   # @api.onchange('EmployeeName')
    def changedriver(self):
        active_id=self._context.get('active_id')
        upd_var=self.env['car.car'].browse(active_id)
        vals={'EmployeeName':self.EmployeeName}
        upd_var.write(vals)
        return {'type': 'ir.actions.client',
                'tag': 'reload'}
        #   self.EmployeeName=self.EmployeeName
    """
    def changecar(self):
        active_id=self._context.get('active_id')
        upd_var=self.env['car.car'].browse(active_id)
        vals={'CarModel':self.CarModel}
        upd_var.write(vals)
        return {'type': 'ir.actions.client',
                'tag': 'reload'}
                """
   