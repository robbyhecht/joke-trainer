from django.contrib.auth.models import User
from ..models import Joke, Category
from django import forms

class UserForm(forms.ModelForm):
    
  username = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
  email = forms.EmailField(widget=forms.TextInput(attrs={'class':'input'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))
  first_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
  last_name = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))

  class Meta:
    model = User
    fields = ('username', 'email', 'password', 'first_name', 'last_name')

class LoginForm(forms.ModelForm):

  username = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
  password = forms.CharField(widget=forms.PasswordInput(attrs={'class':'input'}))

  class Meta:
    model = User
    fields = ('username', 'password')
    # next = form.fields['next'].widget = forms.HiddenInput()

class NewJokeForm(forms.ModelForm):

  question = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
  answer = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
  hint = forms.CharField(widget=forms.TextInput(attrs={'class':'input'}))
  category = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

  class Meta:
    model = Joke
    fields = ('question', 'answer', 'hint', 'category')
