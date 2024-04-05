from typing import Any
from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Webinar, WebinarLesson
from authorization.models import User
from django.db.models import Sum
# Create your views here.

# class WebinarsListView(ListView):
#     template_name = "webinars/webinars.html"
def webinars(request):
    return render(request, 'webinars/webinars.html')

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
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        webinar = self.get_object()
        webinarlessons = webinar.webinarlessons.all()  # Получаем все уроки для данного вебинара
        context['webinarlessons'] = webinarlessons
        return context