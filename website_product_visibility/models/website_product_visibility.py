# -*- coding: utf-8 -*-

from odoo import models, fields, api


class ProductVisibility(models.Model):
    _inherit = 'res.partner'

    filter_type = fields.Selection([
        ('all', 'All Products'),
        ('product_wise', 'Product Wise'),
        ('category_wise', 'Category Wise')], string='Filter Type', default='all')
    allowed_products = fields.Many2many('product.template', string='Allowed Products',
                                        domain="[('is_published', '=', True)]")
    allowed_categories = fields.Many2many('product.public.category', string='Allowed Product Categories')

    @api.onchange('filter_type')
    def onchange_filter_type(self):
        if self.filter_mode == 'all':
            self.allowed_products = None
            self.allowed_categories = None


