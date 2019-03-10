from django.conf.urls import include
from django.urls import path
from jt import views


app_name = "jt"
urlpatterns = [
  # path('', views.index, name='index'),
  path('', views.random_joke, name = 'random_joke'),
  path('categories', views.list_categories, name='list_categories'),
  path('login', views.login_user, name='login'),
  path('logout', views.user_logout, name='logout'),
  path('register', views.register, name='register'),
  path('category/<int:id>', views.list_by_category, name='list_by_category'),
  path('favorites', views.favorites_list, name='favorites'),
  path('favorites/trainer', views.favorites_train, name='favorites_trainer'),
  path('category/add', views.add_to_favorites, name='add_to_favorites'),
  path('favorites/delete/<int:id>', views.delete_from_favorites, name ='delete_from_favorites'),
]