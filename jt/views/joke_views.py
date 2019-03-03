from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from jt.models import Category, Joke, JokeCategory

def list_categories(request):
  '''Handles listing joke categories in sidebar'''
  # retrieves all categories
  category_list = Category.objects.all()
  # creates a dictionary to pass departments and employees to the HTML template
  context ={'category_list' : category_list}
  return render(request, 'index.html', context)

def random_joke(request, id):
  '''Handles displaying question and answer on flip card'''
  joke = get_object_or_404(Joke, pk=id)
  context = { 'joke' : joke }
  print(context)
  return render (request, 'index.html', context)

def list_by_category(request, id):
  '''Handles listing jokes by category...
  Category name is accessed in joke_category
  joke_content filters using join table to match up jokes with categories'''
  joke_category = get_object_or_404(Category, pk= id)
  joke_content = Joke.objects.filter(category = id)
  context = { 'joke_category' : joke_category, 'joke_content' : joke_content }
  print(context)
  return render(request, 'joke_category.html', context)
