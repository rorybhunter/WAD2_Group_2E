from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User


# Create your models here.


class Movie(models.Model):
    movie_name = models.CharField(max_length=128, unique=True)
    movie_id = models.IntegerField()
    category_id = models.IntegerField()
    main_actor = models.CharField(max_length=128)
    likes = models.IntegerField()
    username = models.CharField(max_length=128)
    # poster = models.imageField() #i forgor how to do this

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self): 
        return self.name
    
class Page(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE) 
    title = models.CharField(max_length=128)
    url = models.URLField()
    views = models.IntegerField(default=0)
    
    def __str__(self): 
        return self.title

class UserProfile(models.Model):
    # Link User profile to User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional attributes we wish to store.
    picture = models.ImageField(upload_to='profile_images', blank=True)

    USER_TYPE_CHOICES = (

        ('COUCH_POTATO', "Couch Potato"),
        ('CRITIC', "Critic"),
        ('CREATOR', "Creator")
    )

    user_type = models.CharField(max_length=15,
                          choices=USER_TYPE_CHOICES,
                          default="COUCH_POTATO")

    def __str__(self):
        return self.user.username


class Review(models.Model):
    title = models.CharField(max_length=20)
    review = models.CharField(max_length=500)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self) :
        return self.review 
