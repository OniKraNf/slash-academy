from .cart import Cart

# Create context processor so our cart can work on all pages of site
# We must to add it in settings.py tempalte field
def cart(request):
    # Return the default data from our Cart
    return {'cart': Cart(request)}