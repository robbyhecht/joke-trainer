from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from jt.models import Category, Joke, JokeCategory
from jt.forms import NewJokeForm, EditJokeForm

@login_required
def add_joke(request):
  '''Handles user adding a new joke to the database'''
  # render the add form
  if request.method == "GET":
    newjoke_form = NewJokeForm()
    template_name = 'new_joke.html'
    return render(request, template_name, {'newjoke_form': newjoke_form})

  # save and post new joke
  elif request.method == "POST":
    creator = request.user
    question = request.POST["question"]
    answer = request.POST["answer"]
    hint = request.POST["hint"]
    category = request.POST.getlist("category")
    new_joke = Joke(creator=creator, question=question, answer=answer, hint=hint)
    new_joke.save()
    print('NEW JOKE ADDED?', new_joke.id)

    # also save any joke-category relationships to the join table
    for category_id in category:
      category = Category.objects.get(pk=category_id)
      JokeCategory.objects.create(joke=new_joke, category=category)
      request.POST["category"], new_joke

    # return to the home page
    return HttpResponseRedirect(reverse('jt:random_joke'))


def edit_joke(request, id):
  '''Handles editing an existing joke'''
  # retrieves the form
  joke = Joke.objects.get(pk=id)
  if request.method == "GET":
    editjoke_form = EditJokeForm(instance=joke)
    question = joke.question
    answer = joke.answer
    hint = joke.hint
    template_name = 'edit_joke.html'
    context = { "joke" : joke, "question" : question, "answer" : answer, "hint" : hint, "editjoke_form" : editjoke_form }
    print("CONTEXT", context)
    return render(request, template_name, context)

  # save the edited joke
  elif request.method == "POST":
    joke.question = request.POST["question"]
    joke.answer = request.POST["answer"]
    joke.hint = request.POST["hint"]
    joke.save()

    # specifies destination after action... in this case, returning to the joke's location
    next = request.POST.get('next', '/')
    return HttpResponseRedirect(next)


def delete_joke(request, id):
  '''Handles deletion of a joke from the Joke table- only accessible if creator_id matches user'''
  joke_for_deletion = Joke.objects.get(pk=id)
  joke_for_deletion.delete()
  # maintains location following action
  return HttpResponseRedirect(request.META.get('HTTP_REFERER'))