from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from jt.models import Joke, UserJoke

def search(request):
  """Shows retrieved jokes when the user makes a search in the navbar search field"""

  if request.method == "POST":
    search_query = request.POST("search_query")

    if search_query is not "":
      search_results = Joke.objects.filter(question__contains=search_query)

      if request.user.is_authenticated:
        faved_jokes = UserJoke.objects.filter(user = request.user)
        for joke in search_results:
          joke.is_favorited_by_user = False
          for fav_joke in faved_jokes:
            if fav_joke.joke.id == joke.id:
              joke.is_favorited_by_user = True
      else: faved_jokes = Joke.objects.all()

      context = { 
        "search_results" : search_results, 
        "search_query" : search_query, 
        "faved_jokes" : faved_jokes,
        "number_of" : len(results),
        "no_jokes_found" : True if len(results) is 0 else False
      }

    else:
      context = {
        "no_jokes_found" : True,
        "search_query" : search_query,
      }

    return render (request, "search_results.html", context)

  else:
    return HttpResponseRedirect(reverse("jt:search"))