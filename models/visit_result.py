from odoo import models, fields, api


class VisitResult(models.Model):
    _name = 'visit_result'
    _description = 'VisitResult'

    
    Doctor=fields.Many2many("doctors_building.Doctor",string="پزشک معالج")
    Patient=fields.Many2many("doctors_building.Patient",string="نام بیمار")
    factor_consultation_fee = fields.Float(string="هزینه وزیت" , default="280000")
    Status = fields.Selection(string="وضعیت", required=True, selection=[('pending','در حال انجام'),('done','ویزیت انجام شده است'),('cancel','لغو شده')],)
    is_active = fields.Char(default=True)
