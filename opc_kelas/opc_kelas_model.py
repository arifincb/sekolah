# -*- coding: utf-8 -*-
from datetime import datetime
from openerp import models, fields, api
class OpcKelas(models.Model):
    _name = 'opc.kelas'    
    _sql_constraints = [
        ('kelas_uniq',
        'UNIQUE (name)',
        'Kelas yang diisikan sudah ada')]
        
    name = fields.Char(string='Kelas / Tingkat', size=20, required=True)
    code = fields.Char(string='Kode Alias', size=20, required=True)    
    is_current = fields.Boolean('Jadikan Kelas / Tingkat Default?')
    jenjang_id = fields.Many2one('opc.jenjang', 'Jenjang')
    prodi_ids = fields.Many2many(
        comodel_name='opc.prodi', # related model
        relation='opc_kelas_prodi_rel', # relation table name
        column1='kelas_id', # field for "this" record
        column2='prodi_id', # field for "other" record
        string='Prodi')
    
    
