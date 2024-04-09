from django.urls import path

from . import views

urlpatterns = [
    path('<slug:course_slug>/', views.study_sandbox, name='study-sandbox')
]
