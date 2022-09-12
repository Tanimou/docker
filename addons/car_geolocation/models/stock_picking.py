# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class InheritFleetVehicle(models.Model):
    _inherit = "stock.picking"

    vehicle_id = fields.Many2one('fleet.vehicle', 'Véhicule', tracking=True)
    driver_id = fields.Many2one(related='vehicle_id.driver_id', string='Conducteur', tracking=True, copy=False)
   # active_id = fields.Integer(compute="pick_active_id",string="Active id")
    latitude = fields.Float(related='vehicle_id.latitude', string='latitude initiale', tracking=True, copy=False)
    longitude = fields.Float(related='vehicle_id.longitude', string='longitude initiale', tracking=True, copy=False)
    latitudeF = fields.Float(related='vehicle_id.latitudeF', string='latitude finale', tracking=True, copy=False)
    longitudeF = fields.Float(related='vehicle_id.longitudeF', string='longitude finale', tracking=True, copy=False)
    active_validate_button = fields.Boolean(default=False)
    state = fields.Selection([
        ('draft', 'Draft'),
        ('waiting', 'Waiting Another Operation'),
        ('confirmed', 'Waiting'),
        ('assigned', 'Ready'),
        ('in_progress', 'En cours'),
        ('done', 'Done'),
        ('cancel', 'Cancelled'),
    ], string='Status', compute='_compute_state',
        copy=False, index=True, readonly=True, store=True, tracking=True,
        help=" * Draft: The transfer is not confirmed yet. Reservation doesn't apply.\n"
             " * Waiting another operation: This transfer is waiting for another operation before being ready.\n"
             " * Waiting: The transfer is waiting for the availability of some products.\n(a) The shipping policy is \"As soon as possible\": no product could be reserved.\n(b) The shipping policy is \"When all products are ready\": not all the products could be reserved.\n"
             " * Ready: The transfer is ready to be processed.\n(a) The shipping policy is \"As soon as possible\": at least one product has been reserved.\n(b) The shipping policy is \"When all products are ready\": all product have been reserved.\n"
             " * Done: The transfer has been processed.\n"
             " * Cancelled: The transfer has been cancelled.")
    # def pick_active_id(self):
    #     params=self._context.get('params')
    #  #   print(params)
    #     if  'id' in params:
    #       #  print("id:",params["id"],"menu_id:",params["menu_id"])
    #         self.active_id=params["id"]
    #       #  print(self.vehicle_id.name)
    #     else:self.active_id=self._context.get('active_id')
    #  #   if self.active_id in self.id:
       
    def action_in_progress(self):
        for rec in self:
            if not rec.vehicle_id:
                raise ValidationError("Veuillez assigner la livraison à un véhicule s'il vous plaît !")

            rec.active_validate_button = True
            rec.state = 'in_progress'
##Je me suis dit que le problème venait de la fonction action_open_map_route, mais je ne sais pas comment la modifier. Je pense que c'est ici qu'il faut appliquer les filtres ou le context un truc comme ça
    def action_open_map_route(self):
      
            return {
                "type": "ir.actions.act_window", 
                "res_model": "position.vehicle", 
                "name": "Route", 
                
                'view_mode': 'form',
               # 'context':{'id':self.active_id}
                }

    def button_validate(self):
        for rec in self:
            if not rec.vehicle_id and rec.picking_type_code == 'outgoing':
                raise ValidationError("Veuillez assigner la livraison à un véhicule s'il vous plaît !")
        super(InheritFleetVehicle, self).button_validate()

    @api.depends('state')
    def _compute_show_validate(self):
        for picking in self:
            if not (picking.immediate_transfer) and picking.state == 'draft':
                picking.show_validate = False
            elif picking.state not in ('draft', 'waiting', 'confirmed', 'assigned', 'in_progress'):
                picking.show_validate = False
            else:
                picking.show_validate = True
