# -*- coding: utf-8 -*-

from odoo import models, fields, api


class Partner(models.Model):
    _inherit = 'res.partner'

    est_un_locataire = fields.Boolean()
    location_ids = fileds.One2many('estate.location', 'locataire_id', 'Locations')

