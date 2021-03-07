# -*- coding: utf-8 -*-
{
    'name': "Price Calculator Multi Currency",

    'summary': """
        Ce module intervient dans le calcul des prix dans les lignes de la facture en changeant la devise
            """,

    'description': """
       
    """,

    'author': "SLIMANI Farid",
    'website': "",

 
    'category': 'account',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','account'],

    # always loaded
    'data': [
        # 'security/ir.model.access.csv',
        'views/account_move.xml',
    ],
  
   
}
