from django.contrib.auth.models import User
from django import forms

COLOR_CHOICES = (
    ('red', 'Red'),
    ('green', 'Green'),
    ('blue', 'Blue')
)

class UserForm(forms.ModelForm):
    
    email = forms.EmailField()
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password', 'first_name', 'last_name',)

class LoginForm(forms.ModelForm):

    class Meta:
      model = User
      fields = ('username', 'password')