from typing import Any
from django.db.models.query import QuerySet
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.views.generic import ListView
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required
from django.db.models import Sum

from courses.models import Course, LessonContent, LessonProgress
from slash_academy.models import Enroll

# Create your views here.
def study_sandbox(request, course_slug):
    try:
        course = get_object_or_404(Course, slug=course_slug)
        lessons = course.lessons.all().prefetch_related('lessons_content') 
    except Course:
        return render(request, 'errors/404.html')
    
    user = request.user

    try:
        enroll = get_object_or_404(Enroll, course=course, user=user)
    except:
        return render(request, 'errors/404.html')

    context = { 'course': course, 'lessons': lessons}  # Add lessons to context
    return render(request, 'study-sandbox/study_sandbox.html', context) 


def mark_lesson_watched(request, lesson_content_id):
    lesson_progress = get_object_or_404(LessonProgress, lesson_content_id=lesson_content_id)
    if not lesson_progress.watched:
        lesson_progress.watched = True
        lesson_progress.save()
        return JsonResponse({'message': 'Lesson content marked as watched.'})
    else:
        return JsonResponse({'message': 'Lesson content is already marked as watched.'})