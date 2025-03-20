# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Propriete(models.Model):
    _name = 'estate.propriete'
    _description = 'Propriété'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    name = fields.Char()
    type_id = fields.Many2one('estate.type.piece', string="Type", help="Définir le type de pièce")
    superficie = fields.Float()
    piece_ids = fields.One2many('estate.piece', 'propriete_id', 'Pièces')
    commodite_ids = fields.One2many('estate.commodite', 'propriete_id', 'Pièces')
    loyer_mensuel = fields.Integer()
