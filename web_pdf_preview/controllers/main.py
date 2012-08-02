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
#    For Commercial or OEM, you need to contact the author and/or licensor
#    and ask for their permission.
#
#    本程序基于AGPL协议发布。在遵守本协议的基础上，您可以本程序用于非商业用途。
#    商业使用及二次开发，您需要联系并得到作者的许可。以上内容如有未尽事宜或冲
#    突以英文内容为准。
##############################################################################

try:
    # embedded
    import openerp.addons.web.common.http as openerpweb
    from openerp.addons.web.controllers.main import View
except ImportError:
    # standalone
    import web.common.http as openerpweb
    from web.controllers.main import View

import simplejson
import web.common as common
import base64
import time


import zlib
import cPickle
import hashlib
FILE_TOKENS ={}

class WebPdfFileTokenView(View):
    _cp_path = "/web/report/pdf_token"

    @openerpweb.jsonrequest
    def index(self, req, action, token):
        args = cPickle.dumps((action, token))
        token = hashlib.md5(args).hexdigest()
        FILE_TOKENS[str(req.session._uid)] = {token:args}
        return dict(pdf_file_token = token)

class WebPdfReports(View):
    _cp_path = "/web/report/pdf"
    POLLING_DELAY = 0.25
    TYPES_MAPPING = {
        'doc': 'application/vnd.ms-word',
        'html': 'text/html',
        'odt': 'application/vnd.oasis.opendocument.text',
        'pdf': 'application/pdf',
        'sxw': 'application/vnd.sun.xml.writer',
        'xls': 'application/vnd.ms-excel',
    }

    @openerpweb.httprequest
    def index(self, req, pdf_file_token):
        args = FILE_TOKENS[str(req.session._uid)].get(pdf_file_token, None)

        if not args:
            return;

        action, token  = cPickle.loads(args)

        action = simplejson.loads(action)

        report_srv = req.session.proxy("report")
        context = req.session.eval_context(
            common.nonliterals.CompoundContext(
                req.context or {}, action[ "context"]))

        report_data = {}
        report_ids = context["active_ids"]
        if 'report_type' in action:
            report_data['report_type'] = action['report_type']
        if 'datas' in action:
            if 'ids' in action['datas']:
                report_ids = action['datas'].pop('ids')
            report_data.update(action['datas'])

        report_id = report_srv.report(
            req.session._db, req.session._uid, req.session._password,
            action["report_name"], report_ids,
            report_data, context)

        report_struct = None
        while True:
            report_struct = report_srv.report_get(
                req.session._db, req.session._uid, req.session._password, report_id)
            if report_struct["state"]:
                break

            time.sleep(self.POLLING_DELAY)

        report = base64.b64decode(report_struct['result'])
        if report_struct.get('code') == 'zlib':
            report = zlib.decompress(report)
        report_mimetype = self.TYPES_MAPPING.get(
            report_struct['format'], 'octet-stream')
        return req.make_response(report,
             headers=[
                 ('Content-Disposition', 'inline; filename="%s.%s"' % (action['report_name'], report_struct['format'])),
                 ('Content-Type', report_mimetype),
                 ('Content-Length', len(report))],
             cookies={'fileToken': int(token)})


# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
