# -*- coding: utf-8 -*-
from datetime import datetime
from openerp import models, fields, api
class OpcTahunAkademik(models.Model):
    _name = 'opc.tahun.akademik'
    _sql_constraints = [
        ('tahun_akademik_uniq',
        'UNIQUE (year_start, year_end)',
        'Tahun  Akademik yang mulai dan berakhir dengan Tahun yang diisikan sudah ada')]
        
    name = fields.Char(string='Tahun Akademik', size=20, required=True)
    code = fields.Char(string='Kode Alias', size=20, required=True,)
    #year_start = fields.Selection([(num, str(num)) for num in range((datetime.now().year)-30 , datetime.now().year)], 'Tahun Mulai'),
    #year_end = fields.Selection([(num, str(num)) for num in range((datetime.now().year)-30 , (datetime.now().year)+1 )], 'Tahun Berakhir'),
    year_start = fields.Integer(string="Tahun Mulai", size=4, required=True,)
    year_end = fields.Integer(string="Tahun Berakhir", size=4, required=True,)
    is_current = fields.Boolean('Jadikan Tahun Akademik Default?')
    
    
