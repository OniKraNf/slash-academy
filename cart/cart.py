from decimal import Decimal
from django.conf import settings

class Cart():
    def __init__(self, request) -> None:
        self.session = request.session
        
        cart = self.session.get('session_key')
        
        if 'session_key' not in request.session:
            cart = self.session['session_key'] = {}