# -*- coding: utf-8 -*-
from odoo import models, fields
class ProductTemplate(models.Model):
   _inherit = 'product.template'
   launch_date = fields.Date(string='Launch Date')