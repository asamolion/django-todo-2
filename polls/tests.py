from datetime import datetime

from django.test import Client, TestCase
from django.http import Http404
from rest_framework.test import APIRequestFactory

from .models import Question, Choice
# Create your tests here.

class QuestionTestCase(TestCase):

    def setUp(self):
        self.question1 = Question.objects.create(question_text='question 1', pub_date=datetime.now())
        self.question2 = Question.objects.create(question_text='question 2', pub_date=datetime.now())
        self.client = Client()

    def test_question_ordered_correctly(self):
        """
        List of questions on the polls index should be reverse chronological order
        """
        response = self.client.get('/polls/')
        self.assertEqual(response.context['latest_question_list'][0], self.question2)
        self.assertEqual(response.context['latest_question_list'][1], self.question1)

    def test_question_detail_view(self):
        """
        The detail page should contain the correct question object
        """
        response = self.client.get('/polls/1/')
        self.assertEqual(response.context['question'], self.question1)

    def test_absent_question_raises_404(self):
        """
        404 exception should be raised if question isn't present
        """
        response = self.client.get('/polls/3/')
        self.assertEqual(response.status_code, 404)


class QuestionsAPITestCase()



