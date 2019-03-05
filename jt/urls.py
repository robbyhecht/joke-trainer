from django.conf.urls import include
from django.urls import path
from jt import views


app_name = "jt"
urlpatterns = [
  path('', views.list_categories, name='list_categories'),
  path('', views.hi_user, name='hi_user'),
  path('login', views.login_user, name='login'),
  path('logout', views.user_logout, name='logout'),
  path('register', views.register, name='register'),
  path('category/<int:id>', views.list_by_category, name='list_by_category'),
  path('favorites', views.favorites_list, name='favorites_list'),
]