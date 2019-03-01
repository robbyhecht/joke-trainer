from django.conf.urls import include
from django.urls import path
from jt import views


app_name = "jt"
urlpatterns = [
  path('', views.list_categories, name='list_categories'),
  path('joke/', views.joke, name='joke'),
]