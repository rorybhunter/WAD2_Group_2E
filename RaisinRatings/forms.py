from django import forms
from RaisinRatings.models import Review, Movie

class ReviewForm(forms.ModelForm):
    title = forms.CharField(max_length=20, help_text = 'Enter your review title: ')
    review = forms.CharField(max_length=500, help_text = 'Enter your review: ')
    
    class Meta:
       model = Review 
       fields = ('movie', 'title', 'review')
       

class AddMovie(forms.ModelForm):
    title = forms.CharField(max_length=20, help_text="Enter movie title here: ")
    summary = forms.CharField(max_length=500, help_text="Enter movie summary here: ")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)
    main_star = forms.CharField(max_length=50, help_text = "Enter the main star of the movie here: ")

    class Meta:
       model = Movie
       fields = ('title', 'summary', 'main_star')

