"""caferino URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls import include, url

from django.conf.urls.static import static
from caferino import settings

urlpatterns = [
    path('admin/', admin.site.urls),
    path("", include('cfhomepage.urls')),
    url(r'^ateliere/', include('ateliere.urls')),
    url(r'^petreceri/', include('summerschool.urls')),
    url(r'^after-school/', include('afterschool.urls')),
    url(r'^blog/', include('blog.urls')),
    url(r'^calendar/', include('caferinocalendar.urls')),
]
