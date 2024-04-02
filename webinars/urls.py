from django.urls import path, include
from .views import *

# app_name = "webinars"

urlpatterns = [
    path('', WebinarView.as_view(), name='webinars'),   
    path('web-test-page', web_test_page, name='web_test_page'),
    path('webinars/<slug:slug>/', WebinarView.as_view(), name="webinar_detail")
]