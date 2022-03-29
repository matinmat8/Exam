from django.test import TestCase
from django.test.client import RequestFactory, Client
from django.contrib.auth.models import User
from django.urls import reverse

from .views import AddExam


class TestingView(TestCase):
    def setUp(self):
        self.factory = RequestFactory()
        self.user = User.objects.create_user(
            username='jacob', email='jacob@gmail.com', password='top_secret')

    def testing_adding_exam_view(self):
        data = {
            "pk": 1,
            "user": self.user,
            "title": "this is test",
            "classroom": '222',
            "exam_duration": 20,
            "teacher_name": 'Matin',
            "type_of_exam": 'Test',
            "start_time": '2022-03-19',
            "end_time": '2022-03-21',
            "exam_score": 20
        }

        request = self.factory.post('add/exam/', data=data)

        # logged-in user by setting request.user manually.
        request.user = self.user
        response = AddExam.as_view()(request)
        response.client = Client()

        # Redirecting to the expected URL
        url = reverse('exam:exam_detail', kwargs={'pk': 1})
        self.assertRedirects(response, expected_url=url, status_code=302, target_status_code=302)