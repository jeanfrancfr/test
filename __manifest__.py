# -*- coding: utf-8 -*-
{
    'name': "school_management",

    'summary': "Record Student Details"
        """ Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': "To manage School" 
    """ Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/15.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','product'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/student.xml',
        'views/templates.xml',
        'views/product_ext.xml',
     ],
    'qweb': [],
    'installable': True,
    'auto_install': False,
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}