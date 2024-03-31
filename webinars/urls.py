from django.urls import path, include
from .views import *

urlpatterns = [
    path('', webinars, name='webinars'),   
    path('web-test-page', web_test_page, name='web_test_page')   
]