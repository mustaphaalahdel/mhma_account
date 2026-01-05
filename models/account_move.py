from odoo import models, fields, api
from datetime import datetime

class AccountMove(models.Model):
    _inherit = "account.move"

    stock_valuation_ids = fields.One2many(
        comodel_name = 'stock.valuation.layer',
        inverse_name = 'account_move_id',
    )

    # حقل مساعد للاختيار
    stock_valuation_select_ids = fields.Many2many(
        'stock.valuation.layer',
        string="Select Stock Valuation Layers",
        help="Temporary field to select existing valuation layers"
    )

    @api.onchange('stock_valuation_select_ids')
    def _onchange_stock_valuation_select_ids(self):
        """عند اختيار سجلات جديدة نربطها مباشرة بالـ account_move_id"""
        for move in self:
            if move.stock_valuation_select_ids:
                move.stock_valuation_select_ids.write({'account_move_id': move.id})

