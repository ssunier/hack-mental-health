from django.http import HttpResponseRedirect, HttpResponse, Http404
from django.template import RequestContext, Context, loader
from django.shortcuts import render, redirect

import pywapi as weather

from health.models import Mood, MoodForm, Weather

# Create your views here.
def index(request, template_name='index.html'):
  
  form = MoodForm(request.POST or None)
  if form.is_valid():
    mood_id = request.POST.get('mood_id', '')
    # get the mood associated with that mood_id
    m=Mood.objects.get(happiness=mood_id)

    #get the weather data
    w=weather.get_weather_from_weather_com("SFXX8501",units="metric")
    temp = w['current_conditions']['temperature']
    w_text = w['current_conditions']['text'] #e.g. cloudy
    #w1 is a new weather object
    w1 = Weather(temperature=temp, weather=w_text)
    w1.save()
    # retrieve that latest weather object so you can save it in day

    
    return redirect('/health')

  return render(request, template_name, {'form': form})

def visualizer(request):
  template = loader.get_template('visualizer.html')
  context = Context({''})
  return HttpResponse(template.render(context))