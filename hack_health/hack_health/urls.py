from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = [
    # Examples:
    # url(r'^$', 'hack_health.views.home', name='home'),
    url(r'^admin/', include(admin.site.urls)),
    url(r'^health/', include('health.urls')),
]
