from odoo import fields, models 
  
from .res_partner import TIPOS_CLIENTE 
  
  
class TiendaConvenio(models.Model): 
    _name = "tienda.convenio" 
    _description = "Convenio de descuento" 
  
    name = fields.Char(string="Nombre", required=True) 
    tipo_cliente = fields.Selection(TIPOS_CLIENTE, string="Tipo de cliente", required=True) 
    porcentaje = fields.Float(string="Descuento (%)", required=True) 
    fecha_inicio = fields.Date(string="Desde", required=True, default=fields.Date.context_today) 
    fecha_fin = fields.Date(string="Hasta") 
    active = fields.Boolean(string="Activo", default=True) 