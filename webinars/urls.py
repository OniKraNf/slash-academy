from django.urls import path, include
from .views import *

# app_name = "webinars"

urlpatterns = [
    path('', WebinarsView.as_view(), name='webinars'),   
    path('<slug:slug>/', WebinarPageView.as_view(), name="webinar_detail")
]