from django.contrib import admin
from RaisinRatings.models import User, Category, Movie, Comment

# Register your models here.
admin.site.register(User)
admin.site.register(Category)
admin.site.register(Movie)
admin.site.register(Comment)