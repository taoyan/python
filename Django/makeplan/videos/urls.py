
from django.conf.urls import url
from . import views

app_name = 'videos'
urlpatterns = [
    url('index/',views.videos),
    # url('videos/',views.videos),
    url('detail/<int:video_id>/',views.detail),

    # url('add/',views.add_video),
    # url('download/Media/<str:file_name>/', views.download),
    # url('delete', views.delete_video),
    # url('update/<int:video_id>/', views.update),
]