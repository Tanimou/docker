# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class InheritFleetVehicle(models.Model):
    _inherit = "fleet.vehicle"

    delivery_end = fields.Char(string='Livraison en cours', compute="_compute_delivery", default="Aucune")
    marker_color = fields.Char(string='Marqueur', default='red', required=True)
    latitude = fields.Float(string='Latitude Initiale', digits=(10, 7))
    longitude = fields.Float(string='Longitude Initiale', digits=(10, 7))
    latitudeF = fields.Float(string='Latitude Finale', digits=(10, 7))
    longitudeF = fields.Float(string='Longitude Finale', digits=(10, 7))
    vehicle_type_id = fields.Many2one('vehicle.type', 'Type de véhicule', tracking=True)
    delivery_ids = fields.One2many('stock.picking', 'vehicle_id', string="Livraisons")
    delivery_count = fields.Integer(compute="_compute_delivery", string='Compteur livraison', copy=False, default=0,
                                    store=True)
    date_localization = fields.Datetime(string="Date", default=fields.Datetime.now)

    @api.depends("delivery_ids")
    def _compute_delivery(self):
        for rec in self:
            rec.delivery_count = len(rec.delivery_ids.ids)
            search_delivery = None
            if len(rec.delivery_ids.ids) > 0:
                search_delivery = rec.env['stock.picking'].sudo().search([
                    ('id', 'in', rec.delivery_ids.ids),
                    ('state', '=', 'in_progress')
                ], limit=1)
                rec.delivery_end = search_delivery.name
            else:
                rec.delivery_end = 'Aucun'
                search_delivery = None

    def action_open_map(self):
        for rec in self:
            return {"type": "ir.actions.act_window", "res_model": "fleet.vehicle", "domain": [('id', '=', rec.id)], 'name': _(f'Localisation : {rec.name}'), 'view_mode': 'google_map,kanban,tree,form'}

    def action_return_delivery(self):
        self.ensure_one()
        return {"type": "ir.actions.act_window", "res_model": "stock.picking", "domain": [('picking_type_code', '=', 'outgoing'), ('vehicle_id', '=', self.id)], "name": "Livraison", 'view_mode': 'calendar,tree,kanban,form'}

    def test_call(self):
        pass
        # print('HEllo Martin')
        # oder = self.env['fleet.vehicle'].sudo().search([])
