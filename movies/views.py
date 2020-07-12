import requests

from django.shortcuts import render
from django.conf import settings
from django.contrib.auth.decorators import login_required
from django.views.decorators.http import require_POST
from django.http import JsonResponse
from django.db.models import Count

from .models import FavoritedMovie

# Create your views here.

TMDB_API_KEY = settings.TMDB_KEY

def index(request):
    '''Request the latest trending movies from the Movie Database API.'''
    
    url = "https://api.themoviedb.org/3/trending/movie/day?api_key={}&".format(TMDB_API_KEY)
    config_url = "https://api.themoviedb.org/3/configuration?api_key={}".format(TMDB_API_KEY)

    res = requests.get(url).json()
    config_res = requests.get(config_url).json()

    context = {
        'movies' : res["results"],
        'base_url':config_res["images"]["base_url"],
        'poster_size':config_res["images"]["poster_sizes"][3]
    }    

    return render(request, 'movies/index.html',context)

def details(request,movie_id):
    '''
        Returns detailed information about a movie identified
        by the movie_id parameter.
    ''' 

    url = "https://api.themoviedb.org/3/movie/{}?api_key={}&language=en-US&append_to_response=videos".format(movie_id,TMDB_API_KEY)       
    config_url = "https://api.themoviedb.org/3/configuration?api_key={}".format(TMDB_API_KEY)
    res = requests.get(url).json()
    config_res = requests.get(config_url).json()

    context = {

        'movie' : res,
        'base_url':config_res["images"]["base_url"],
        'poster_size':config_res["images"]["poster_sizes"][3]
    }    

    return render(request,'movies/movie.html',context)  

@login_required
@require_POST
def watchlist(request):
    movie_id = request.POST['movie_id']
    title = request.POST['title']
    imagePath = request.POST['imagePath']
    user = request.user
    status = 'Error while adding the movie to your watchlist!'

    #check if this user has already liked this movie
    liked_movie = user.liked_movies.filter(movie_id = movie_id)

    if liked_movie:
        status = 'You already added this movie to your watchlist!'
    else:
        # save as favorited movie - user has not yet liked movie 
        favorite = FavoritedMovie.objects.create(movie_id = movie_id,title = title,
                                                 image_url = imagePath,user = user)
                                                
        if favorite:
            return JsonResponse({'status': 'Movie has been added to your watchlist!'})
    
    return JsonResponse({'status': status})


@login_required
def user_watchlist(request):
    '''
       Returns all movies that have been favorited by the currently 
       authenticated user.
    '''

    user = request.user
    context = {

        'movies': user.liked_movies.distinct('movie_id')
    }

    return render(request, 'movies/user.html', context)  


def favorite(request):
    '''
      Returns the most favorited movies by users on
      the platform.
    '''  

    movies_by_popularity = FavoritedMovie.objects.values('title','image_url')\
                                                 .annotate(num_likes=Count('id'))\
                                                 .order_by('-num_likes')[:5]
    context = {
        'movies': movies_by_popularity 
    }
    
    return render(request, 'movies/favorites.html', context)     


   

