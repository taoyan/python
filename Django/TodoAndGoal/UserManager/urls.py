
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^users/$' ,views.UserInfoModelView.as_view({"get" :"list" ,"post" :"create"}), name="user"),
    url(r'^users/(?P<pk>\d+)/$', views.UserInfoModelView.as_view({"get" :"retrieve" ,"put" :"update" ,"delete" :"destroy"})),
]