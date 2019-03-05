from django.contrib.auth.models import User
from django import forms

COLOR_CHOICES = (
  ('red', 'Red'),
  ('green', 'Green'),
  ('blue', 'Blue')
)

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