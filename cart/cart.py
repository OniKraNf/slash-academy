from decimal import Decimal
from django.conf import settings

from courses.models import Course

class Cart():
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}
            
        self.cart = cart
    
    
    def add(self, course):
        course_slug = str(course.slug)
        
        if course_slug in self.cart:
            pass
        else:
            self.cart[course_slug] = {'price': str(course.price)}
            
        self.session.modified = True
        
        
    def get_cours(self):
        # get data from session_key
        course_slug = self.cart.keys()
        # We are filtering all our courses in __in we used for filter
        courses = Course.objects.filter(slug__in=course_slug)
        return courses
    
    
    def delete(self, course):
        course_slug = str(course.slug)
        
        if course_slug in self.cart:
            del self.cart[course_slug]
        
        self.session.modified = True
        
    
    def get_quantity(self):
        quantity_keys = self.cart.keys()
        
        quantity = len(quantity_keys)
        return quantity
    
    
    def get_total_price(self):
        courses = self.get_cours()
        total_price = sum([course.price for course in courses])
        return total_price
        
        
    def __len__(self):
        return len(self.cart)