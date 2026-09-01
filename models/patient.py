from odoo import api, fields, models

class Patient(models.Model):
    _name = 'medical.patient'
    _description = 'Patient'

    first_name = fields.Char(string="نام")
    last_name = fields.Char(string="نام خانوادگی")
    national_code = fields.Char(string="کد ملی")
    birth_date = fields.Date(string="تاریخ تولد")
    age = fields.Integer(string="سن", compute="_compute_age", store=True)
    gender = fields.Selection([('male','مرد'),('female','زن')], string="جنسیت")
    phone = fields.Char(string="شماره تماس")
    address = fields.Text(string="آدرس")
    emergency_contact = fields.Char(string="شماره تماس اضطراری")
    blood_type = fields.Selection([('a_positive','A+'),('a_negative','A-'),('b_positive','B+'),('b_negative','B-'),('ab_positive','AB+'),('ab_negative','AB-'),('o_positive','O+'),('o_negative','O-')], string="گروه خونی")
    insurance = fields.Selection([('social_security','تأمین اجتماعی'),('health','بیمه سلامت'),('military','نیروهای مسلح'),('other','سایر'),('none','بدون بیمه')], string="نوع بیمه")
    insurance_number = fields.Char(string="شماره بیمه")
    is_active = fields.Boolean(string="فعال", default=True)
    description = fields.Text(string="توضیحات")


    @api.depends('birth_date')
    def _compute_age(self):
        today = fields.Date.today()
        for record in self:
            if record.birth_date:
                record.age = today.year - record.birth_date.year - ((today.month, today.day) < (record.birth_date.month, record.birth_date.day))
            else:
                record.age = 0