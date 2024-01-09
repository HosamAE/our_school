from odoo import fields, models


class Teacher(models.Model):
    _name = 'teacher'
    _description = 'Our teacher in our school, what in ?'

    name = fields.Char(required=1, string='Teacher Name')
    age = fields.Integer(required=1)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=1)
    employee = fields.Boolean()
    description = fields.Text(string="Specialty")
    salary = fields.Float()
    phone = fields.Char()
