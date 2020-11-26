# -*- coding: utf-8 -*-

from odoo import models, fields


class Ship(models.Model):
    _name = 'sale.ship_info'
    _description = 'Ship Information'
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _rec_name = 'imo'

    imo = fields.Char(string="IMO", required=True)
    hull_no = fields.Char(string="Hull Number")
    engine_no = fields.Char(string="Engine Number")
    vessel_name = fields.Char(string="Vessel Name")
    build_year = fields.Char(string="Build Year")
    shipyard = fields.Many2one('res.partner', string="Shipyard")
    ship_owner = fields.Many2one('res.partner', string="Ship Owner")
    ship_management = fields.Many2one('res.partner', string="Ship Management")
    engine_builder = fields.Many2one('res.partner', string="Engine Builder")

    # _sql_constraints = [
    #     ('imo_unique', 'unique(imo)', "IMO already exists !")
    # ]


class ShipSaleOrder(models.Model):
    _inherit = 'sale.order'

    ship = fields.Many2one('sale.ship_info', string='Ship')

    # Update ship information to order lines
    def update_ship_info(self):
        self.order_line.ship = self.ship
        # print("Ship", self.ship)


class ShipSaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    ship = fields.Many2one('sale.ship_info', string='Ship')