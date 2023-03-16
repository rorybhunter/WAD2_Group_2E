from django.contrib import admin
<<<<<<< HEAD
from RaisinRatings.models import UserProfile, Category, Movie, Review

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Review)
=======
from RaisinRatings.models import Category, UserProfile, Movie

# Register your models here.

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Movie)
>>>>>>> 5c8b02d1418bf6fef64f09c0782e9f213bc04611
