# -*- coding: utf-8 -*-
from odoo import models, fields, api

#this is a simple model for a simple website.
#We need also to implement some rules also.

class WebsiteMenu(models.Model):

    _name='website.menulevel'
    _description='New website menu'

    def _default_sequence(self):
        menu = self.search([], limit=1, order="sequence DESC")
        return menu.sequence or 0

    name = fields.Char('label',required=True)
    url = fields.Char(string='Url',required=True,default='')
    area = fields.Selection([('area_1', 'Area 1'), ('area_2', 'Area 2')],'Which Area the menu should be', default='area_1')
    parent_id = fields.Many2one('website.menulevel', 'Parent Menu', index=True, ondelete="cascade")


    sequence = fields.Integer(default=_default_sequence)
