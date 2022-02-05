from django.contrib.auth.models import User
from django.db import models

from django.dispatch import receiver
from django.db.models.signals import post_save

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


# Filling in the exam_url field
@receiver(post_save, sender=Exam)
def add_url(sender, instance, **kwargs):
    url = 'http://127.0.0.1:8000/exam/%s/' % instance.id
    instance.exam_url = url


class Question(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    question = models.CharField(max_length=450)
    option_1 = models.CharField(max_length=250)
    option_2 = models.CharField(max_length=250)
    option_3 = models.CharField(max_length=250)
    option_4 = models.CharField(max_length=250)
    answer = models.CharField(
        max_length=25, choices=(('o_1', option_1), ('o_2', option_2), ('o_3', option_3), ('o_4', option_4)))


class Student(models.Model):
    exam = models.ForeignKey(Exam, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=250)
    last_name = models.CharField(max_length=250)
    email = models.EmailField()
    score = models.IntegerField()