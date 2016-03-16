# -*- coding: utf-8 -*-
from openerp import models, fields, api
class OpcSiswa(models.Model):
    _name = 'opc.siswa'
    #_inherit = 'res.partner'
    _inherits = {'res.users': 'user_id'}

    
    nationality = fields.Many2one('res.country', 'Nationality')
    language = fields.Many2one('res.lang', 'Mother Tongue')        
    emergency_contact = fields.Many2one(
        'res.partner', 'Emergency Contact')    
    id_number = fields.Char('ID Card Number', size=64)
    photo = fields.Binary('Photo')            
    #partner_id = fields.Many2one(
    #    'res.partner', 'Partner', required=True, ondelete="cascade")    
    alumni_boolean = fields.Boolean('Alumni Student')        
    user_id = fields.Many2one('res.users', 'User')    
    #parent_ids = fields.Many2many('op.parent', string='Parent')
    rombel_ids = fields.Many2many('opc.rombel', string='Rombongan Belajar')

    
    #@api.multi    
    #def onchange_districts(self, districts_id):
    #    res = False
    #    if districts_id:
    #        res = super(res.partner, self).onchange_districts(districts_id)            
    #    return res
    
