from django.shortcuts import render
from django.views.generic import View

from .forms import AddExamForm
from .models import Exam

# Getting form fields
get_field = lambda f, request: request.POST.get(f)


def index(request):
    return render(request, 'exam/base.html')


class AddExam(View):
    model = Exam
    template_name = 'exam/add_exam.html'

    def get(self, *args, **kwargs):
        form = AddExamForm()
        return render(request=self.request, template_name=self.template_name, context={'form': form})

    def post(self, *args, **kwargs):
        request = self.request
        obj = Exam.objects.create(
            user=request.user,
            title=get_field('title', request),
            classroom=get_field('classroom', request),
            exam_duration=get_field('exam_duration', request),
            teacher_name=get_field('teacher_name', request),
            type_of_exam=get_field('type_of_exam', request),
            start_time=get_field('start_time', request),
            end_time=get_field('end_time', request),
        )
        obj.save()
        return render(request=request, template_name='exam/base.html')