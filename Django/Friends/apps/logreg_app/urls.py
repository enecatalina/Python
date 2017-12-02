from django.conf.urls import url, include
from django.contrib import admin
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index, name = 'index'),
    url(r'^create$', views.create, name = 'create'),
    url(r'^success$', views.success, name = "success"),
    url(r'^login$', views.login, name = "login"),
    url(r'^user/(?P<user_id>\d+)$', views.show, name = 'show'),
    url(r'^user/add/(?P<id>\d+)$', views.add_friend),
    url(r'^user/remove/(?P<id>\d+)$', views.remove),
    url(r'^logout$', views.logout, name = "logout"),
]