from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

from courses.models import Course, Lesson
from slash_academy.models import Enroll

# Create your views here.
def study_sandbox(request, enroll_id    )
    