from odoo import fields, models,api


class OurTeacher(models.Model):
    _name = 'our.teacher'
    _description = 'Our teacher in our school, what in ?'

    name = fields.Char(required=1, string='Teacher Name')
    age = fields.Integer(required=1)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=1)
    is_employee = fields.Boolean()
    hiring_date = fields.Date(default=fields.datetime.now())
    experience_years = fields.Integer(compute='_compute_experience_years', store=True)
    description = fields.Text(string="Specialty")
    salary = fields.Float()
    phone = fields.Char()

    @api.depends('hiring_date')
    def _compute_experience_years(self):
        for rec in self:
            if rec.hiring_date:
                rec.experience_years = (fields.Date.today() - rec.hiring_date).days // 365
            else:
                rec.experience_years = 0
