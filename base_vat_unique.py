# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2009 Tiny SPRL (<http://tiny.be>).
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
##############################################################################
#import logging
from osv import osv
from osv import fields
from tools.translate import _

#_logger = logging.getLogger(__name__)

class res_partner(osv.osv):
    _name = "res.partner"
    _inherit = "res.partner"


    def _check_unique_insesitive(self, cr, uid, ids, context=None):
        sr_ids = self.search(cr, 1 , [], context=context)
	current_partner = self.browse(cr, uid, ids, context=context)[0]


        lst = [x.vat.lower() for x in self.browse(cr, uid, sr_ids, context=context) if x.vat and x.id not in ids and x.supplier == current_partner.supplier]
        for self_obj in self.browse(cr, uid, ids, context=context):
            if self_obj.vat and self_obj.vat.lower() in  lst:
                return False
            return True

    _constraints = [(_check_unique_insesitive, 'Errore! La Partita IVA inserita esiste già associata ad un altra azienda.', ['vat'])]

res_partner()



