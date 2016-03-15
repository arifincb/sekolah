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

from openerp import models, fields, api, _
from openerp.exceptions import Warning


class OpcGuru(models.Model):
    _name = 'opc.guru'
    _inherits = {'hr.employee': 'emp_id'}
    
    emergency_contact = fields.Many2one(
        'res.partner', 'Emergency Contact')    
    photo = fields.Binary('Photo')
    nationality = fields.Many2one('res.country', 'Nationality')
    login = fields.Char(
        'Login', related='user_id.login', readonly=1)
    last_login = fields.Date(
        'Latest Connection', related='user_id.login_date',
        readonly=1)
    #timetable_ids = fields.One2many('op.timetable', 'faculty_id', 'Time table')    
    #faculty_subject_ids = fields.Many2many('op.subject', string='Subjects')
    emp_id = fields.Many2one('hr.employee', 'Employee')

    @api.one
    def create_employee(self):
        emp_obj = self.env['hr.employee']
        vals = {            
            'name': self.name,
            'country_id': self.nationality.id,
            'gender': self.gender,
        }
        emp_id = emp_obj.create(vals)
        self.write({'emp_id': emp_id.id})


class HrEmployee(models.Model):
    _inherit = 'hr.employee'
    _inherits = {'res.users': 'user_id'}
    
    @api.onchange('user_id')
    def onchange_user(self):
        if self.user_id:
            self.user_id.partner_id.supplier = True
            self.address_home_id = self.user_id.partner_id.id
            self.work_email = self.user_id.email
            self.identification_id = False
            return {'domain':
                    {'address_id': [('id', '=', self.user_id.partner_id.id)]}}

    @api.onchange('address_id')
    def onchange_address_id(self):
        if self.address_home_id and self.address_id and \
                self.address_home_id != self.address_id:
            raise Warning(_('Configuration Error!'), _(
                'Home Address and working address should be same!'))
        if self.address_id:
            self.work_phone = self.address_id.phone
            self.mobile_phone = self.address_id.mobile

    @api.onchange('address_home_id')
    def onchange_address_home_id(self):
        if self.address_home_id and self.address_id and \
                self.address_home_id != self.address_id:
            raise Warning(_('Configuration Error!'), _(
                'Home Address and working address should be same!'))
        if self.address_home_id:
            self.address_home_id.write({'supplier': True, 'employee': True})


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
