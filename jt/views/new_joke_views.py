from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, get_object_or_404
from django.template import RequestContext
from django.urls import reverse
from jt.models import Category, Joke, JokeCategory, UserJoke
from jt.forms import NewJokeForm, EditJokeForm

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
      from jt.forms import EditJokeForm

    return HttpResponseRedirect(reverse('jt:random_joke'))


def delete_joke(request, id):
  '''Handles deletion of a joke from the Joke table- only accessible if creator_id matches user'''
  joke_for_deletion = Joke.objects.get(pk=id)
  joke_for_deletion.delete()
  return HttpResponseRedirect(reverse("jt:random_joke"))




def edit_joke(request, id):
  '''Handles editing an existing joke'''
  # retrieves the form
  if request.method == "GET":
    editjoke_form = EditJokeForm()
    joke = Joke.objects.get(pk=id)
    category_list = Category.objects.all()
    question = joke.question
    answer = joke.answer
    hint = joke.hint
    template_name = 'edit_joke.html'

    context = { "joke" : joke, "category_list" : category_list, "question" : question, "answer" : answer, "hint" : hint, "editjoke_form" : editjoke_form }
    return render(request, template_name, context)


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



  # if you're on the edit employee page
  if request.method == "POST":
    # get employee object
    employee = Employee.objects.get(id=employee_id)
    # make variables from individual post requests
    employee.first_name = request.POST["first_name"]
    employee.last_name = request.POST["last_name"]
    employee.start_date = request.POST["start_date"]
    employee.is_supervisor = request.POST["is_supervisor"]
    # department is a foreign key, so use department's pk
    employee.department_id = get_object_or_404(Department, pk=request.POST["department_id"])
    employee.save()
    # use url name from urls plus id extension using kwargs and dictionary to assign employee.id
    return HttpResponseRedirect(reverse('HR:employeeDetail', kwargs={'id' : employee.id}))











# def edit_joke(request, pk):
#   if request.method == "GET":
#     newjoke_form = NewJokeForm()
#     joke = Joke.objects.get(pk=pk)
#     category = Category.objects.all()
#     context = {
#       "joke": joke,
#       "category": category,
#       "id": joke.id, 
#       "edit": True,
#       "route": "jt:edit_joke",
#       "question": joke.question,
#       "answer": joke.answer,
#       "hint": joke.hint,
#       "newjoke_form": newjoke_form
#     }
#     return render(request, 'jt/new_joke.html', context)

#   if request.method == "POST":
#     joke_to_edit = Joke.objects.get(pk=pk)
#     category = Category.objects.get(pk=request.POST["category"])
#     joke_to_edit.question = request.POST["question"]
#     joke_to_edit.answer = request.POST["answer"]
#     joke_to_edit.hint = request.POST["hint"]
#     joke_to_edit.save()

#     addSongAlbum(request.POST["albums"], song_to_edit)
#     add_joke_category(request.POST["category"], joke_to_edit)

#     return HttpResponseRedirect(reverse('jt:random_joke'))