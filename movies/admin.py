from django.contrib import admin
from .models import FavoritedMovie

# Register your models here.

@admin.register(FavoritedMovie)
class FavoritedMovieAdmin(admin.ModelAdmin):
    list_display = ['movie_id','user','title','image_url']
