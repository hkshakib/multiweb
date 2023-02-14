from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, mail_admins, BadHeaderError


# Create your views here.

def send_email(request):
    try:
        send_mail('Subject', 'massa ge', 'hkshakib@gmail.com', ['shakib@gmail.com'])
    except BadHeaderError:
        pass
    return HttpResponse("Hello")
