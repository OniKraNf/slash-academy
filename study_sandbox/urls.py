from django.urls import path

from . import views

urlpatterns = [
    path('', views.StudySandboxView.as_view(), name='study-sandbox')
]
