# -*- coding: utf-8 -*-

from odoo import models, fields, api


class PurchaseTeam(models.Model):
    _name = 'purchase.team'
    _description = 'Purchase team'

    name = fields.Char(string="Team Name", required=True)
    user_id = fields.Many2many(
        comodel_name='res.users', 
        relation="purchase_team_user_rel",  
        column1="team_id",  
        column2="user_id", 
        string='Team Members'
    )


class team(models.Model):
    _inherit = 'res.users'

    team_id = fields.Many2many(
        comodel_name='purchase.team', 
        relation="purchase_team_user_rel",
        column1="user_id",
        column2="team_id",
        string="Purchase Teams"
    )
