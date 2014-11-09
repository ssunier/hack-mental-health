from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets

from health import views

urlpatterns = [
    # Examples:
    # url(r'^$', 'hack_health.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^health/', include('health.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.index, name='index')
]
