from django.urls import path
from . import views

urlpatterns = [

    path('', views.index, name='movies_list'),
    path('movies/<int:movie_id>', views.details, name='movie_details'),
    path('movies/like', views.watchlist, name='movie_like'),
    path('movies/favorites/',views.favorite,name='movie_favorites'),
    path('watchlist/', views.user_watchlist,name='watch_list'),
]