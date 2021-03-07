# -*- coding: utf-8 -*-

from odoo import models, fields, api
import logging
_logger = logging.getLogger(__name__)

class Accountmove(models.Model):
    _inherit = 'account.move'


    @api.model
    def _get_default_old_currency(self):
        ''' Get the default old currency from either the journal, either the default journal's company. '''
        journal = self._get_default_journal()
        return journal.currency_id or journal.company_id.currency_id

    old_currency_id = fields.Many2one('res.currency', string='Ancienne devise',default=_get_default_old_currency)

        
    @api.onchange('date', 'currency_id')
    def _onchange_currency(self):
        super(Accountmove, self)._onchange_currency()
        for line in self.invoice_line_ids:  
            price = line.price_unit / self.old_currency_id.rate 
            line.price_unit = self.currency_id.rate * price
            #to update price_subtotal
            line._onchange_price_subtotal() 

        #to update taxes amount and recompute taxes lines
        self._recompute_tax_lines()
        self._recompute_dynamic_lines()
        self.old_currency_id = self.currency_id.id 
