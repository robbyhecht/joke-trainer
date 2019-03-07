from django.conf.urls import include
from django.urls import path
from jt import views


app_name = "jt"
urlpatterns = [
  path('', views.list_categories, name='list_categories'),
  # path('', views.nav_favorites, name='nav_favorites'),
  path('login', views.login_user, name='login'),
  path('logout', views.user_logout, name='logout'),
  path('register', views.register, name='register'),
  path('category/<int:id>', views.list_by_category, name='list_by_category'),
  path('favorites', views.favorites_list, name='favorites'),
  path('favorites/trainer', views.favorites_train, name='favorites_trainer'),
]