from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from jt.models import Category

# from jt.forms import UserForm, ProductForm
# from jt.models import Product

def index(request):
  template_name = 'index.html'
  return render(request, template_name, {})

def joke(request):
  template_name = 'joke.html'
  return render(request, template_name, {})

