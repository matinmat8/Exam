from django.contrib import messages
from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView, DetailView
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse

# from .forms import AddExamForm, AddQsForm
from .models import Exam

# Getting form fields
get_field = lambda f, request: request.POST.get(f)


def index(request):
    return render(request, 'exam/base.html')


@method_decorator(login_required, name='dispatch')
class AddExam(View):
    model = Exam
    template_name = 'exam/add_exam.html'

    def get(self, *args, **kwargs):
        return render(request=self.request, template_name=self.template_name)

    def post(self, *args, **kwargs):
        request = self.request
        try:
            obj = Exam.objects.create(
                user=request.user,
                title=get_field('title', request),
                classroom=get_field('classroom', request),
                exam_duration=get_field('exam_duration', request),
                teacher_name=get_field('teacher_name', request),
                type_of_exam=get_field('type_of_exam', request),
                start_time=get_field('start_time', request),
                end_time=get_field('end_time', request),
                exam_score=get_field('exam_score', request),
            )
            obj.save()
            return redirect('exam:exam_detail', pk=obj.pk)  # Redirecting to Exam detail page
        except:
            messages.add_message(request, messages.ERROR, message="There were some errors occurred during the adding "
                                                                  "exam, please try agin!")
            return HttpResponse('There is an error! please try again!')


@method_decorator(login_required, name='dispatch')
class ExamList(ListView):
    model = Exam
    template_name = 'exam/exam_list.html'

    def get_queryset(self):
        obj = super().get_queryset()
        user = self.request.user
        return obj.filter(user=user)


@method_decorator(login_required, name='dispatch')
class ExamDetail(DetailView):
    model = Exam
