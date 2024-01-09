from odoo import fields, models


class Classroom(models.Model):
    _name = "classroom"
    _description = "classrooms in our school"

    name = fields.Char(required=1)
    number_of_student = fields.Char(required=1, string='The number')

    teacher_ids = fields.Many2many("teacher", string="teacher")
    student_ids = fields.One2many("student", "class_id", string="student")


