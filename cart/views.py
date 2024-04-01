from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from courses.models import Course
from .cart import Cart

# Create your views here.
def cart_summary(request):
    return render(request, 'cart/cart_summary.html', {})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        course_slug = request.POST.get('course_slug')
        course = get_object_or_404(Course, slug=course_slug)
        cart.add(course=course)
        
        response = JsonResponse({'Course name: ': course.name})
        return response
        