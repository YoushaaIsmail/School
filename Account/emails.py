from django.core.mail import send_mail
import random
from django.conf import settings
from .models import Account

def send_otp_via_email(email1):
    subject = "Your account verification email"
    otp1 = random.randint(1000 ,9999)
    message= f'Your otp is {otp1} '
    email_from = settings.EMAIL_HOST_USER
    send_mail(subject , message ,email_from , [email1])
    user_obj = Account.objects.get(email=email1)
    print(user_obj.email)
    user_obj.otp=otp1
    user_obj.save()