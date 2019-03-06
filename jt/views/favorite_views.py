from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from jt.models import Joke, UserJoke, User

@login_required

def favorites_list(request, id):
  '''Handles listing jokes by user's favorites...
  User name is accessed in favorite_jokes
  joke_content filters using join table to match up jokes with user'''
  favorite_jokes = get_object_or_404(User, pk= id)
  joke_detail = Joke.objects.filter(user = id)
  context = { 'favorite_jokes' : favorite_jokes, 'joke_detail' : joke_detail }
  print("faves", context)
  return render(request, 'favorite_jokes.html', context)


def list_categories(request):
  '''Handles listing joke categories in sidebar'''
  # retrieves all categories
  category_list = Category.objects.all()
  # creates a dictionary to pass departments and employees to the HTML template
  context ={'category_list' : category_list}
  return render(request, 'index.html', context)

def list_by_category(request, id):
  '''Handles listing jokes by category...
  Category name is accessed in joke_category
  joke_content filters using join table to match up jokes with categories'''
  joke_category = get_object_or_404(Category, pk= id)
  joke_content = Joke.objects.filter(category = id)
  context = { 'joke_category' : joke_category, 'joke_content' : joke_content }
  print(context)
  return render(request, 'joke_category.html', context)