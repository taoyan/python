
from django.conf.urls import url
from . import views

app_name = 'videos'
urlpatterns = [
    url('index/',views.index),
]