from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView
from django.db.models import Sum

from .models import Course

from authorization.models import User

# Create your views here.
class CourseView(DetailView):
    model = Course
    template_name = 'courses/course.html'
    context_object_name = 'course'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)

        course = self.object
        includes = context['course'].includes.split(',')
        total_duration = course.lessons.aggregate(total_duration=Sum('duration'))['total_duration']
        
        user = User.objects.get(id=course.author.id)
        course_count = Course.objects.filter(author=user).count()
        
        context['includes'] = includes
        context['total_duration'] = total_duration
        context['course_count'] = course_count
        
        return context
    

class CoursesSearchView(ListView):
    model = Course
    template_name = "courses/courses_search.html"
    context_object_name = 'courses'
    
    def get_queryset(self) -> QuerySet[Any]:
        query = self.request.GET.get('q', '')
        if query:
            return self.model.objects.filter(name__icontains = query)
        else:
            return self.model.objects.none()