from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    url("aurel-vlaicu", views.aurelVlaicu, name='aurel-vlaicu'),
    url("parcul-circului", views.parculCircului, name='parcul-circului'),
    path("detaliu/<int:id>/", views.detaliu, name='detaliu'),
    path("register/<int:id>/", views.register, name='detaliu'),
]
