from django.db import models
from django.template.defaultfilters import slugify



class Movie(models.Model):
    title = models.CharField(max_length=20, unique=True)
    summary = models.CharField(max_length=500)
    slug = models.SlugField(unique=True)
    likes = models.IntegerField(default = 0)
    main_star = models.CharField(max_length=50)
    

    def save (self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self) :
        return self.title 

class Review(models.Model):
    title = models.CharField(max_length=20)
    review = models.CharField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) :
        return self.review 