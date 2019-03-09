from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from jt.models import Category, Joke, JokeCategory, UserJoke

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
  # for listing category name
  joke_category = get_object_or_404(Category, pk= id)
  # for retrieving the joke details to have on cards
  joke_content = Joke.objects.filter(category = id)
  # retrieves the joke objects included in the userjoke table
  if request.user.is_authenticated: # -> because of the loop below, this method crashes if no user is logged in. Therefore, this if statement is required to eliminate the filter in the case of user not being logged in.
    faved_jokes = UserJoke.objects.filter(user = request.user)
    for joke in joke_content:
      joke.is_favorited_by_user = False
      for fav_joke in faved_jokes:
        if fav_joke.joke.id == joke.id:
          joke.is_favorited_by_user = True
  else: faved_jokes = Joke.objects.all()
  context = { 'joke_category' : joke_category, 'joke_content' : joke_content, 'faved_jokes' : faved_jokes }
  return render(request, 'joke_category.html', context)

@login_required
def add_to_favorites(request):
  '''Handles adding the selected joke to UserJoke table'''
  print('REQUEST', request)
  user = request.user
  UserJoke.objects.create(joke_id = request.POST["joke_id"], user = user)
  return HttpResponseRedirect(reverse("jt:favorites"))

def favorites_list(request):
  '''Handles listing jokes by user's favorites...
  User name is accessed in favorite_jokes
  joke_content filters using join table to match up jokes with user'''
  filtered_jokes = UserJoke.objects.filter(user_id = request.user.id)
  joke_list = []
  for joke in filtered_jokes:
    joke_list.append(Joke.objects.get(pk = joke.joke.id))
  context = { 'joke_list' : joke_list }
  return render(request, 'favorite_jokes.html', context)


def random_joke(request):
  '''Handles displaying question and answer on flip card'''
  joke_at_random = Joke.objects.order_by("?").first()
  context = { 'joke_at_random' : joke_at_random }
  print('RANDOMJOKE', context)
  # return HttpResponseRedirect(reverse("jt:random_joke"))
  return render (request, 'index.html', context)



  
# def random_joke(request):
#   '''Handles displaying question and answer on flip card'''
#   import random
#   all_jokes = Joke.objects.all()
#   joke_at_random = random.sample(all_jokes, 1)
#   print(joke_at_random)
#   # return HttpResponseRedirect(reverse("jt:"))
#   return render (request, 'index.html', joke_at_random)

# def random_joke(request, id):
#   '''Handles displaying question and answer on flip card'''
#   joke = get_object_or_404(Joke, pk=id)
#   context = { 'joke' : joke }
#   print(context)
#   return render (request, 'index.html', context)