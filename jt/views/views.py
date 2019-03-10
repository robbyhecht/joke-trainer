from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render
from django.template import RequestContext
from django.urls import reverse
from django.db.models import Q
from jt.models import Category, User
from jt.forms import UserForm, LoginForm
import operator

def index(request):
  template_name = 'index.html'
  return render(request, template_name, {})

def about(request):
  template_name = 'about.html'
  return render(request, template_name, {})

def hi_user(request):
  users_name = User.objects.all()
  context = { 'users_name' : users_name }
  return render(request, 'index.html', context)

def nav_favorites(request, id):
  current_user = get_object_or_404(User, pk= id)
  context = { 'current_user' : current_user }
  return render(request, 'navbar.html', context)

def search_bar(request):
  result = request.get_queryset()
  query = self.request.GET.get('q')

  if query:
    query_list = query.split()
    result = result.filter(
      reduce(operator.and_,
        (Q(question__icontains=q) for q in query_list)) |
      reduce(operator.and_,
        (Q(answer__icontains=q) for q in query_list))
    )
  return result



# class BlogSearchListView(BlogListView):
#     """
#     Display a Blog List page filtered by the search query.
#     """
#     paginate_by = 10

#     def get_queryset(self):
#         result = super(BlogSearchListView, self).get_queryset()

#         query = self.request.GET.get('q')
#         if query:
#             query_list = query.split()
#             result = result.filter(
#                 reduce(operator.and_,
#                        (Q(title__icontains=q) for q in query_list)) |
#                 reduce(operator.and_,
#                        (Q(content__icontains=q) for q in query_list))
#             )

#         return result



def register(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # A boolean value for telling the template whether the registration was successful.
    # Set to False initially. Code changes value to True when registration succeeds.
    registered = False

    # Create a new user by invoking the `create_user` helper method
    # on Django's built-in User model
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)

        if user_form.is_valid():
            # Save the user's form data to the database.
            user = user_form.save()

            # Now we hash the password with the set_password method.
            # Once hashed, we can update the user object.
            user.set_password(user.password)
            user.save()

            # Update our variable to tell the template registration was successful.
            registered = True
            user_id = user.id

        return login_user(request)

    elif request.method == 'GET':
        user_form = UserForm()
        template_name = 'register.html'
        return render(request, template_name, {'user_form': user_form,})


def login_user(request):
    '''Handles the creation of a new user for authentication

    Method arguments:
      request -- The full HTTP request object
    '''

    # Obtain the context for the user's request.
    # print('CONTEXT', next_route)

    # If the request is a HTTP POST, try to pull out the relevant information.

    if request.method == 'POST':
      login_form = LoginForm(data=request.POST)

      # Use the built-in authenticate method to verify
      username=request.POST['username']
      password=request.POST['password']
      authenticated_user = authenticate(username=username, password=password)

        # If authentication was successful, log the user in
      if authenticated_user is not None:
          login(request=request, user=authenticated_user)
          if request.POST.get('next') == '/':
            return HttpResponseRedirect('/')
          else:
           return HttpResponseRedirect(request.POST.get('next', '/'))

      else:
          # Bad login details were provided. So we can't log the user in.
          print("Invalid login details: {}, {}".format(username, password))
          return HttpResponse("Invalid login details supplied.")

    elif request.method == 'GET':
      login_form = LoginForm()
      context = {'next': request.GET.get('next', '/')
, 'login_form': login_form,}
      template_name = 'login.html'
      return render(request, template_name, context)


  # Use the login_required() decorator to ensure only those logged in can access the view.
@login_required
def user_logout(request):
    # Since we know the user is logged in, we can now just log them out.
    logout(request)

    # Take the user back to the homepage. Is there a way to not hard code
    # in the URL in redirects?????
    return HttpResponseRedirect('/')