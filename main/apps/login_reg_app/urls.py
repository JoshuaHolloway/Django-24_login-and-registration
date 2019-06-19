from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.users),
    url(r'^users/new', views.users_new),
]
