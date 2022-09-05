# -*- coding: utf-8 -*-
# from odoo import http


# class Document(http.Controller):
#     @http.route('/document/document', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/document/document/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('document.listing', {
#             'root': '/document/document',
#             'objects': http.request.env['document.document'].search([]),
#         })

#     @http.route('/document/document/objects/<model("document.document"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('document.object', {
#             'object': obj
#         })
