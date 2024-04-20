from django.urls import path

from . import views

urlpatterns = [
    path('<slug:course_slug>/', views.study_sandbox, name='study-sandbox'),
    path('mark_lesson_watched/<int:lesson_content_id>/', views.mark_lesson_watched, name='mark_lesson_watched'),
    path('get_quiz/<int:pk>/', views.get_quiz, name='get_quiz'),
]
