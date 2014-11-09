from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, Context

from health.models import Mood

# Create your views here.
def index(request):
  return HttpResponse('hello you are at the index')
