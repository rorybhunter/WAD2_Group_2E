from django.shortcuts import render, redirect
from .forms import MovieForm
# Create your views here.


def index(request):
    # will uncomment and modifiy these to fit actual models later:
    # category_list = Category.objects.order_by('-likes')[:8]
    # movie_list = Movy.objects.order_by('-likes')[:5]

    # some example models created to test the categories and movies display correctly
    class CategoryExample:
        def __init__(self, name, likes):
            self.name = name
            self.likes = likes

    class MovieExample:
        def __init__(self, name, likes):
            self.name = name
            self.likes = likes

    category_list = [CategoryExample("Example movie", 5), CategoryExample("Example movie 2", 3)]
    movie_list = [MovieExample("Example movie", 4), CategoryExample("Example movie 2", 2)]
    context_dict = {}
    context_dict['categories'] = category_list
    context_dict['movies'] = movie_list

    # visitor_cookie_handler(request)

    response = render(request, 'RaisinRatings/index.html', context=context_dict)
    return response


def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies_list')  # replace movies_list with your own view name
    else:
        form = MovieForm()
    return render(request, 'movies/add_movie.html', {'form': form})

