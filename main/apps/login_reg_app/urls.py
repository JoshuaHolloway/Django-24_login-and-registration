from django.conf.urls import url
from . import views

urlpatterns = [
    # 0. Root
    url(r'^$', views.index),

    # 1. Show table
    url(r'^users$', views.users),

    # TODO:
    # 2. Show row
    url(r'^users/(?P<user_id>\d+)$', views.users_showUser),  # localhost:8000/shows/<id>

    # 3. Register and Login
    url(r'^users/reg_login', views.reg_login),
    url(r'^users/reg', views.register),
    url(r'^users/login', views.login),
    url(r'^users/logout', views.logout),

    # TODO:
    # 4. Edit
    # 5. Delete
]
