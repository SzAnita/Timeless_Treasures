from django.urls import path
from . import views

urlpatterns = [
    path('index/', views.index, name='index'),
    path('login', views.login, name='login'),
    path('check_user', views.check_user, name='check_userpypy')
]