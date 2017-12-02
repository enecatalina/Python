from django.conf.urls import url, include
from django.contrib import admin
from . import views           # This line is new!

urlpatterns = [
    url(r'^$', views.index, name="index"),
    url(r'^add$', views.add, name="add"),
    url(r'^(?P<book_id>\d+)$', views.show, name = "success",)
]