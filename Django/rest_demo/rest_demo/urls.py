"""rest_demo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""

from django.conf.urls import url, include
from django.contrib import admin
from app01 import views

from rest_framework import routers
routers = routers.DefaultRouter()
routers.register(r"authors",views.AuthorModelView)


urlpatterns = [
    url(r"", include(routers.urls)),
    url(r'^admin/', admin.site.urls),

    url(r'^publishers/$', views.PublishView.as_view(), name="publishs"),
    url(r'^publishers/(?P<pk>\d+)/$', views.PublishViewDetail.as_view(), name="publish_detail"),

    url(r'^books/$',views.BookView.as_view(), name="books"),
    url(r'^books/(\d+)/$', views.BookDetailView.as_view(), name="bood_detail"),

    # url(r'^authors/$',views.AuthorView.as_view(), name="authors"),
    # url(r'^authors/(?P<pk>\d+)/$', views.AuthorDetailView.as_view(), name="authors_detail"),

    # url(r'^authors/$',views.AuthorModelView.as_view({"get":"list","post":"create"}), name="authors"),
    # url(r'^authors/(?P<pk>\d+)/$', views.AuthorModelView.as_view({"get":"retrieve","put":"update","delete":"destroy"})),


    url(r'^login/$',views.LoginView.as_view()),
]
