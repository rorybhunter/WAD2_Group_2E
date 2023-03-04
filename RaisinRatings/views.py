from django.shortcuts import render, redirect

# Create your views here.

from .forms import MovieForm


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies_list')  # replace movies_list with your own view name
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})
