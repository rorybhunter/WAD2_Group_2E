from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class UserProfile(models.Model):
    # Link User profile to User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    # additional attributes we wish to store.
    picture = models.ImageField(upload_to='profile_images', blank=True)
    user_type = models.CharField(max_length=50, unique=False)

    def __str__(self):
        return self.user.username
