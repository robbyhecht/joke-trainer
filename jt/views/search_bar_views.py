from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from jt.models import Joke, UserJoke

def search(request):
  """Shows retrieved jokes when the user makes a search in the navbar search field"""
  # post the query and retrieve jokes that match the query
  if request.method == "POST":
    search_query = request.POST["search_query"]
    if search_query is not "":
      all_joke_content = Joke.objects.filter(question__contains=search_query)

      # loop through queryset make a list of the jokes
      joke_content = list()
      for joke in all_joke_content:
        if joke.creator_id is None or joke.creator_id == request.user.id:
          joke_content.append(joke)
          print("SEARCH RESULTS", joke_content)

      # must check for authentication before checking user table to avoid crash if no user is logged in
      if request.user.is_authenticated:
        # limit jokes searched to those visible to current user
        faved_jokes = UserJoke.objects.filter(user = request.user)
        for joke in joke_content:
          joke.is_favorited_by_user = False
          for fav_joke in faved_jokes:
            if fav_joke.joke.id == joke.id:
              joke.is_favorited_by_user = True
      else: faved_jokes = Joke.objects.all()

      context = { 
        "joke_content" : joke_content, 
        "search_query" : search_query, 
        "number_of" : len(joke_content),
        "no_jokes_found" : True if len(joke_content) is 0 else False
      }
      print("CONTEXT", context)

    # or else, if query is empty
    else:
      context = {
        "no_jokes_found" : True,
        "search_query" : search_query,
      }

    return render (request, "search_results.html", context)

  else:
    return HttpResponseRedirect(reverse("jt:random_joke"))