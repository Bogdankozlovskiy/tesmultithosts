from django.urls import re_path, include

from . import views

urlpatterns = [
    re_path(r'articles/$', views.articles, name='articles'),
    re_path(r'articles/(?P<pk>\d+)/$', views.article_details, name='article_details'),
    re_path(r'', views.home, name='home'),
]
