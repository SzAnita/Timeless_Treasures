from django.urls import path
from . import views

urlpatterns = [
    path('index', views.index, name='index'),
    path('login', views.login),
    path('signup', views.signup),
    path('add_fav/<str:name>', views.add_favorite),
    path('logout', views.logout, name='logout'),
    path('user/<str:collection_>', views.user),
    path('check_user', views.check_user),
    path('update_coll', views.update_coll),
    path('add_collection/<str:antique>', views.add_to_collection),
    path('get_coll', views.get_coll, name='get_coll'),
    path('user', views.user),
    path('filter', views.filter_),
    path('<str:kind_>', views.menu),
    path('search', views.filter_),
]
