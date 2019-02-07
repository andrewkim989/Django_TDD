from django.conf.urls import url
from . import views

urlpatterns = [
    url(r"^$", views.index),
    url(r"^album/create$", views.create),
    url(r'^album/(?P<id>\d+)/edit$', views.edit),
    url(r'^album/(?P<id>\d+)/delete$', views.delete),
    url(r'^album/(?P<id>\d+)$', views.read),
    url(r"^user/new$", views.newUser),
    url(r'^user/(?P<id>\d+)/edit$', views.editUser),
    url(r'^user/(?P<id>\d+)/delete$', views.deleteUser),
    url(r'^user/(?P<id>\d+)$', views.getUser)
]
