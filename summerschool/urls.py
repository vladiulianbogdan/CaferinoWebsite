from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    path("details/<int:id>/", views.detaliu, name='details'),
    path("register/<int:id>/", views.register, name='details'),
]