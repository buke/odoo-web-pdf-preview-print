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

{
    "name": "Web PDF Report Preview & Print",
    'version': '1.0',
    'category': 'Web',
    'description': """Web PDF Report Preview & Print
    For IE on windows, Adobe Reader is required.
    For Chrome , nothing is requried.
    For Firefox on windows, Adobe Reader is required.

    If your brower prevented pop-up window, you should allow it.
    """,
    'author': 'wangbuke@gmail.com',
    'website': 'http://my.oschina.net/wangbuke',
    'license': 'AGPL-3',
    'depends': ['web'],
    'data': [],
    'auto_install': False,
    'web_preload': True,
    'js': ['static/src/js/web_pdf_preview.js'],
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
