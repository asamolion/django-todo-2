from rest_framework import serializers
from .models import Question, Choice


class QuestionSerializer(serializers.Serializer):
    class Meta:
        model = Question
        fields = '__all__'
