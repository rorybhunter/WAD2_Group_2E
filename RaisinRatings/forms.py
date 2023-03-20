from django import forms

from RaisinRatings.models import Review, Movie
from .models import Movie, Category
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
    summary = forms.CharField(max_length=Movie.SUMMARY_MAX_LENGTH)
    trailer_link = forms.CharField(max_length=Movie.TRAILER_MAX_LENGTH)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    poster = forms.ImageField(required=False)

    widgets = {
        'user': forms.HiddenInput(),
    }


    class Meta:
        model = Movie
        exclude = ('user', )
        fields = ['movie_name', 'main_actor', 'summary', 'trailer_link', 'poster', 'category', ]


class CategoryForm(forms.ModelForm):
    name = forms.CharField(max_length=127, help_text="category name")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)


    class Meta: 
        model = Category 
        fields = ["name", 'description']


class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=20, help_text = 'Enter your review title: ')
    review = forms.CharField(max_length=500, help_text = 'Enter your review: ')
    
    class Meta:
       model = Review 
       fields = ('movie', 'title', 'review', 'username')

class EditMovie(forms.ModelForm):
    movie_name = forms.CharField(max_length=Movie.MOVIE_TITLE_MAX_LENGTH)
    main_actor = forms.CharField(max_length=Movie.MAIN_ACTOR_MAX_LENGTH)
    summary = forms.CharField(max_length=Movie.SUMMARY_MAX_LENGTH)
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    poster = forms.ImageField(required=False)

    class Meta:
        model = Movie
        fields = ['movie_name', 'main_actor', 'summary', 'poster']
