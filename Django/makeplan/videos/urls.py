
from django.conf.urls import url
from . import views

app_name = 'videos'
urlpatterns = [
    url('^index/$',views.videos),
    url('^videos$',views.videos),
    url('^detail/(\d+).html$',views.detail),
    url('^detail$',views.detail2),


    url('^bookmark$',views.bookmark),                     #收藏/取消收藏
    url('^myBookmarks$',views.my_bookmarks),          #收藏列表


    # url('add/',views.add_video),
    # url('download/Media/<str:file_name>/', views.download),
    # url('delete', views.delete_video),
    # url('update/<int:video_id>/', views.update),
]