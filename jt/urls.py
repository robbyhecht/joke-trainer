from django.conf.urls import include
from django.urls import path
from jt import views


app_name = "jt"
urlpatterns = [
  path('', views.list_categories, name='list_categories'),
  # path('', views.random_joke, name='random_joke'),
  path('category/<int:id>', views.list_by_category, name='list_by_category'),
  
  path('joke/', views.joke, name='joke'),
]