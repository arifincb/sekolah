# -*- coding: utf-8 -*-
from datetime import datetime
from openerp import models, fields, api
class OpcJenjang(models.Model):
    _name = 'opc.jenjang'
    _sql_constraints = [
        ('jenjang_uniq',
        'UNIQUE (name)',
        'Jenjang yang diisikan sudah ada')]
        
    name = fields.Char(string='Jenjang Pendidikan', size=20, required=True)
    code = fields.Char(string='Kode Alias', size=20, required=True,)    
    is_current = fields.Boolean('Jadikan Jenjang Pendidikan Default?')
    kelas_ids = fields.One2many(
        'opc.kelas', # related model
        'jenjang_id', # field for "this" on related model
        'Kelas')

    
    
