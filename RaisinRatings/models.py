from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
import uuid

# Create your models here.


class Movie(models.Model):
    movie_name = models.CharField(max_length=128, unique=True)
    category = models.IntegerField()
    main_actor = models.CharField(max_length=128)
    likes = models.IntegerField()
    username = models.CharField(max_length=128, blank=True, default=None)
    poster = models.ImageField(upload_to='profile_images', blank=True)


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


# class User(models.Model):
#     ROLES = (('USER', 'User'), ('CRITIC', 'Critic'), ('CREATOR', 'Creator'))
#     username = models.CharField(primary_key=True, max_length=128, unique=True,)
#     password = models.CharField(max_length=128)
#     role = models.CharField(max_length=15, choices=ROLES, default='USER')
#     profile_picture = models.ImageField(upload_to='profilepics')
#     tag = models.CharField(max_length=128)

#     def __str__(self):
#         return self.username


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    username = models.ForeignKey(User, on_delete=models.CASCADE)
    slug = models.SlugField(unique=True)


    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = 'Categories'

class Movie(models.Model):
    movie_id = models.UUIDField(primary_key= True, default=uuid.uuid4, editable=False)
    name = models.CharField(max_length = 128, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    main_actor = models.CharField(max_length = 128)
    likes = models.IntegerField(default=0)
    poster = models.ImageField(upload_to='posters')
    # username = models.ManyToManyField(User)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Category, self).save(*args, **kwargs)


class Comment(models.Model):
    content = models.CharField(max_length=1024)
    # username = models.ForeignKey(User, on_delete=models.CASCADE)
    critic = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.content

