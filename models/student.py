from odoo import fields, models


class Student(models.Model):
    _name = 'student'
    _description = 'Our student in our school, in your opinion what in?'

    name = fields.Char(required=1, string='Student Name')
    age = fields.Integer(required=1)
    gender = fields.Selection([
        ('male', 'Male'),
        ('female', 'Female')
    ], required=1)
    academic_year = fields.Selection([
        ('first', 'The first'),
        ('second', 'The second'),
        ('third', 'The third'),
        ('fourth', 'The fourth'),
        ('fifth', 'The fifth'),
        ('sixth', 'The sixth')
    ])
    class_id = fields.Many2one("classroom", string="classroom")
