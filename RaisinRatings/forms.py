from django import forms

from RaisinRatings.models import Review, Movie, Category
from .models import Movie
from django.contrib.auth.models import User
from RaisinRatings.models import UserProfile


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('picture', 'user_type')


class MovieForm(forms.ModelForm):
    movie_name = forms.CharField(max_length=Movie.MOVIE_TITLE_MAX_LENGTH, help_text="Please enter the movie name")
    main_actor = forms.CharField(max_length=Movie.MAIN_ACTOR_MAX_LENGTH, help_text="Please enter the main actor of the movie")
    username = forms.CharField(max_length=Movie.USERNAME_MAX_LENGTH, help_text="Enter your username")
    summary = forms.CharField(max_length=Movie.SUMMARY_MAX_LENGTH, help_text="Please enter the movie summary")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    categories = forms.ModelMultipleChoiceField(queryset=Category.objects.all())

    class Meta:
        model = Movie
        fields = ['movie_name', 'main_actor', 'username', 'summary', 'poster', 'categories']
        
class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=20, help_text = 'Enter your review title: ')
    review = forms.CharField(max_length=500, help_text = 'Enter your review: ')
    
    class Meta:
       model = Review 
       fields = ('movie', 'title', 'review')


