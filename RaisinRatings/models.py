from django.db import models
from django.template.defaultfilters import slugify
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import uuid

class Movie(models.Model):
    MOVIE_TITLE_MAX_LENGTH = 128
    MAIN_ACTOR_MAX_LENGTH = 128
    USERNAME_MAX_LENGTH = 128
    SUMMARY_MAX_LENGTH = 500

    movie_name = models.CharField(max_length=MOVIE_TITLE_MAX_LENGTH, unique=True)
    main_actor = models.CharField(max_length=MAIN_ACTOR_MAX_LENGTH)
    likes = models.IntegerField(default=0)
    username = models.CharField(max_length=USERNAME_MAX_LENGTH)
    summary = models.CharField(max_length=SUMMARY_MAX_LENGTH)
    slug = models.SlugField(unique=True)
    poster = models.ImageField(upload_to='movie_posters', blank=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.movie_name)
        super(Movie, self).save(*args, **kwargs)

    def __str__(self):
        return self.movie_name

class Category(models.Model):
    name = models.CharField(max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    slug = models.SlugField(unique=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    class Meta:
        verbose_name_plural = "Categories"
    
    def __str__(self): 
        return self.name

class UserProfile(models.Model):
    # Link User profile to User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    likes = models.IntegerField(default=0)
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
    # username = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self) :
        return self.review 



