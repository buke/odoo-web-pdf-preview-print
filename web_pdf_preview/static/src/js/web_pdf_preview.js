/*############################################################################
#    Web PDF Report Preview & Print
#    Copyright 2014 wangbuke <wangbuke@gmail.com>
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
############################################################################*/
odoo.define('report.web_pdf_preview', function (require) {

function is_mobile() {
    return /Android|iPhone|iPad|iPod|Mobi/i.test(navigator.userAgent);
}

/*
 * Hook `session.get_file` in /addons/report/static/src/js/qwebactionmanager.js to prevent downloading.
 */
var session = require('web.session');
var get_file = session.get_file;

session.get_file = function(options) {
	alert("文本")
    if (!options || options.url !== '/report/download') {
        get_file.apply(this, arguments);
        return;
    }

    var params = {
        data: options.data.data,
        token: new Date().getTime()
    };
    var url = session.url('/report/preview', params);

    /*
     * Open the PDF report in current window on mobile (since iPhone prevents
     * openning in new window), while open in new window on desktop.
     * 手机上在当前页面打开 PDF 文档(因为iPhone不允许在新窗口打开)， 桌面浏览器在新窗口打开
     */
    if (is_mobile()) {
        require('web.framework').unblockUI();
        location.href = url;
    } else {
        window.open(url);
        if (typeof options.success === 'function') {
            options.success();
        }
        if (typeof options.complete === 'function') {
            options.complete();
        }
    }
};

});
