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


  elif request.method == "POST":
    joke.question = request.POST["question"]
    joke.answer = request.POST["answer"]
    joke.hint = request.POST["hint"]
    joke.save()

    return HttpResponseRedirect(reverse('jt:random_joke'))


def delete_joke(request, id):
  '''Handles deletion of a joke from the Joke table- only accessible if creator_id matches user'''
  joke_for_deletion = Joke.objects.get(pk=id)
  joke_for_deletion.delete()
  return HttpResponseRedirect(reverse("jt:random_joke"))





  # elif request.method == "POST":
  #   joke = Joke.objects.get(pk=id)
  #   joke.question = request.POST["question"]
  #   joke.answer = request.POST["answer"]
  #   joke.hint = request.POST["hint"]
  #   joke.save()

  #   addSongAlbum(request.POST["albums"], song_to_edit)
  #   add_joke_category(request.POST["category"], joke_to_edit)

  #   return HttpResponseRedirect(reverse('jt:random_joke'))




  #   def editEmployee(request, employee_id):
  # # if you're not currently on the add employee page
  # if request.method == "GET":
  #   # get specific employee object by id
  #   employee = Employee.objects.get(id=employee_id)
  #   # get all dept objects for template dropdown
  #   department_list = Department.objects.all()
  #   # make variables for properties on employee
  #   first_name = employee.first_name
  #   last_name = employee.last_name
  #   start_date = str(employee.start_date)
  #   is_supervisor = employee.is_supervisor
  #   department = employee.department
  #   # context holds employee dictionary
  #   context = {"employee" : employee, "department_list" : department_list, "first_name" : first_name, "last_name" : last_name, "start_date" : start_date, "is_supervisor" : is_supervisor, "department" : department}
  #   # request url, reference template, and give it context
  #   return render(request, 'HR/employee/editEmployee.html', context)




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