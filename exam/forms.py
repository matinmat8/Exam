from django.forms.models import ModelForm
from .models import Exam


class AddExamForm(ModelForm):
    class Meta:
        model = Exam
        fields = ['title', 'classroom', 'exam_duration', 'teacher_name', 'type_of_exam', 'start_time', 'end_time']