from django.conf.urls import url
from . import views

app_name = 'friends'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^new$', views.new, name='new'),
    url(r'^user/(?P<id>\d+)$', views.user, name='user'),
    url(r'^delete/(?P<id>\d+)$', views.delete, name='delete'),
]
