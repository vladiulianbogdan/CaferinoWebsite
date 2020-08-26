from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'detaliu', views.detaliu, name='detaliu'),
    path("register/<int:id>/", views.register, name='detaliu'),
]