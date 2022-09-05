# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class InheritFleetVehicle(models.Model):
    _inherit = "stock.picking"

    vehicle_id = fields.Many2one('fleet.vehicle', 'Véhicule', tracking=True)
    driver_id = fields.Many2one(related='vehicle_id.driver_id', string='Conducteur', tracking=True, copy=False)
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

    def action_in_progress(self):
        for rec in self:
            if not rec.vehicle_id:
                raise ValidationError("Veuillez assigner la livraison à un véhicule s'il vous plaît !")

            rec.active_validate_button = True
            rec.state = 'in_progress'

    def action_open_map_route(self):
        for rec in self:
            self.ensure_one()
            return {"type": "ir.actions.act_window", "res_model": "position.vehicle", "domain": [('id', '=', 1)], "name": "Route", 'view_mode': 'form'}

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
