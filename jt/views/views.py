from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from jt.models import Category

# from jt.forms import UserForm, ProductForm
# from jt.models import Product

def index(request):
  template_name = 'index.html'
  return render(request, template_name, {})

  # ---DECIDE HOW UNIVERSAL THIS SIDEBAR WILL BE... BASE? INDEX?, OTHER?---

def list_categories(request):
  '''Handles listing joke categories in sidebar'''
  # retrieves all categories
  category_list = Category.objects.all()
  # creates a dictionary to pass departments and employees to the HTML template
  context ={'category_list' : category_list}
  return render(request, 'index.html', context)

def joke(request):
  template_name = 'joke.html'
  return render(request, template_name, {})

