from django.urls import path, include
from rest_framework import routers

from .views import (
    PollView,
    QuestionView,
    AnswerView,
    OptionView,
    UserAnswers,
    # get_user_answers,
    ActivePollsView,
)

router = routers.DefaultRouter()
router.register('active-polls', ActivePollsView, 'active-polls')
router.register('polls', PollView)
router.register('questions', QuestionView)
# router.register('answers/user/<int:user_id>/', UserAnswers, basename='UserAnswers')
router.register('answers', AnswerView)
router.register('options', OptionView)


urlpatterns = [
    path('', include(router.urls)),
    path('answers/user/<int:user_id>/', UserAnswers.as_view({'get': 'list'})),
    # path('active-polls/', ActivePolls.as_view({'get': 'list'})),
]