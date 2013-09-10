# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2004-2010 Tiny SPRL (<http://tiny.be>).
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

from openerp.osv import fields, osv
import pdb

class res_partner(osv.osv):
    _name = 'res.partner'
    _inherit = "res.partner"

    def _fnct_recency(self, cr, uid, ids, field_name, args, context=None):

	import pdb;pdb.set_trace()
	for partner in self.browse(cr,uid,ids,context=context):
		sql_string = "select date_invoice from account_invoice where partner_id = %d and type = 'out_invoice' and state in ('open','paid') order by date_invoice desc limit 1"%(partner.id)
	        cr.execute(sql_string)
        ids = map(itemgetter(0), cr.fetchall())

        partner_obj = self.pool.get('res.partner')
        if context is None:
            context = {}
        res = {}
        for partner in self.browse(cr, uid, ids, context=context):
            res[partner.id] = 0
        return res

    def _fnct_frequency(self, cr, uid, ids, field_name, args, context=None):
        partner_obj = self.pool.get('res.partner')
        if context is None:
            context = {}
        res = {}
        for partner in self.browse(cr, uid, ids, context=context):
            res[partner.id] = 0
        return res

    def _fnct_monetary(self, cr, uid, ids, field_name, args, context=None):
        partner_obj = self.pool.get('res.partner')
        if context is None:
            context = {}
        res = {}
        for partner in self.browse(cr, uid, ids, context=context):
            res[partner.id] = 0
        return res

    _columns = {
        'recency_metric': fields.function(_fnct_recency, string='Purchase Recency'),
        'frequency_metric': fields.function(_fnct_frequency, string='Purchase Frequency'),
        'monetary_metric': fields.function(_fnct_monetary, string='Purchase Amount'),
    }

res_partner()

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
