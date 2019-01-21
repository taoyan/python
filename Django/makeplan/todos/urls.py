from django.urls import path
from django.conf.urls import url
from . import views

app_name = 'todos'
urlpatterns = [
    url('regist/',views.regist),
    url('login/',views.login),
    url('index/',views.index),
    url('logout/',views.logout),
]