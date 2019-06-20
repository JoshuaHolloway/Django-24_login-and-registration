from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.index),
    url(r'^users$', views.users),
    url(r'^users/reg_login', views.reg_login),
    url(r'^users/reg_login/reg', views.reg_login_reg)
]
