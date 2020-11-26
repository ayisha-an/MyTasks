# -*- coding: utf-8 -*-
"""Ship object creation form in website"""
from odoo import http
from odoo.http import request


class WebsiteShipInfo(http.Controller):
    """Add ship information from website"""

    @http.route('/shipinfo', type='http', auth='public', website=True, sitemap=False)
    def ship_webform(self):
        """render ship object creation form when ship information menu item is clicked"""
        partners = request.env['res.partner'].search([])
        return http.request.render('sale_ship_information.createship_form', {
            'partners': partners
        })

    @http.route('/create/webship', type='http', auth='public', website=True, sitemap=False)
    def create_ship(self, **kwargs):
        """Create ship object and render a page with creation success message"""
        imo = kwargs['imo']
        ship = request.env['sale.ship_info'].search([])
        for each in ship:
            if each.imo == imo:
                return http.request.render('sale_ship_information.creation_failed', {})

            else:
                request.env['sale.ship_info'].create(kwargs)
                return http.request.render('sale_ship_information.creation_success', {})

