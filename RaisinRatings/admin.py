from django.contrib import admin
from RaisinRatings.models import Category, UserProfile, Movie, Review

# Register your models here.

admin.site.register(Category)
admin.site.register(UserProfile)
admin.site.register(Movie)
admin.site.register(Review)