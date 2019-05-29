from django.conf.urls import url

from . import views

urlpatterns = [
    url('^register/$',views.register),
    url('^login/$',views.login),
    url('^logout/$',views.logout),

    url('^send_sms_regist/$',views.send_sms_regist),
    url('^send_sms_login/$',views.send_sms_login),
    url('^send_sms/$',views.send_sms),

    url('^BindNewMobile/$',views.bind_new_mobile),
    url('^ModifyPassword/$', views.modify_password),
    url('^userInfo/$',views.user_info),
]