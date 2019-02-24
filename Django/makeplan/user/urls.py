from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    url('register/',views.register),
    url('login/',views.login),
    url('send_sms_regist',views.send_sms_regist),
    url('send_sms_login',views.send_sms_login),
]