from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    url('register/',views.register),
    url('login/',views.login),
    url('send_sms',views.send_sms),
]