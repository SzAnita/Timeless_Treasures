from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login, name='login'),
    path('signup', views.signup, name='signup'),
    path('<str:kind>s', views.search),
    path('add_fav/<str:name>', views.add_favorite),
    path('logout', views.logout)
]
