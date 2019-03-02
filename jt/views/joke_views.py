from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from jt.models import Category, Joke

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