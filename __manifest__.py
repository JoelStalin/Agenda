# -*- coding: utf-8 -*-
{
    'name': 'Agenda',
    'category': 'Uncategorized',
    'version': '1.0',
    'depends': ['base','contacts','web'],  
    'data': [
        'security/agenda_security.xml',
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        'views/agenda_templates.xml',
        'views/report_contact_agenda_template.xml',
        'reports/agenda_report.xml'
        
    ],
    'assets': {
        'web.assets_backend': [
            'Agenda/static/src/js/rpc_service.js'
        ]
        },
    'demo': [
        'demo/demo.xml',
    ],
    'description': 'Descripción del módulo Agenda.',
    'author': 'Joel S. Martinez',
    'license': 'LGPL-3'
}
