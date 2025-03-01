# -*- coding: utf-8 -*-
{
    'name': "purchase_user_mod",

    'summary': "Short (1 phrase/line) summary of the module's purpose",

    'description': """This module filters the view of a purchase user to only see their individual purchase and other members of the team""",

    'author': "Toluwani",
    'website': "https://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','purchase'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/purchaseteam_security.xml',
        'views/views.xml',
        'views/user_creation.xml',
        'data/purchase_team.xml'
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
    'installable': True,
    'application': True

}

