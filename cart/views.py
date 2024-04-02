from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse

from courses.models import Course
from .cart import Cart

# Create your views here.
def cart_summary(request):
    cart = Cart(request)
    courses = cart.get_cours()
    quantity = cart.get_quantity()
    total_price = cart.get_total_price()
    return render(request, 'cart/cart_summary.html', {"courses": courses, 'quantity': quantity, 'total_price': total_price})

def cart_add(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        course_slug = request.POST.get('course_slug')
        course = get_object_or_404(Course, slug=course_slug)
        cart.add(course=course)
        cart_quantity = cart.__len__()
        response = JsonResponse({'Course name: ': course.name, 'cart_quantity': cart_quantity})
        return response
        

def cart_delete(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        course_slug = request.POST.get('course_slug')
        course = get_object_or_404(Course, slug=course_slug)
        cart.delete(course=course)
        response = JsonResponse({'Course has been deleted: ': course.name})
        return response