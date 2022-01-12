from django.contrib import admin

from .models import Poll, Question, Answer, Option


class PollInline(admin.TabularInline):
    model = Question
    # fields = ['name', 'description', 'questions']

class PollAdmin(admin.ModelAdmin):
    inlines = [PollInline]

class QuestionInline(admin.TabularInline):
    model = Option

class QuestionAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

admin.site.register(Poll, PollAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Answer)
admin.site.register(Option)