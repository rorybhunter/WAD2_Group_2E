from django.db import models


# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(128)
    movie_id = models.IntegerField()
    category_id = models.IntegerField()
    main_actor = models.CharField(128)
    likes = models.IntegerField()
    username = models.CharField(128)
    poster = models.imageField()
