# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Arifin Sekolah',
    'description': 'Siswa, Orang Tua.',
    'author': 'Arifin',
    'depends': ['base','hr'],
    'application': True,
    'data': [
        'security/opc_security.xml',
        'security/ir.model.access.csv',        
        'res_users/res_users_view.xml',
        'res_partner/res_partner_view.xml',
        'res_city/res_city_view.xml',
        'res_districts/res_districts_view.xml',
        'opc_siswa/opc_siswa_view.xml',
        'opc_guru/opc_guru_view.xml',
        'opc_tahun_akademik/opc_tahun_akademik_view.xml',
        'opc_jenjang/opc_jenjang_view.xml',
        'opc_kelas/opc_kelas_view.xml',
        'opc_prodi/opc_prodi_view.xml',
        'opc_rombel/opc_rombel_view.xml',                
        
    ],
}
