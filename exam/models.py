from django.contrib.auth.models import User
from django.db import models


TYPE_OF_TEST = (
    ('Descriptive', 'descriptive'),
    ('Test', 'test'),
    ('T/F', 't/f'),
)


class Exam(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    classroom = models.CharField(max_length=65)
    exam_duration = models.IntegerField()
    teacher_name = models.CharField(max_length=65)
    type_of_exam = models.CharField(choices=TYPE_OF_TEST, max_length=20)
    exam_url = models.URLField()
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    # students = models.ManyToManyField(student_model)