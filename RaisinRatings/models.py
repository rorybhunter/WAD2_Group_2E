from django.db import models
from django.template.defaultfilters import slugify
import uuid

class User(models.Model):
    ROLES = (('USER', 'User'), ('CREATOR', 'Creator'), ('CRITIC', 'Critic'))
    username = models.CharField(primary_key=True, max_length=128, unique=True,)
    password = models.CharField(max_length=128)
    role = models.CharField(max_length=32, choices=ROLES, default='USER')
    profile_picture = models.ImageField(upload_to='profilepics', blank=True)
    tag = models.CharField(max_length=128)

    def __str__(self):
        return self.username


class Category(models.Model):
    name = models.CharField(primary_key=True, max_length=128, unique=True)
    likes = models.IntegerField(default=0)
    creator = models.ForeignKey(User, on_delete=models.CASCADE)
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
    category_id = models.ForeignKey(Category, on_delete=models.CASCADE) 
    main_actor = models.CharField(max_length = 128)
    likes = models.IntegerField(default=0)
    poster = models.ImageField(upload_to='posters', blank=True)
    creator = models.ForeignKey(User, on_delete=models.CASCADE, related_name='Creator', null=True)
    user_raters = models.ManyToManyField(User, related_name='User')
    slug = models.SlugField(unique=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        super(Movie, self).save(*args, **kwargs)


class Comment(models.Model):
    comment_id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    content = models.CharField(max_length=1024)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)

    def __str__(self):
        return self.content