# -*- coding: utf-8 -*-
import urllib,os
from email.policy import default
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

##j'ai copié le model stock.picking et j'ai ajouté le champ latitude et longitude, vu que le model stock.picking contient déja les informations du véhicule
class PositionVehicle(models.Model):
    _name = "position.vehicle"
  
    _description = "position vehicle"
    
    vehicle_name = fields.One2many('stock.picking', 'vehicle_id', string="Vehicle ")
    time_start = fields.Float(string="Heure de départ", readonly=1)
    time_end = fields.Float(string="Heure d'arrivée")
    #name_vehicule=fields.Many2one("fleet.vehicle",string="Position",tracking=True)
    ##j'ai fait la relation entre le model position.vehicle et le model fleet.vehicle
    ##normalment il devrait aller chercher directement les informatios de latitude et longitude dans le model fleet.vehicule et les afficher correctement
    ##lorsque je les affiche sur la vue form du stock.picking, il me les affiche correctement. Mais lorsque je les affiche sur la vue form du position.##vehicle, il me les affiche pas
   

   