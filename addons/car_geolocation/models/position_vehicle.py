# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import ValidationError


class PositionVehicle(models.Model):
    _name = "position.vehicle"
    _description = "position vehicle"

    name = fields.Char(string="Conducteur")
    time_start = fields.Float(string="Heure de départ", default=4.324)
    time_end = fields.Float(string="Heure d'arrivée", default=20.124)



