from django.urls import path
from .views import *

app_name = 'exam'

urlpatterns = [
    path('', index, name='index'),
    path('add/exam/', AddExam.as_view(), name='add_name'),
]