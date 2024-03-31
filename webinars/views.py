from django.shortcuts import render
from django.views.generic import ListView
# Create your views here.

# class WebinarsListView(ListView):
#     template_name = "webinars/webinars.html"
def webinars(request):
    return render(request, 'webinars/webinars.html')

def web_test_page(request):
    return render(request, 'webinars/web_test_page.html')