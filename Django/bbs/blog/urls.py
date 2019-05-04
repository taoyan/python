
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'up_down/$',views.up_down),
    url(r'comment/$', views.comment),
    url(r'comment_tree/(\d+)/$', views.comment_tree),
    url(r'backend/add_article/', views.add_article),
    url(r'(\w+)/article/(\d+)/$', views.article_detail),
    url(r'(\w+)/$',views.home),





    url(r'bootstrap01',views.bootstrap),
    url(r'bootstrap02',views.bootstrap2),
    url(r'font_awesome',views.font_awesome),
    url(r'nav',views.nav),
    url(r'panel',views.panel),
    url(r'carousel',views.carousel),
    url(r'dashboard',views.dashboard),
]