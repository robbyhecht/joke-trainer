from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from jt.models import Category, Joke, JokeCategory, UserJoke
from jt.forms import NewJokeForm

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

    for category_id in category:
      category = Category.objects.get(pk=category_id)
      JokeCategory.objects.create(joke=new_joke, category=category)
      request.POST["category"], new_joke

    return HttpResponseRedirect(reverse('jt:random_joke'))


def delete_joke(request, id):
  '''Handles deletion of a joke from the Joke table- only accessible if creator_id matches user'''
  joke_for_deletion = Joke.objects.get(pk=id)
  joke_for_deletion.delete()
  return HttpResponseRedirect(reverse("jt:random_joke"))



  #   def delete_joke(request, pk):
  # '''Handles deletion of a joke from the Joke table- only accessible if creator_id matches user'''
  # joke = Joke.objects.get(pk = id)
  # Joke.objects.filter(creator = request.creator).get(joke = joke).delete()
  # return HttpResponseRedirect(reverse("jt:random_joke"))



# def remove_from_favorites(request, id):
#   '''Handles deletion of a joke from the UserJoke table (a.k.a. favorites)'''
#   joke = Joke.objects.get(pk = id)
#   UserJoke.objects.filter(user = request.user).get(joke = joke).delete()
#   return HttpResponseRedirect(reverse("jt:favorites"))



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





