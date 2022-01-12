from django.shortcuts import render
from django.utils import timezone
from rest_framework import viewsets, permissions, generics
from rest_framework.response import Response
from rest_framework.decorators import api_view

from .models import Poll, Question, Answer, Option
from .serializers import PollSerializer, QuestionSerializer, AnswerSerializer, OptionSerializer


class PollView(viewsets.ModelViewSet):
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticated,)


class QuestionView(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    serializer_class = QuestionSerializer
    permission_classes = (permissions.IsAuthenticated,)


class AnswerView(viewsets.ModelViewSet):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = (permissions.AllowAny,)


class OptionView(viewsets.ModelViewSet):
    queryset = Option.objects.all()
    serializer_class = OptionSerializer
    permission_classes = (permissions.IsAuthenticated,)


# @api_view(['GET'])
# def get_user_answers(request, user_id):
#     """Returns user answers by its id."""
#     answers = Answer.objects.filter(user_id=user_id)
#     serializer = AnswerSerializer(answers, many=True)
#     return Response(serializer.data)

class UserAnswers(viewsets.ModelViewSet):
    # queryset = Answer.objects.all()
    serializer_class = AnswerSerializer

    def get_queryset(self):
        return Answer.objects.filter(user_id=self.kwargs["user_id"])


class ActivePollsView(viewsets.ModelViewSet):
    """
        Returns active polls. An active poll is one that satisfies the following condition:
        poll started before current user date and has not ended yet

        """
    queryset = Poll.objects.all()
    serializer_class = PollSerializer
    permission_classes = (permissions.IsAuthenticatedOrReadOnly,)

    def filter_queryset(self, queryset):
        return queryset.filter(**self.request.data)

    def get_queryset(self):
        return Poll.objects.filter(end_date__gte=timezone.now()).filter(start_date__lte=timezone.now())
