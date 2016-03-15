# -*- coding: utf-8 -*-
from datetime import datetime
from openerp import models, fields, api
class OpcRombel(models.Model):
    _name = 'opc.rombel'
    #_inherit = ['opc.tahun.akademik', 'opc.kelas', 'opc.prodi']
    _sql_constraints = [
        ('rombel_uniq',
        'UNIQUE (name, tahun_akademik_id, kelas_id, prodi_id)',
        'Rombongan Belajar yang diisikan sudah ada')]
        
    name = fields.Char(string='Rombongan Belajar', size=64, required=True)
    code = fields.Char(string='Kode Alias', size=20, required=True)
    tahun_akademik_id = fields.Many2one('opc.tahun.akademik', 'Tahun Akademik', required=True)
    kelas_id = fields.Many2one('opc.kelas', 'Kelas', select=True, required=True)
    prodi_id = fields.Many2one('opc.prodi',
                               'Prodi',
                               domain="[('kelas_ids', 'in',kelas_id), ]",
                               required=True
    )
    guru_id = fields.Many2one('opc.guru', 'Guru Wali Rombongan Belajar', required=True)
    siswa_ids = fields.Many2many(
        'opc.siswa', # related model        
        string='Siswa')
    
    
