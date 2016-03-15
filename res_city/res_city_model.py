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


class ResCity(models.Model):
    _name = "res.city"    

    name = fields.Char('City')
    city_code = fields.Char('Code')
    city_num_seq = fields.Char('Sequence')
    state_id = fields.Many2one('res.country.state','Propinsi')
    districts_ids = fields.One2many('res.districts', 'city_id', 'Kecamatan')    

class ResCountryState(models.Model):
    _inherit = 'res.country.state'
    
    #city_ids = fields.One2many('res.city', 'state_id', 'Kota', context="{'state_id': id}")
    city_ids = fields.One2many('res.city', 'state_id', 'Kota')

    
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
