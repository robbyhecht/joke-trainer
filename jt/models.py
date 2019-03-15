from django.contrib.auth.models import User
from django.db import models


    

class Joke(models.Model):
  '''joke model'''
  hint = models.CharField(max_length=50, blank=False)
  question = models.CharField(max_length=170, blank=False)
  answer = models.CharField(max_length = 65, blank=False)
  creator = models.ForeignKey(User, on_delete=models.CASCADE, null=True, related_name='creator')
  user = models.ManyToManyField(User, blank=True, through='UserJoke')

  # @property
  # def is_favorite(self):
  #   favorite_jokes = UserJoke.objects.filter(joke = self.id)
  #   is_favorite_joke = False
  #   if favorite_jokes:
  #     is_favorite_joke = True
  #   return is_favorite_joke
    
  def __str__(self):
    return self.hint

  class Meta:
    ordering = ('question',)

class Category(models.Model):
  '''joke categories'''
  name = models.CharField(max_length=21, blank=False)
  joke = models.ManyToManyField(Joke, blank=True, through='JokeCategory')

  def __str__(self):
    return self.name

  class Meta:
    ordering = ('name',)

class JokeCategory(models.Model):
  '''join class for the many to many connection between jokes and their categories'''
  category = models.ForeignKey(Category, on_delete=models.CASCADE)
  joke = models.ForeignKey(Joke, on_delete=models.CASCADE)

class UserJoke(models.Model):
  '''join class for users' favorite jokes'''
  user = models.ForeignKey(User, on_delete=models.CASCADE)
  joke = models.ForeignKey(Joke, on_delete=models.CASCADE)

  def __str__(self):
    return self.joke.hint