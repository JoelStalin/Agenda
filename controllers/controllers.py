# -*- coding: utf-8 -*-
from odoo import http

class MyModule(http.Controller):
  
    @http.route('/agenda', auth='public', website=True)
    def agenda_view(self, **kwargs):
        # Obtener los contactos desde el modelo res.partner
        contacts = http.request.env['contact.agenda'].search([])
        # Renderizar la plantilla con los contactos
        return http.request.render('Agenda.agenda_template', {
            'contacts': contacts,
        })
    @http.route('/agenda/agenda/contacts/', auth='public')
    def list(self, **kw):
        return http.request.render('Agenda.agenda_template', {
            'root': '/agenda/agenda',
            'contacts': http.request.env['contacts.agenda'].search([]),
        })
    @http.route('/Agenda/Agenda/objects/<model("contacts.agenda"):obj>/', auth='public')
    def object(self, obj, **kw):
        return http.request.render('Agenda.object', {
            'object': obj
        })
    
    @http.route('/agenda/print_report', type='json', auth='user')
    def print_report(self, report_name, record_ids):
        report = http.request.env['ir.actions.report']._get_report_from_name(report_name)
        if report:
            pdf = report._render_qweb_pdf(record_ids)[0]
            return http.request.make_response(pdf, {
                'Content-Type': 'application/pdf',
                'Content-Length': len(pdf),
            })
        return False