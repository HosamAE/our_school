from odoo import fields, models, api, exceptions


class OurStudent(models.Model):
    _name = 'our.student'
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
    ], default='first')
    number_of_courses = fields.Integer(default=4)
    check_old = fields.Boolean(default=True)

    class_id = fields.Many2one("our.classroom", string="classroom")

    @api.constrains('age')
    def _check_permissible_age(self):
        for rec in self:
            if rec.age < 6:
                raise exceptions.ValidationError(
                    f"Sorry, in record ({rec.name}) the age is too small to join to our classroom")
            elif rec.age > 12:
                raise exceptions.ValidationError(
                    f"Sorry, in record ({rec.name}) thes age is too old to join to our classroom")

    @api.onchange('number_of_courses')
    def _onchange_number_of_courses(self):
        for rec in self:
            if rec.check_old and rec.number_of_courses < 6:
                raise exceptions.ValidationError(
                    f'The number of subjects to study in this semester " {rec.academic_year}'
                    + '" is very small')

    @api.onchange('academic_year')
    def _onchange_academic_year(self):
        for rec in self:
            if rec.academic_year == 'fifth':
                rec.number_of_courses = 6
                rec.check_old = True
            elif rec.academic_year == 'sixth':
                rec.check_old = True
                rec.number_of_courses = 6
            elif rec.academic_year == 'fourth':
                rec.check_old = True
                rec.number_of_courses = 6
            else:
                rec.check_old = False
