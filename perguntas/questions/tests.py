
from django.test import TestCase

from .models import Question

from django.contrib.auth import get_user_model

from questions.factory import UserFactory

from . import models

from rest_framework.test import APIClient

class QuestionEndpoint(TestCase):

    def setUp(self):
        Question.objects.create(text="Mensagem de teste?", answer="Sim", ordem="2" ,owner= UserFactory())
        Question.objects.create(text="Tudo certo?", answer="Sim", ordem="1" , owner= UserFactory())

    def test_endpoint_200(self):
        client = APIClient()
        response = client.get('/questions/')
        self.assertEqual(response.status_code, 200)

    def test_endpoint_users(self):
        client = APIClient()
        response = client.get('/users/')
        self.assertEqual(response.status_code, 200)

    def test_endpoint_post(self):
        client = APIClient()
        client.login(username = UserFactory(), password='123456')
        response = client.post('/questions/', {'text': 'teste post', 'answer': 'correto', 'ordem':3}, format="json")
        self.assertEqual(response.status_code, 201)
