from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index),
    path('login', views.login),
    path('signup', views.signup),
    path('add_fav/<str:name>', views.add_favorite),
    path('logout', views.logout),
    path('check_user', views.check_user),
    path('user', views.user),
    path('filter', views.filter_),
    path('<str:kind_>', views.menu),
    path('search', views.search)
]
