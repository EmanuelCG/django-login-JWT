from django_otp.oath import TOTP
from django_otp.util import random_hex
from django.core.mail import EmailMessage
from .models import User, OneTimePassword
from core import settings

def generate_verification_code():
    key = random_hex(20).encode()
    totp = TOTP(key, step=300, digits=6)
    return totp.token()

def send_code_to_user(email):
    subject = "Almost there! Complete the registration"
    otp_code = generate_verification_code()
    user = User.objects.get(email=email)
    current_site = "validation.com"
    OneTimePassword.objects.filter(user=user).delete()
    body = f'Hi {user.first_name} thanks for signing up on {current_site}. Please verify your email with the \n one time passocde {otp_code}'
    from_email = settings.DEFAULT_FROM_EMAIL
    OneTimePassword.objects.create(user=user, code=otp_code)
    email = EmailMessage(subject=subject, body=body, from_email=from_email, to=[email])
    email.send(fail_silently=True)

def send_normal_email(data):
    print(data)
    email = EmailMessage(
        subject=data['email_subject'],
        body=data['email_body'],
        from_email= settings.DEFAULT_FROM_EMAIL,
        to=[data['to_email']]
    )
    email.send()
