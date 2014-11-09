from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, Context, loader

from health.models import Mood

# Create your views here.
def index(request):
  template = loader.get_template('index.html')
  context = Context({''})
  return HttpResponse(template.render(context))

def visualizer(request):
  template = loader.get_template('visualizer.html')
  context = Context({''})
  return HttpResponse(template.render(context))

