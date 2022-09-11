# -*- coding: utf-8 -*-

from email.policy import default
from odoo import models, fields, api, _
from odoo.exceptions import ValidationError

##j'ai copié le model stock.picking et j'ai ajouté le champ latitude et longitude, vu que le model stock.picking contient déja les informations du véhicule
class PositionVehicle(models.Model):
    _name = "position.vehicle"
    _inherit='stock.picking'
    _description = "position vehicle"
    
    vehicle_name = fields.One2many('stock.picking', 'vehicle_id', string="Vehicle ")
    time_start = fields.Float(string="Heure de départ", readonly=1)
    time_end = fields.Float(string="Heure d'arrivée")
    #name_vehicule=fields.Many2one("fleet.vehicle",string="Position",tracking=True)
    ##j'ai fait la relation entre le model position.vehicle et le model fleet.vehicle
    ##normalment il devrait aller chercher directement les informatios de latitude et longitude dans le model fleet.vehicule et les afficher correctement
    ##lorsque je les affiche sur la vue form du stock.picking, il me les affiche correctement. Mais lorsque je les affiche sur la vue form du position.##vehicle, il me les affiche pas
    latitude=fields.Float(compute="_find_lat_long",string="Latitude",copy=False)
   
    # latitude = fields.Float(related='vehicle_id.latitude', string='Conducteur', tracking=True, copy=False)
    longitude = fields.Float(compute="_find_lat_long",string="Longitude",copy=False)
    @api.depends("vehicle_name")
    def _find_lat_long(self):
        for rec in self:
          #  if (rec.vehicle_name.vehicle_id.latitude !=0.0):
                t=rec.env['stock.picking'].sudo().search([
                    ('vehicle_id', '=', rec.vehicle_name.vehicle_id.name),
                   
                ])
             #   f=rec.env['stock.picking'].sudo().search([])
                
             #   upd_var=self.env['stock.picking'].browse(active_id)
                
      #  upd_var=self.env['car.car'].browse(active_id)
               # for ff in f:
                  # if (self.active_id in ff.id):
                #      print("active_ff:",ff.id,"active_id:",self.vehicle_name.active_id,"Vehicle",ff.vehicle_id.name)
             #   print("rec:",rec.id)
                if(t.vehicle_id.name!="False"):
                    
                        rec.latitude=t.vehicle_id.latitude
                        rec.longitude=t.vehicle_id.longitude
                      #  print((rec.latitude,rec.longitude))