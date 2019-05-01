
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'(?P<username>\w+)',views.home),



    url(r'bootstrap01',views.bootstrap),
    url(r'bootstrap02',views.bootstrap2),
    url(r'font_awesome',views.font_awesome),
    url(r'nav',views.nav),
    url(r'panel',views.panel),
    url(r'carousel',views.carousel),
    url(r'dashboard',views.dashboard),
]