from django.db import models
from django.conf import settings

# Create your models here.

class FavoritedMovie(models.Model):
    title = models.CharField(max_length=200)
    movie_id = models.IntegerField()
    image_url = models.URLField(verbose_name='Poster Path')
    user = models.ForeignKey(settings.AUTH_USER_MODEL,on_delete=models.CASCADE,related_name='liked_movies')

    def __str__(self):
        return self.title

