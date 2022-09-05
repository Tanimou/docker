# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class InheritResPartner(models.Model):
    _inherit = "res.partner"

    delivery_ids = fields.One2many('stock.picking', 'driver_id', string="Livraison")
    delivery_count = fields.Integer(compute="_compute_delivery", string='Compteur livraison', copy=False, default=0,
                                    store=True)

    @api.depends("delivery_ids")
    def _compute_delivery(self):
        for rec in self:
            rec.delivery_count = len(rec.delivery_ids.ids)

    def action_return_delivery(self):
        self.ensure_one()
        return {"type": "ir.actions.act_window", "res_model": "stock.picking", "domain": [('picking_type_code', '=', 'outgoing'), ('driver_id', '=', self.id)], "name": "Livraison", 'view_mode': 'tree,calendar,kanban,form'}
