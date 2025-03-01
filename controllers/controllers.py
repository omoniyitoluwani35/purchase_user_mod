# -*- coding: utf-8 -*-
# from odoo import http


# class PurchaseUserMod(http.Controller):
#     @http.route('/purchase_user_mod/purchase_user_mod', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/purchase_user_mod/purchase_user_mod/objects', auth='public')
#     def list(self, **kw):
#         return http.request.render('purchase_user_mod.listing', {
#             'root': '/purchase_user_mod/purchase_user_mod',
#             'objects': http.request.env['purchase_user_mod.purchase_user_mod'].search([]),
#         })

#     @http.route('/purchase_user_mod/purchase_user_mod/objects/<model("purchase_user_mod.purchase_user_mod"):obj>', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('purchase_user_mod.object', {
#             'object': obj
#         })

