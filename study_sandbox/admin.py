from django.contrib import admin
from .models import Result, Quiz, Question, Answer

# Register your models here.

admin.site.register(Result)
admin.site.register(Quiz)

class AnswerInline(admin.TabularInline):
    model = Answer
    
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]

admin.site.register(Answer)
admin.site.register(Question, QuestionAdmin)