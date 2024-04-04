from typing import Any
from django.shortcuts import render
from django.views.generic import DetailView

from authorization.models import Profile
from slash_academy.models import Enroll

class ProfilePageView(DetailView):
    model = Profile
    template_name = 'user_profile/profile.html'
    context_object_name = 'profile'
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        
        profile = self.object
        
        enrolled_courses = Enroll.objects.filter(user=profile.user)

        context['enrolled_courses'] = enrolled_courses
        
        return context