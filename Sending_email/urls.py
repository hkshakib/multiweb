from django.urls import path
from . import views

urlpatterns = [
    path('', views.send_email),
    path('admin_mail/', views.sending_admin_mail)
]