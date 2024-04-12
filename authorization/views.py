from django.core.mail import EmailMessage
from django.conf import settings
from django.http import HttpResponse
from django.shortcuts import redirect, render
from django.contrib.auth import logout, login, authenticate, get_user_model
from django.contrib.sites.shortcuts import get_current_site
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.utils.encoding import force_bytes, force_str

from authorization.forms import LoginForm, SignUpForm
from .tokens import account_activation_token
from .tasks import send_email_task

# Create your views here.
def activate(request, uidb64, token):
    User = get_user_model()
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = User.objects.get(pk=uid)
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):
        user = None
    
    if user is not None and account_activation_token.check_token(user, token):
        user.is_active = True
        user.save()
        return HttpResponse('Thank you for your email confirmation. Now you can login your account.')
    else:
        return HttpResponse('Activation link is invalid!')


def logout_view(request):
    logout(request)
    return redirect('/')


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request, data=request.POST)
        if form.is_valid():
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('/')
            else:
                form.add_error(None, 'Invalid username or password')
    else:
        form = LoginForm()
            
    return render(request, 'authorization/login.html', context={'form': form})


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            current_site = get_current_site(request)
            send_email_task.delay(user.id, user.email, current_site.domain)
            return redirect('/login/')
    else:
        form = SignUpForm()
    
    return render(request, 'authorization/signup.html', {'form': form})