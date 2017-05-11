from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^$', views.index),
    url(r'^article/(?P<id>\d+)/$', views.article, name='article'),
    url(r'^edit/(?P<id>\d+)/$', views.edit, name='edit'),
    url(r'^edit/action$', views.editAction, name='editAction'),
]
