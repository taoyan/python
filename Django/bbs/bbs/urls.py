"""bbs URL Configuration

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
from django.views.static import serve
from django.conf import settings
from blog import views


def test01(request):
    from django.http import HttpResponse
    return HttpResponse("app01/book")

def list_view(request):
    from django.http import HttpResponse
    return HttpResponse("list_view")

def add_view(request):
    from django.http import HttpResponse
    return HttpResponse("add_view")

def change_view(request, id):
    from django.http import HttpResponse
    return HttpResponse("change_view")

def delete_view(request, id):
    from django.http import HttpResponse
    return HttpResponse("delete_view")

def get_urls2():
    temp = []

    temp.append(url(r'^$', list_view))
    temp.append(url(r'^add/$', add_view))
    temp.append(url(r'^(\d+)/change/$', change_view))
    temp.append(url(r'^(\d+)/delete/$', delete_view))

    return temp

def get_urls():
    temp = []

    for model, admin_class_obj in admin.site._registry.items():
        app_name = model._meta.app_label
        model_name = model._meta.model_name
        temp.append(url(r'^{0}/{1}/'.format(app_name, model_name),
                        (get_urls2(), None, None)),)

    print(temp)
    return temp


urlpatterns = [
    url(r'^admin/', admin.site.urls),

    url(r'^Xadmin/',(get_urls(), None, None)),




    #
    # url(r'^media/(?P<path>.*)$', serve, {"document_root":settings.MEDIA_ROOT}),
    #
    # url(r'login/$',views.login),
    # url(r'index/$',views.index),
    # url(r'logout/$', views.logout),
    # #url(r'register/$', views.register),
    # url(r'register/$', views.register2),
    # url(r'check_username/$',views.check_username),
    #
    #
    # url(r'^upload/',views.upload),
    # url(r'blog/', include('blog.urls')),


]
