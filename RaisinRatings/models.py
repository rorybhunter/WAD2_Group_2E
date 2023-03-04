from django.db import models


# Create your models here.

class Movie(models.Model):
    movie_name = models.CharField(max_length=128, unique=True)
    movie_id = models.IntegerField()
    category_id = models.IntegerField()
    main_actor = models.CharField(max_length=128)
    likes = models.IntegerField()
    username = models.CharField(max_length=128)
    # poster = models.imageField()
