from django.conf.urls import url

from django.urls import path
from . import views

urlpatterns = [
    url('synchronizeTodo',views.synchronize_todo),
]