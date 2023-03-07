from RaisinRatings.forms import ReviewForm, AddMovie, UserForm, UserProfileForm, MovieForm
from RaisinRatings.models import Review, Movie
from django.urls import reverse 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse



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




def register(request):
    registered = False

    if request.method == "POST":
        user_form = UserForm(request.POST)
        profile_form = UserProfileForm(request.POST)

        if user_form.is_valid() and profile_form.is_valid():
            user = user_form.save()

            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if 'picture' in request.FILES:
                profile.picture = request.FILES['picture']
            profile.save()

            registered = True
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileForm()

    return render(request, 'RaisinRatings/register.html',
                  context = {'user_form': user_form,
                             'profile_form': profile_form,
                             'registered': registered})


def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user:
            if user.is_active:
                login(request, user)
                return redirect(reverse('RaisinRatings:index'))
            else:
                return HttpResponse("Your RaisinRatings account is disabled.")
        else:
            print(f"Invalid login details: {username}, {password}")
            return HttpResponse("Invalid login details supplied.")
    else:
        return render(request, 'RaisinRatings/login.html')
 
def add_movie(request):
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('movies_list')  # replace movies_list with your own view name
    else:
        form = MovieForm()
    return render(request, 'RaisinRatings/add_movie.html', {'form': form})
    
    
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


