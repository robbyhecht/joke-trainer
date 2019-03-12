from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from jt.models import Category, Joke, JokeCategory, UserJoke
from jt.forms import NewJokeForm

# helper function used by add and edit new joke functions
def add_joke_category(form_category, joke):
  for category_id in form_category:
    category = Category.objects.get(pk=category_id)
    joke_category_pairing = JokeCategory.objects.filter(joke=joke, category=category)
    if joke_category_pairing:
      pass
    else:
      JokeCategory.objects.create(joke=joke, category=category)

@login_required
def add_joke(request):
  '''Handles user adding a new joke to the database'''

  if request.method == "GET":
    newjoke_form = NewJokeForm()
    template_name = 'new_joke.html'
    return render(request, template_name, {'newjoke_form': newjoke_form})

  elif request.method == "POST":
    creator = request.user
    question = request.POST["question"]
    answer = request.POST["answer"]
    hint = request.POST["hint"]
    category = request.POST.getlist("category")
    new_joke = Joke(creator=creator, question=question, answer=answer, hint=hint)
    new_joke.save()
    print('NEW JOKE ADDED?', new_joke.id)

    add_joke_category(request.POST["category"], new_joke)

    return HttpResponseRedirect(reverse('jt:random_joke'))

def edit_joke(request, pk):
  if request.method == "GET":
    newjoke_form = NewJokeForm()
    joke = Joke.objects.get(pk=pk)
    category = Category.objects.all()
    context = {
      "joke": joke,
      "category": category,
      "id": joke.id, 
      "edit": True,
      "route": "jt:edit_joke",
      "question": joke.question,
      "answer": joke.answer,
      "hint": joke.hint,
      "newjoke_form": newjoke_form
    }
    return render(request, 'jt/new_joke.html', context)

  if request.method == "POST":
    joke_to_edit = Joke.objects.get(pk=pk)
    category = Category.objects.get(pk=request.POST["category"])
    joke_to_edit.question = request.POST["question"]
    joke_to_edit.answer = request.POST["answer"]
    joke_to_edit.hint = request.POST["hint"]
    joke_to_edit.save()

    addSongAlbum(request.POST["albums"], song_to_edit)
    add_joke_category(request.POST["category"], joke_to_edit)

    return HttpResponseRedirect(reverse('jt:random_joke'))
    