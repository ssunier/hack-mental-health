from django.conf.urls import *
from django.contrib import admin
from django.contrib.auth.models import User


from health import views

urlpatterns = [
    url(r'^health/', include('health.urls')),
    url(r'^admin/', include(admin.site.urls)),
    #url(r'^$', views.index, name='index')
]
