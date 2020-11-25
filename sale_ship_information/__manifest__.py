# -*- coding: utf-8 -*-
{
    'name': "Ship Information",
    'summary': """Shipping Information""",
    'description': """Details of ship""",
    'author': "My Company",
    'license': 'AGPL-3',
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/13.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'sale_management', 'website'],

    # always loaded
    'data': [
         'security/ir.model.access.csv',
         'views/ship_info.xml',
         'views/ship_website_form.xml',
         'data/menu.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
    ],

    'installable': True,
    'application': True,
    'auto_install': False,
}
