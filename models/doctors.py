from odoo import models, fields, api
from datetime import timedelta


class Doctors(models.Model):
    _name = 'medical.doctors'
    _description = 'Doctors'

    first_name = fields.Char(string="نام", required=True)

    last_name = fields.Char(string="نام خانوادگی")
    
    medical_code = fields.Integer(string="شماره نظام پزشکی",required=True)
    
    specialty = fields.Selection(string="تخصص", required=True, selection=[('dentist','دندان پزشک'),('orthopedist','ارتوپد')],)
    
    phone = fields.Char(string="تلفن داخلی")
    
    email = fields.Char(string="ایمیل")
    
    birth_date = fields.Date(string="تاریخ تولد")
    
    gender = fields.Selection(string="",selection=[('women','زن'),('man','مرد')],)
    
    is_active = fields.Boolean(string="فعال")
    
    room_number = fields.Char(string="شماره اتاق")
    
    working_schedual_ids = fields.One2many(string="روز های فعال")
    
    description = fields.Char(string="توضیحات")
    
    consultation_fee = fields.Float(string="هزینه وزیت" , default="280000")
