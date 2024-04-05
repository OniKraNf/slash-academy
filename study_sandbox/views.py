from django.shortcuts import render
from django.views.generic import ListView

from courses.models import Lesson

# Create your views here.
class StudySandboxView(ListView):
    model = Lesson
    template_name = 'study-sandbox/study_sandbox.html'
    context_object_name = 'lessons'
