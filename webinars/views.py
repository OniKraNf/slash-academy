from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Webinar
from authorization.models import User
from django.db.models import Sum
# Create your views here.

# class WebinarsListView(ListView):
#     template_name = "webinars/webinars.html"
def webinars(request):
    return render(request, 'webinars/webinars.html')

def web_test_page(request):
    return render(request, 'webinars/web_test_page.html')

class WebinarsView(ListView):
    model = Webinar
    template_name = 'webinars/webinars.html'
    context_object_name = 'webinars'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        context['webinars'] = self.model.objects.all().order_by('name')
        return context        
    
class WebinarPageView(DetailView):
    model = Webinar
    template_name = 'webinars/webinar_page.html'
    context_object_name = 'webinar'