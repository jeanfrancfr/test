# -*- coding: utf-8 -*-
from odoo import models, fields
class SaleOrder(models.Model):
   _inherit = 'sale.order'
short_note = fields.Char(string='Short Note')