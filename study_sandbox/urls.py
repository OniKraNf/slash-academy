from django.urls import path

from . import views

urlpatterns = [
    path('<slug:course_slug>/', views.StudySandboxView.as_view(), name='study-sandbox')
]
