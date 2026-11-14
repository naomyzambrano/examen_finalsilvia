from odoo import fields, models

TIPOS_CLIENTE = [
    ("estudiante", "Estudiante"),
    ("docente", "Docente"),
    ("administrativo", "Administrativo"),
    ("externo", "Externo"),
]

class ResPartner(models.Model):
    _inherit = "res.partner"

    tipo_cliente = fields.Selection(
        TIPOS_CLIENTE,
        string="Tipo de cliente",
        default="externo",
    )

    numero_cuenta = fields.Char(
        string="Número de cuenta",
        copy=False,
    )

    carrera = fields.Char(string="Carrera")