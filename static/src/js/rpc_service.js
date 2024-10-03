/** @odoo-module **/

import { rpc } from 'web.core';

export const PrintReportService = {
    async printReport(reportName, recordIds) {
        try {
            const response = await rpc({
                route: '/agenda/print_report',
                params: {
                    report_name: reportName,
                    record_ids: recordIds,
                },
            });
            if (response) {
                const blob = new Blob([response], { type: 'application/pdf' });
                const url = URL.createObjectURL(blob);
                window.open(url, '_blank');
            } else {
                console.error('Error al generar el reporte');
            }
        } catch (error) {
            console.error('RPC Error:', error);
        }
    }
};
