from django.shortcuts import render
from RaisinRatings.forms import ReviewForm, AddMovie
from django.shortcuts import redirect
from RaisinRatings.models import Review, Movie
from django.urls import reverse 

def show_movie(request, movie_title_slug):
    context_dir = {}
    movie = Movie.objects.get(slug=movie_title_slug)
    reviews = Review.objects.filter(movie=movie)
    likes = movie.likes
    context_dir['movie'] = movie
    context_dir['reviews'] = reviews
    context_dir['likes'] = likes

    return render(request, 'RaisinRatings/movie.html', context=context_dir)

def like(request, movie_title_slug):
    movie = Movie.objects.get(slug=movie_title_slug)
    print(movie.likes)
    movie.likes += 1
    movie.save()
    print(movie.likes)
    
    return redirect(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug': movie_title_slug}))
    
    
def add_review(request, movie_title_slug):
    movie = Movie.objects.get(slug=movie_title_slug) 

    form = ReviewForm()
    
    if request.method == 'POST':
        form  = ReviewForm(request.POST)
        if form.is_valid():
            if movie:
                review = form.save()
                review.movie = movie 
                review.save()
            return redirect(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug': movie_title_slug}))
        else:
            print(form.errors)
    context_dict = {'form': form, 'movie': movie}
    return render(request, 'RaisinRatings/add_review.html', context=context_dict)


   


