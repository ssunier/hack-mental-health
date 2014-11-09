from django.shortcuts import render_to_response
from django.http import HttpResponseRedirect, HttpResponse, Http404
#from django.contrib.auth import authenticate, login

# Create your views here.
def index(request):
  return HttpResponse('this is where login should go')
  '''
  state = "Please log in below..."
  username = password = ''
  if request.POST:
      username = request.POST.get('username')
      password = request.POST.get('password')

      user = authenticate(username=username, password=password)
      if user is not None:
          if user.is_active:
              login(request, user)
              state = "You're successfully logged in!"
          else:
              state = "Your account is not active, please contact the site admin."
      else:
          state = "Your username and/or password were incorrect."

  return render_to_response('login.html',{'state':state, 'username': username})
  '''

def mood(request):
  return HttpResponse('this is where the mood will be asked')
