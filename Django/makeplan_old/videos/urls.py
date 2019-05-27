
from django.conf.urls import url
from django.urls import path
from . import views

app_name = 'videos'
urlpatterns = [
    url('index/',views.videos),
    url('videos/',views.videos),
    url('add/',views.add_video),
    path('download/Media/<str:file_name>/', views.download),
    path('detail/<int:video_id>/',views.detail),
    url('delete', views.delete_video),
    path('update/<int:video_id>/', views.update),
]