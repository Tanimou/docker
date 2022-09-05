from odoo import http
from odoo.http import request

class CarMap(http.Controller):
    @http.route('/car_map', auth='public', website=True)
    def index(self, **kw):
        return http.request.render('car_management.car_map', {})