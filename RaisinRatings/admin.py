from django.contrib import admin
from RaisinRatings.models import UserProfile, Category, Movie, Review

# Register your models here.
admin.site.register(UserProfile)
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Review)