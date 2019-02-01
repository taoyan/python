
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'videos'
urlpatterns = [
    url('index/',views.index),
    url('add/',views.add_video),
    path('download/Media/<str:file_name>/', views.download),
    url('detail/',views.detail),
]