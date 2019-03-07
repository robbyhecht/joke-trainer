from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from jt.models import Joke, UserJoke, User

@login_required
def favorites_list(request):
  '''Handles listing jokes by user's favorites...
  User name is accessed in favorite_jokes
  joke_content filters using join table to match up jokes with user'''
  filtered_jokes = UserJoke.objects.filter(user_id = request.user.id)
  joke_list = []
  for joke in filtered_jokes:
    joke_list.append(Joke.objects.get(pk = joke.joke.id))
  print('EMPTY', joke_list)
  context = { 'joke_list' : joke_list }
  print("faves", context)
  return render(request, 'favorite_jokes.html', context)

@login_required
def favorites_train(request):
  '''Handles listing jokes by user's favorites...
  User name is accessed in favorite_jokes
  joke_content filters using join table to match up jokes with user'''
  filtered_jokes = UserJoke.objects.filter(user_id = request.user.id)
  joke_list = []
  for joke in filtered_jokes:
    joke_list.append(Joke.objects.get(pk = joke.joke.id))
  print('EMPTY', joke_list)
  context = { 'joke_list' : joke_list }
  print("faves", context)
  return render(request, 'favorite_trainer.html', context)