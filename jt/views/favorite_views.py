from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from jt.models import Joke, UserJoke

def favorites_list(request, id):
  '''Handles listing jokes by user's favorites...
  User name is accessed in favorite_jokes
  joke_content filters using join table to match up jokes with user'''
  favorite_jokes = get_object_or_404(User, pk= id)
  joke_content = Joke.objects.filter(user = id)
  context = { 'favorite_jokes' : favorite_jokes, 'joke_content' : joke_content }
  print("faves", context)
  return render(request, 'favorite_jokes.html', context)