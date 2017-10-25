from django.conf.urls import url
from django.contrib import admin
from . import views


urlpatterns = [
    url(r'^dashboard$', views.dashboard),
    url(r'^account/(?P<id>\d+)$', views.showUser),
]
