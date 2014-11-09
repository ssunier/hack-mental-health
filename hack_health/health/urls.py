from django.conf.urls import patterns, url
from health import views


urlpatterns = patterns('',
  url(r'^$', views.index, name='index'),
  url(r'^visualizer$', views.visualizer, name='visualizer'),
  #url(r'^)
)