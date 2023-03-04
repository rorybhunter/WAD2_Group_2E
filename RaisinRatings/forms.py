from django import forms
from .models import Movie

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['movie_name', 'movie_id', 'category_id', 'main_actor', 'likes', 'username', 'poster']