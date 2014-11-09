from django.conf.urls import *
from django.contrib import admin
<<<<<<< HEAD
#admin.autodiscover()
=======
from django.contrib.auth.models import User

>>>>>>> aab57816fc342a78ff54fe92927fdf5997595bc0

from health import views

urlpatterns = [
    url(r'^health/', include('health.urls')),
    url(r'^admin/', include(admin.site.urls)),
#    url(r'^$', views.index, name='index')
]
