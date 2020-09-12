from django.conf.urls import url
from django.urls import include, path

from . import views

urlpatterns = [
    path("", views.index, name='index'),
    path("proiecte_sociale", views.social_projects, name='index'),
    path("reguli", views.rules, name='index'),
    path("covid", views.covid, name='index'),
    path("politica-de-confidentialitate", views.gdpr, name='index'),
    path("contact", views.contact, name='index'),
    path("club", views.club, name='index'),
]