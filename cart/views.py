from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseServerError, HttpResponse

from courses.models import Course

from slash_academy.models import Enroll
from authorization.models import User

from .cart import Cart


# Create your views here.

# this is our main page with the specific useful context
def cart_summary(request):
    cart = Cart(request) # Get cart with request.session from cache
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
    

def cart_buy(request):
    cart = Cart(request)
    if request.POST.get('action') == 'post':
        course_slug = request.POST.get('course_slug')
        print(course_slug)
        user = request.user
        course = get_object_or_404(Course, slug=course_slug) # SOBRADSAADAAAA AAAAA ELBAN WED YA EBLAN AAAA EBLAAAAN AAAAA 
        
        # Check if the user is already in the course
        if Enroll.objects.filter(user=user, course=course).exists():
            return HttpResponseServerError('User is already enrolled in course')
        
        enroll = Enroll(user=user, course=course)
        try:
            enroll.save()
            cart.delete(course)
            return HttpResponse('Entrollment successful.')
        except Exception as e:
            print('Enroll error:', e)
            return HttpResponseServerError('Failed to enroll in the course')
        