from django.shortcuts import render
from django.http import HttpResponse  # new


# Create your views here.

def send_mail(request):
    return HttpResponse("HEllo")
