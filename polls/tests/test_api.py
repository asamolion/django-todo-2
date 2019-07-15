import json
from datetime import datetime

from django.test import TestCase
from rest_framework.test import APIRequestFactory, APIClient

from polls.models import Question
from polls.api import QuestionList

from pprint import pprint

PUB_DATE = '2019-07-15T14:37:49.629427Z'


class QuestionsAPITestCase(TestCase):

    def setUp(self):
        pub_date = datetime.strptime(PUB_DATE, '%Y-%m-%dT%H:%M:%S.%fZ')
        self.question1 = Question.objects.create(
            question_text='question 1', pub_date=pub_date)
        self.question2 = Question.objects.create(
            question_text='question 2', pub_date=pub_date)
        self.factory = APIRequestFactory()
        self.client = APIClient()

    def test_question_list_api(self):
        request = self.factory.get('/questions/')
        response = QuestionList().get(request)
        self.assertEqual(
            json.dumps(response.data),
            ('[{"id": 1, "question_text": "question 1", "pub_date": '
             '"2019-07-15T14:37:49.629427Z"}, {"id": 2, "question_text": "question 2", '
             '"pub_date": "2019-07-15T14:37:49.629427Z"}]')
        )

    def test_create_question(self):
        response = self.client.post(
            '/questions/',
            data={'question_text': 'QTA', 'pub_date': PUB_DATE},
            format='json'
        )

        self.assertEqual(response.status_code, 201)
        self.assertEqual(
            response.data,
            {
                'id': 3,
                'pub_date': '2019-07-15T14:37:49.629427Z',
                'question_text': 'QTA'
            }
        )
