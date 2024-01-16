from odoo import fields, models, api, exceptions


class OurClassroom(models.Model):
    _name = "our.classroom"
    _description = "classrooms in our school"

    name = fields.Char(required=1)

    number_of_student = fields.Integer(compute='_compute_number_of_student', store=True)

    teacher_ids = fields.Many2many("our.teacher", string="Teachers")
    studgent_ids = fields.One2many("our.student", "class_id", string="Students")

    @api.depends('student_ids')
    def _compute_number_of_student(self):
        for rec in self:
            rec.number_of_student = len(rec.student_ids)

    @api.constrains('number_of_student')
    def _check_copy_count(self):
        for rec in self:
            if int(rec.number_of_student) > 20:
                raise exceptions.ValidationError(
                    "You cannot add more student. Maximum allowed student: 20\nyou can "
                    + "create a new classroom")
