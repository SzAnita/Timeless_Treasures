from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('login', views.login),
    path('signup', views.signup),
    path('<str:kind>s', views.search),
    path('add_fav/<str:name>', views.add_favorite),
    path('logout', views.logout),
    path('favorite', views.favorites),
    path('check_user', views.check_user),
    path('user', views.user),
]
