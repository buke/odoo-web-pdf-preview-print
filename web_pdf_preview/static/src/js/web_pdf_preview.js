/*############################################################################
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
############################################################################*/

openerp.web_pdf_preview = function(openerp) {
    _t = openerp.web._t;

    openerp.web.ActionManager = openerp.web.ActionManager.extend({
        ir_actions_report_xml: function(action, on_closed) {
            //$("a").attr('target', '_blank');
            var self = this;
            $.blockUI();
            self.rpc("/web/session/eval_domain_and_context", {
                contexts: [action.context],
                domains: []
            }).then(function(res) {
                //if(action.report_type == 'pdf') { 
                var os = navigator.platform || "Unknown OS";
                linux = os.indexOf("Linux") > -1;
                if(!linux) { 
                    action = _.clone(action);
                    action.context = res.context;
                    self.rpc('/web/report/pdf_token', 
                        {action: JSON.stringify(action), token: new Date().getTime()}, 
                        function(result) {
                            $.unblockUI();
                            self.dialog_stop();
                            window.open('/web/report/pdf?pdf_file_token=' + result.pdf_file_token + '&session_id=' + self.session.session_id, 'report', '');
                        }
                    );
                }
                else{
                    action = _.clone(action);
                    action.context = res.context;
                    self.session.get_file({
                        url: '/web/report',
                        data: {action: JSON.stringify(action)},
                        complete: $.unblockUI,
                        success: function(){
                            if (!self.dialog && on_closed) {
                                on_closed();
                            }
                            self.dialog_stop();
                        },
                        error: openerp.webclient.crashmanager.on_rpc_error
                    });
                }
                    
            });
        },

    });


};


