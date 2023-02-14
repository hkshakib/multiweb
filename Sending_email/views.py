from django.shortcuts import render
from django.http import HttpResponse
from django.core.mail import send_mail, mail_admins, BadHeaderError


# Create your views here.

def send_email(request):
    try:
        send_mail('Subject', 'massage', 'hkshakib@gmail.com', ['shakib@gmail.com'])
    except BadHeaderError:
        pass
    return HttpResponse("Email Send Successfully")


def sending_admin_mail(request):
    try:
        mail_admins('Subject', 'massage', html_message="massages only")
    except BadHeaderError:
        pass
    return HttpResponse("Email Send Successfully")