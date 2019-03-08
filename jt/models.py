from django.contrib.auth.models import User
from django.db import models


    

class Joke(models.Model):
  '''joke model'''
  hint = models.CharField(max_length=100, blank=False)
  question = models.CharField(max_length=500, blank=False)
  answer = models.CharField(max_length = 500, blank=False)
  user = models.ManyToManyField(User, blank=True, through='UserJoke')

  # @property
  def is_favorite(self):
    favorite_jokes = UserJoke.objects.filter(joke = self.id)
    is_favorite_joke = False
    if favorite_jokes:
      is_favorite_joke = True
    return is_favorite_joke
    
  

  def __str__(self):
    return self.hint


class Category(models.Model):
  '''joke categories'''
  name = models.CharField(max_length=50, blank=False)
  joke = models.ManyToManyField(Joke, blank=True, through='JokeCategory')

  def __str__(self):
    return self.name

class JokeCategory(models.Model):
  '''join class for the many to many connection between jokes and their categories'''
  category = models.ForeignKey(Category, on_delete=models.PROTECT)
  joke = models.ForeignKey(Joke, on_delete=models.PROTECT)

class UserJoke(models.Model):
  '''join class for users' favorite jokes'''
  user = models.ForeignKey(User, on_delete=models.PROTECT)
  joke = models.ForeignKey(Joke, on_delete=models.PROTECT)

  def __str__(self):
    return self.joke.question