from celery import shared_task
from django.template.loader import render_to_string
from django.utils.http import urlsafe_base64_encode
from django.utils.encoding import force_bytes
from django.core.mail import EmailMessage

from .models import User
from .tokens import account_activation_token

@shared_task()
def send_email_task(user_id, email, domain):
    user = User.objects.get(pk=user_id)
    subject = 'Activation link has been sent to your email'
    message = render_to_string(
        'authorization/activate_email.html', 
        {
            'user': user,
            'domain': domain,
            'uid': urlsafe_base64_encode(force_bytes(user.pk)), # User id which we need to encode for security in bytes
            'token': account_activation_token.make_token(user),
        })
    
    email = EmailMessage(
        subject, message, to=[email]
    )
    
    email.send()