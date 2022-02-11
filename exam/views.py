from django.shortcuts import render, redirect
from django.utils.decorators import method_decorator
from django.views.generic import View, ListView, DetailView
from django.contrib.auth.decorators import login_required

# from .forms import AddExamForm, AddQsForm
from .models import Exam

# Getting form fields
get_field = lambda f, request: request.POST.get(f)


def index(request):
    return render(request, 'exam/base.html')


class AddExam(View):
    model = Exam
    template_name = 'exam/add_exam.html'

    def get(self, *args, **kwargs):
        return render(request=self.request, template_name=self.template_name)

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
            exam_score=get_field('exam_score', request),
        )
        obj.save()
        return redirect('exam:exam_detail', pk=obj.pk)  # Redirecting to Exam detail page


@method_decorator(login_required, name='dispatch')
class ExamList(ListView):
    model = Exam
    template_name = 'exam/exam_list.html'

    def get_queryset(self):
        obj = super().get_queryset()
        user = self.request.user
        return obj.filter(user=user)


class ExamDetail(DetailView):
    model = Exam

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data()
    #     context['form'] = AddQsForm()
    #     return context
