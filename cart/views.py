from django.shortcuts import render

# Create your views here.
def cart_summary(request):
    return render(request, 'cart/cart_summary.html', {})