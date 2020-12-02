# -*- coding: utf-8 -*-
{
    'name': "Website Product Visibility",
    'description': """
        Long description of module's purpose
    """,
    'author': "My Company",
    'website': "http://www.yourcompany.com",
    'category': 'Uncategorized',
    'version': '14.0.0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'website_sale', 'contacts'],

    # always loaded
    'qweb': [
        # 'static/src/xml/ProductDescription.xml',
        # 'static/src/xml/Description.xml',
    ],
    'data': [
        # 'security/ir.model.access.csv',
        'views/website_product_visibility.xml',
        # 'views/product_description.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True,
    'auto-install': False,
}
