from django import forms

from RaisinRatings.models import Review, Movie
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
    movie_name = forms.CharField(max_length=Movie.MOVIE_TITLE_MAX_LENGTH)
    main_actor = forms.CharField(max_length=Movie.MAIN_ACTOR_MAX_LENGTH)
    username = forms.CharField(max_length=Movie.USERNAME_MAX_LENGTH)
    summary = forms.CharField(max_length=Movie.SUMMARY_MAX_LENGTH)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = Movie
        fields = ['movie_name', 'main_actor', 'username', 'summary' ]
        
class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=20, help_text = 'Enter your review title: ')
    review = forms.CharField(max_length=500, help_text = 'Enter your review: ')
    
    class Meta:
       model = Review 
       fields = ('movie', 'title', 'review')


