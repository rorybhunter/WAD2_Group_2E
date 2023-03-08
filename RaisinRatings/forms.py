from django import forms
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
    class Meta:
        model = Movie
        fields = ['name', 'category', 'main_actor', 'likes', 'poster']
