from django.conf.urls import url
from . import views

urlpatterns = [
    # 书相关
    url(r'^book_list/',views.book_list, name='book_list'),
    # url(r'^add_book/', views.add_book),
    url(r'^add_book/', views.AddBook.as_view(), name='add_book'),
    # url(r'^delete_book/',views.delete_book),
    # url(r'^delete_book/([0-9]+)/$',views.delete_book),                  #url分组,位置参数
    url(r'^delete_book/(?P<id>[0-9]+)/$', views.delete_book, name='delete_book'), # url分组,关键字参数
    url(r'^edit_book/', views.edit_book, name='edit_book'),

    # 作者相关
    url(r'^author_list/', views.author_list),
    url(r'^add_author/', views.add_author),
    url(r'^delete_author/', views.delete_author),
    url(r'^edit_author/', views.edit_author),
]