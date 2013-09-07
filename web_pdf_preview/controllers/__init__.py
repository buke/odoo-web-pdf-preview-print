# -*- coding: utf-8 -*-
##############################################################################
#    Web PDF Report Preview & Print
#    Copyright 2012 wangbuke <wangbuke@gmail.com>
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

import openerp.addons.web.http as openerpweb
from openerp.addons.web.controllers.main import Reports
import urllib

class WebPdfReports(Reports):
    _cp_path = "/web/report/pdf"

    @openerpweb.httprequest
    def index(self, req, action, token):
        action = urllib.unquote(action)
        result = super(WebPdfReports, self).index(req, action, token)
        result.headers['Content-Disposition'] = result.headers['Content-Disposition'].replace('attachment', 'inline')
        return result

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
