from django.urls import path

from .views import *

app_name = "courses"

urlpatterns = [
    path('courses/<slug:slug>/', CourseView.as_view(), name="course_detail"),
    path('courses/', CoursesSearchView.as_view(), name="courses_search"),
]
