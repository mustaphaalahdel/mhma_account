{
    'name': 'MHMA Account',
    'version': '1.0',
    'summary': '',
    'author': 'MHMA',
    'category': 'Account',
    'depends': [
        'base',
        'account',
        'stock',
        'stock_account'
        ],
    'data': [
        "security/ir.model.access.csv",
        'views/account_move.xml',
         'views/res_partner.xml',
    ],
    'installable': True,
    'application': False,
}