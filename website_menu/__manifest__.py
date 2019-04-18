{
    'name': 'Website Menu',
    'category': 'Website',
    'version': '1.0',
    'author': 'Odoo S.A.(nwi@odoo.com)',
    'depends': ['website'],
    'data': [
        'security/ir.model.access.csv',
        'views/backend/menu_view_form.xml',
    ],
    'application': True,
}
