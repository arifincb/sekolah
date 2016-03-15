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

from openerp import SUPERUSER_ID, models, fields

from openerp.osv import fields, osv, expression

class res_users(osv.osv):
    _inherit = 'res.users'
    _inherits = {
        'res.partner': 'partner_id',
    }

    def _get_group_sekolah(self,cr, uid, context=None):        
        dataobj = self.pool.get('ir.model.data')
        result = []
        try:            
            dummy,group_id = dataobj.get_object_reference(cr, SUPERUSER_ID, 'sekolah', 'group_opc_siswa')
            result.append(group_id)
        except ValueError:
            # If these groups does not exists anymore
            pass
        return result
    
    _defaults = {        
        'groups_id': _get_group_sekolah,        
    }

        

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
