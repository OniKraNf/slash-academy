from decimal import Decimal
from django.conf import settings

from courses.models import Course


# Our class for cart on site
class Cart():
    """
        This class used for cart feature on website
        Args:
            __init__ (self, request): initialization session_key or create it.
            add (self, course): to add course in session_key.
            get_cours (self): to get course.
            delete (self, course): to delete course.
            get_quantity (self): get quantity of all courses in cart.
            get_total_price (self): to get total price.
    """
    
    
    # Constructor to get session_key or set it 
    def __init__(self, request):
        self.session = request.session
        
        cart = self.session.get('session_key') # we try to get session_key from request
        
        if 'session_key' not in request.session: # if we haven't 
            cart = self.session['session_key'] = {}
            
        self.cart = cart 
    
    
    def add(self, course): # Method to add cart in self.cart
        course_slug = str(course.slug) # get our slug from course
        
        if course_slug in self.cart:
            pass
        else:
            self.cart[course_slug] = {'price': str(course.price)} # set for cart['name'] price, but we can add something more.
            
        self.session.modified = True # that's important, without it, session won't be modified
        
        
    def get_cours(self):
        # we get all session_data using keys
        course_slug = self.cart.keys()
        
        # We are filtering all our courses in __in we used for filter
        courses = Course.objects.filter(slug__in=course_slug)
        return courses
    
    
    # delete cart
    def delete(self, course):
        course_slug = str(course.slug)
        
        if course_slug in self.cart:
            del self.cart[course_slug] # we delete this regular variable with our course_slug
        
        self.session.modified = True
        
    
    def get_quantity(self): # we get quantity of courses in cart
        quantity_keys = self.cart.keys()
        quantity = len(quantity_keys)
        return quantity
    
    
    def get_total_price(self):
        courses = self.get_cours()
        total_price = sum([course.price for course in courses])
        return total_price
        
        
    def __len__(self):
        return len(self.cart)