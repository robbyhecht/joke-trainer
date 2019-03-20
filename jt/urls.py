from django.conf.urls import include
from django.urls import path
from jt import views


app_name = "jt"
urlpatterns = [
  # path('', views.index, name='index'),
  path('', views.random_joke, name = 'random_joke'),
  path('categories', views.list_categories, name='list_categories'),
  path('myjokes', views.list_my_jokes, name='list_my_jokes'),
  path('login', views.login_user, name='login'),
  path('logout', views.user_logout, name='logout'),
  path('register', views.register, name='register'),
  path('category/<int:id>', views.list_by_category, name='list_by_category'),
  path('favorites', views.favorites_list, name='favorites'),
  path('favorites/trainer', views.favorites_train, name='favorites_trainer'),
  path('category/add', views.add_to_favorites, name='add_to_favorites'),
  path('favorites/remove/<int:id>', views.remove_from_favorites, name ='remove_from_favorites'),
  path('about', views.about, name = 'about'),
  path('about/cruise', views.about_cruise, name = 'about_cruise'),
  path('about/favorites', views.about_favorites, name = 'about_favorites'),
  path('about/trainer', views.about_trainer, name = 'about_trainer'),
  path('about/add', views.about_add, name = 'about_add'),


  path('search', views.search, name = 'search'),
  path('add', views.add_joke, name = 'add_joke'),
  path('delete/<int:id>', views.delete_joke, name = 'delete_joke'),
  path('edit/<int:id>', views.edit_joke, name = 'edit_joke'),
]