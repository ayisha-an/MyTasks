# -*- coding: utf-8 -*-
from odoo import http
from odoo.http import request


class WebsiteShipInfo(http.Controller):

    @http.route('/shipinfo', type='http', auth='public', website=True, sitemap=False)
    def ship_webform(self, **kwargs):
        partners = request.env['res.partner'].search([])
        return http.request.render('sale_ship_information.createship_form', {
            'partners': partners
        })

    @http.route('/create/webship', type='http', auth='public', website=True, sitemap=False)
    def create_ship(self, **kwargs):
        print('data', kwargs)
        request.env['sale.ship_info'].create(kwargs)
        return http.request.render('sale_ship_information.creation_success', {})
