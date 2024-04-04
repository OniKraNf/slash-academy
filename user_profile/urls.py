from django.urls import path
from . import views


urlpatterns = [
    path('<slug:slug>/', views.ProfilePageView.as_view(), name='profile_page')
]
