# -*- coding: utf-8 -*-
##############################################################################
#    Web PDF Report Preview & Print
#    Copyright 2012 wangbuke <wangbuke@gmail.com>
#    Modified by Yuan Xulei <hi@yxl.name> on Jan 1, 2017
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

from odoo.addons.report.controllers.main import ReportController
from odoo.addons.web.controllers.main import Reports, serialize_exception
from odoo import http

class PreviewReportController(ReportController):

    @http.route(['/report/preview'], type='http', auth="user")
    def report_download(self, data, token):
        result = super(PreviewReportController, self).report_download(data, token)
        result.headers['Content-Disposition'] = result.headers['Content-Disposition'].replace('attachment', 'inline')
        return result

class PreviewReports(Reports):

    @http.route('/web/report', type='http', auth="user")
    @serialize_exception
    def index(self, action, token):
        result = super(PreviewReports, self).index(action, token)
        result.headers['Content-Disposition'] = result.headers['Content-Disposition'].replace('attachment', 'inline')
        return result

