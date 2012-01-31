# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2012 Therp BV (<http://therp.nl>).
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
{
    "name" : "Accounting Reports Alternative",
    "version" : "0.1r6",
    "author" : "Therp BV",
    "category": 'Accounting & Finance',
    'complexity': "normal",
    "description": """
This is a port of the financial reports 'Balance sheet' and
'Profit and Loss' from OpenERP 6.0 to OpenERP 6.1
    """,
    'website': 'http://therp.nl',
    'images' : [],
    'init_xml': [],
    "depends" : ["account"],
    'update_xml': [
        'menu.xml',
        'wizard/account_report_common_view.xml',
        'wizard/account_report_balance_sheet_view.xml',
        'wizard/account_report_profit_loss_view.xml',
    ],
    'demo_xml': [],
    'test': [ ],
    'installable': True,
    'active': False,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
