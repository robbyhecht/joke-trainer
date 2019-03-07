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
  joke_category = get_object_or_404(Category, pk= id)
  joke_content = Joke.objects.filter(category = id)
  context = { 'joke_category' : joke_category, 'joke_content' : joke_content }
  print(context)
  return render(request, 'joke_category.html', context)


@login_required
def add_to_favorites(request):
  '''Handles adding the selected joke to UserJoke table'''
  joke_to_add = Joke.objects.get(pk = joke.id)
  context = { 'joke_to_add' : joke_to_add }
  print('SELECTED JOKE', joke_to_add)
  return render(request, 'joke_category.html', context)


# @login_required
# def add_product_to_cart(request, product_details):
    
#     user_id = request.user.id
#     website_order_id = Order.objects.raw('''select * from website_order
#                                             Where deletedOn is null and customer_id = %s''', [user_id])[0]
#     print('website_order_id', website_order_id.id)
#     print('user_id', user_id)
#     with connection.cursor() as cursor:
#         try:
#             cursor.execute('''Insert into website_productorder (deletedOn, order_id, product_id)
#                             Values(NULL, %s, %s)''', [website_order_id.id, product_details])
#         except IndexError:
#             raise Http404("This product type does not exist")
#     return HttpResponseRedirect(reverse('website:cart'))





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


  
def random_joke(request, id):
  '''Handles displaying question and answer on flip card'''
  joke = get_object_or_404(Joke, pk=id)
  context = { 'joke' : joke }
  print(context)
  return render (request, 'index.html', context)

  
# def flip_the_card(request):
#   joke_card = get_object_or_404(Joke, pk= id)
#   joke_card.classList.toggle('flipit')
#   context = {'joke_card' : joke_card}
#   print('FLIPCARD', context)
#   return render(request, 'joke_category.html', context)