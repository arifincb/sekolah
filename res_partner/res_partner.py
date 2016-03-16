# -*- coding: utf-8 -*-
###############################################################################
#
#    Tech-Receptives Solutions Pvt. Ltd.
#    Copyright (C) 2009-TODAY Tech-Receptives(<http://www.techreceptives.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
###############################################################################

from openerp import models, fields, api


class ResPartner(models.Model):
    _inherit = 'res.partner'
    _sql_constraints = [
        ('partner_name_uniq',
        'UNIQUE (name, birth_place, birth_date, gender, active)',
        'There is already Active Partner/Person with current name, birth_place, birth_date, gender!')]
        
    birth_place = fields.Char('Tempat Lahir', required=True)    
    birth_date = fields.Date('Tanggal Lahir', required=True)
    birth_mother_name = fields.Char('Nama Ibu Kandung', required=True)
    blood_group = fields.Selection(
        [('A+', 'A+ve'), ('B+', 'B+ve'), ('O+', 'O+ve'), ('AB+', 'AB+ve'),
         ('A-', 'A-ve'), ('B-', 'B-ve'), ('O-', 'O-ve'), ('AB-', 'AB-ve')],
        'Golongan Darah')
    gender = fields.Selection(
        [('m', 'Male'), ('f', 'Female'),
         ('l', 'Laki-laki'), ('p', 'Perempuan'),
         ('o', 'Other')], 'Gender', required=True)
    religion = fields.Selection(
        [('islam', 'Islam'), ('kristen', 'Kristen'),
         ('katholik', 'Katholik'), ('hindu', 'Hindu'),
         ('budha', 'Budha'),
         ('lainnya', 'Lainnya')], 'Agama', required=True)
    nik = fields.Char('Nomor Induk Kependudukan')
    rt = fields.Char('RT')
    rw = fields.Char('RW')
    kelurahan = fields.Char('Desa/Kelurahan')
    #districts_id = fields.Many2one('res.districts','Kecamatan', placeholder="Kecamatan", domain="[('city_id', '=',city_id)]")
    #city_id = fields.Many2one('res.city','Kota', placeholder="Kota", domain="[('id', '=',districts_id.city_id.id)]")
    districts_id = fields.Many2one('res.districts','Kecamatan', placeholder="Kecamatan", on_change="onchange_districts(disctricts_id)")
    city_id = fields.Many2one('res.city','Kota', placeholder="Kota")
    city = fields.Char(related='districts_id.city_id.name', inherited=True)

    @api.multi
    #@api.onchange('districts_id')
    def onchange_districts(self, districts_id):
    #def onchange_districts(self):    
        if districts_id:
            districts = self.env['res.districts'].browse(districts_id)            
            return {
                'value': {                    
                    'city_id': districts.city_id.id
                    ,'state_id': districts.city_id.state_id.id
                    ,'country_id': districts.city_id.state_id.country_id.id                    
                    },
                'domain': {
                    'city_id': [('state_id', '=', districts.city_id.state_id.id)]
                    ,'state_id': [('country_id', '=', districts.city_id.state_id.country_id.id)]
                    }
                }
        return {}


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
