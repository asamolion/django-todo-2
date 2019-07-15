
from django.http import Http404
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Choice, Question
from .serializers import QuestionSerializer

class QuestionList(APIView):
    """
    List all Questions, or create a new Question.
    """
    def get(self, request, format=None):
        Questions = Question.objects.all()
        serializer = QuestionSerializer(Questions, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
        serializer = QuestionSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class QuestionDetail(APIView):
    """
    Retrieve, update or delete a Question instance.
    """
    def get_object(self, pk):
        try:
            return Question.objects.get(pk=pk)
        except Question.DoesNotExist:
            raise Http404

    def get(self, request, pk, format=None):
        Question = self.get_object(pk)
        serializer = QuestionSerializer(Question)
        return Response(serializer.data)

    def put(self, request, pk, format=None):
        Question = self.get_object(pk)
        serializer = QuestionSerializer(Question, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, pk, format=None):
        Question = self.get_object(pk)
        Question.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)