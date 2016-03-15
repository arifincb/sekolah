# -*- coding: utf-8 -*-
from datetime import datetime
from openerp import models, fields, api
class OpcProdi(models.Model):
    _name = 'opc.prodi'
    
    _sql_constraints = [
        ('prodi_uniq',
        'UNIQUE (name)',
        'Prodi yang diisikan sudah ada')]
        
    name = fields.Char(string='Program Studi', size=64, required=True)
    code = fields.Char(string='Kode Alias', size=20, required=True)    
    is_current = fields.Boolean('Jadikan Program Studi Default?')    
    kelas_ids = fields.Many2many(
        comodel_name='opc.kelas', # related model
        relation='opc_kelas_prodi_rel', # relation table name
        column1='prodi_id', # field for "this" record
        column2='kelas_id', # field for "other" record
        string='Kelas')
    
    
