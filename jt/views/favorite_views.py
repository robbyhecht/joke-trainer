from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse
from jt.models import Joke, UserJoke, User
from django.core.paginator import Paginator


@login_required
def favorites_list(request):
  '''Handles listing jokes by user's favorites...
  User name is accessed in favorite_jokes
  joke_content filters using join table to match up jokes with user'''
  filtered_jokes = UserJoke.objects.filter(user_id = request.user.id).order_by('joke')
  joke_content = []
  for joke in filtered_jokes:
    joke_content.append(Joke.objects.get(pk = joke.joke.id))

  # pagination
  paginator = Paginator(joke_content, 5)
  page = request.GET.get('page')
  joke_content = paginator.get_page(page)

  context = { 'joke_content' : joke_content }
  print("faves", context)
  return render(request, 'favorite_jokes.html', context)


@login_required
def favorites_train(request):
  '''Handles listing jokes by user's favorites...
  User name is accessed in favorite_jokes
  joke_content filters using join table to match up jokes with user'''
  filtered_jokes = UserJoke.objects.filter(user_id = request.user.id).order_by('joke')
  joke_content = []
  for joke in filtered_jokes:
    joke_content.append(Joke.objects.get(pk = joke.joke.id))
  print('EMPTY', joke_content)

  # pagination
  paginator = Paginator(joke_content, 5)
  page = request.GET.get('page')
  joke_content = paginator.get_page(page)

  context = { 'joke_content' : joke_content }
  print("faves", context)
  return render(request, 'favorite_trainer.html', context)
  

def remove_from_favorites(request, id):
  '''Handles deletion of a joke from the UserJoke table (a.k.a. favorites)'''
  joke = Joke.objects.get(pk = id)
  UserJoke.objects.filter(user = request.user).get(joke = joke).delete()
  return HttpResponseRedirect(reverse("jt:favorites"))