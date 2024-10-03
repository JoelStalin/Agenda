# -*- coding: utf-8 -*-

from odoo import models, fields, api
from odoo.exceptions import ValidationError

class ContactAgenda(models.Model):
    _name = 'contact.agenda'
    _description = 'Agenda de Contactos'

    name = fields.Char(string="Nombre", required=True)
    age = fields.Integer(string="Edad")
    phone = fields.Char(string="Teléfono")
    email = fields.Char(string="Correo Electrónico")
    photo = fields.Binary(string="Foto")
    address_ids = fields.One2many('contact.address', 'contact_id', string="Direcciones")
    user_type = fields.Selection([
        ('public', 'Público'),
        ('internal', 'Interno')
    ], string="Tipo de Usuario", default='public')

    def create_user(self):
        # Lógica para crear el usuario asociado
        for record in self:
            # Verificar si el usuario tiene el permiso adecuado
            if self.env.user.has_group('agenda_contactos.group_create_user'):
                vals = {
                    'name': record.name,
                    'login': record.email,
                    'groups_id': [(6, 0, [self.env.ref('base.group_public').id if record.user_type == 'public' else self.env.ref('base.group_internal_user').id])]
                }
                self.env['res.users'].create(vals)
            else:
                raise ValidationError('No tiene permiso para crear usuarios.')
    
    def print_report(self):
        # Lógica para imprimir datos (puede ser un reporte PDF, vista de impresión, etc.)
        return self.env.ref('Agenda.action_report_contact_agenda').report_action(self)


class ContactAddress(models.Model):
    _name = 'contact.address'
    _description = 'Dirección de Contacto'

    contact_id = fields.Many2one('contact.agenda', string="Contacto")
    street = fields.Char(string="Calle")
    city = fields.Char(string="Ciudad")
    country_id = fields.Many2one('res.country', string="País")
    
    
    @api.model
    def create(self, vals):
        # Verifica si el grupo de usuarios existe, si no, lo crea
        # group_name = 'Contact Address Group'
        
        # group = self.env['res.groups'].search([('name', '=', group_name)], limit=1)
        
        # if not group:
        #     group = self.env['res.groups'].create({
        #         'name': group_name,
        #         'implied_ids': [(6, 0, [self.env.ref('base.group_user').id])]  # Grupo implícito
        #     })

        # # Asigna el grupo a los permisos de acceso del modelo
        # vals = {
        #     'name': self.contact_id,
        #     'group_id' : [(4, group.id)]
        #     }
        

        return super(ContactAddress, self).create(vals)
