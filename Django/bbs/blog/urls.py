
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'login/$',views.login),
    url(r'index/$',views.index),
    url(r'logout/$', views.logout),
    url(r'register/$', views.register),

    url(r'bootstrap01',views.bootstrap),
    url(r'bootstrap02',views.bootstrap2),
    url(r'font_awesome',views.font_awesome),
    url(r'nav',views.nav),
    url(r'panel',views.panel),
    url(r'carousel',views.carousel),
]