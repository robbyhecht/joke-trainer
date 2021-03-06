from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from jt.models import Category, Joke, JokeCategory, UserJoke
from django.core.paginator import Paginator

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
  all_joke_content = Joke.objects.filter(category = id)
  joke_content = list()
  for joke in all_joke_content:
    if joke.creator_id is None or joke.creator_id == request.user.id:
      joke_content.append(joke)

  # assures there is a user before trying to access UserJoke table: an action which requires an active user.
  if request.user.is_authenticated:
    # retrieves the joke objects included in the UserJoke table
    faved_jokes = UserJoke.objects.filter(user = request.user)
    for joke in joke_content:
      joke.is_favorited_by_user = False
      for fav_joke in faved_jokes:
        if fav_joke.joke.id == joke.id:
          joke.is_favorited_by_user = True
  else: faved_jokes = Joke.objects.all()

  # pagination
  paginator = Paginator(joke_content, 5)
  page = request.GET.get('page')
  joke_content = paginator.get_page(page)

  context = { 'joke_category' : joke_category, 'joke_content' : joke_content, 'faved_jokes' : faved_jokes }

  return render(request, 'joke_category.html', context)


def list_my_jokes(request):
  '''Handles listing the jokes added by the user via the link in right sidebar'''
  my_joke_content = Joke.objects.filter(creator_id = request.user.id)
  joke_content = list()
  for joke in my_joke_content:
      joke_content.append(joke)

  # assures there is a user before trying to access UserJoke table: an action which requires an active user.
  if request.user.is_authenticated:
    # retrieves the joke objects included in the UserJoke table
    faved_jokes = UserJoke.objects.filter(user = request.user)
    for joke in joke_content:
      joke.is_favorited_by_user = False
      for fav_joke in faved_jokes:
        if fav_joke.joke.id == joke.id:
          joke.is_favorited_by_user = True
  else: faved_jokes = Joke.objects.all()

  # pagination
  paginator = Paginator(joke_content, 5)
  page = request.GET.get('page')
  joke_content = paginator.get_page(page)

  context = { 'joke_content' : joke_content }

  return render(request, 'my_jokes.html', context)


@login_required
def add_to_favorites(request):
  '''Handles adding the selected joke to UserJoke table'''
  user = request.user
  UserJoke.objects.create(joke_id = request.POST["joke_id"], user = user)
  # this return keeps user on the same page after doing the action
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))


def favorites_list(request):
  '''Handles listing jokes by user's favorites...
  User name is accessed in favorite_jokes
  joke_content filters using join table to match up jokes with user'''
  # accesses all jokes that match user's id in the join table
  filtered_jokes = UserJoke.objects.filter(user_id = request.user.id)
  # makes a list from the returned queryset
  joke_list = []
  for joke in filtered_jokes:
    joke_list.append(Joke.objects.get(pk = joke.joke.id))
  context = { 'joke_list' : joke_list }
  return render(request, 'favorite_jokes.html', context)


def random_joke(request):
  '''Handles displaying random question and answer on flip card on home page'''
  # get all jokes in random order
  all_random_jokes = Joke.objects.order_by("?")
  # make a list from queryset
  joke_at_random = list()
  for joke in all_random_jokes:
    if joke.creator_id is None or joke.creator_id == request.user.id:
      joke_at_random.append(joke)

  # to avoid crash, limit to authenticated users before filtering by user (if no user, only a joke with a null creator value will be diplayed)
  if request.user.is_authenticated:
    # filter by current user to establish connection with favorited jokes
    faved_jokes = UserJoke.objects.filter(user = request.user)
    for joke in joke_at_random:
      joke.is_favorited_by_user = False
      for fav_joke in faved_jokes:
        # compare each joke in the full collection to each joke in the user's favorited jokes
        if fav_joke.joke.id == joke.id:
          joke.is_favorited_by_user = True
  else: faved_jokes = Joke.objects.all()

  # return only the first random joke to the template with each page reload
  for joke in joke_at_random:
    return render (request, 'index.html', { 'joke_at_random' : joke, 'faved_jokes' : faved_jokes })