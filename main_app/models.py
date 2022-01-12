from django.db import models
from django.utils.translation import gettext_lazy as _


class Poll(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    start_date = models.DateTimeField()
    end_date = models.DateTimeField()

    def __str__(self):
        return self.name


class Question(models.Model):
    class QuestionType(models.TextChoices):
        FREEFORM = 'FREE', _('Freeform')
        SINGLE = 'SING', _('Single Choice')
        MULTIPLE = 'MULT', _('Multiple Choice')

    poll = models.ForeignKey(Poll, related_name='questions', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    type = models.CharField(
        max_length=4,
        choices=QuestionType.choices,
        default=QuestionType.SINGLE,
    )

    def __str__(self):
        return self.text


class Option(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text


class Answer(models.Model):
    user_id = models.IntegerField(null=True, blank=True)
    poll = models.ForeignKey(Poll, on_delete=models.CASCADE)
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    option = models.ForeignKey(Option, on_delete=models.CASCADE, null=True, blank=True)
    text = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.text
