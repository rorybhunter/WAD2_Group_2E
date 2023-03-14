from RaisinRatings.forms import ReviewForm, UserForm, UserProfileForm, MovieForm
from RaisinRatings.models import Review, Category, Movie
from django.urls import reverse 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.http import HttpResponse
from RaisinRatings.bing_search import run_query


def index(request):
 
    # some example models created to test the categories and movies display correctly
    #class CategoryExample:
        #def __init__(self, name, likes):
            #self.name = name
            #self.likes = likes

    #class MovieExample:
        #def __init__(self, name, likes):
            #self.name = name
            #self.likes = likes

    #category_list = [CategoryExample("Example movie", 5), CategoryExample("Example movie 2", 3)]
    #movie_list = [MovieExample("Example movie", 4), CategoryExample("Example movie 2", 2)]

    context_dict = {}
    
    category_list = Category.objects.all()
    movie_list = Movie.objects.order_by('-likes')[:5]

    context_dict['movies'] = movie_list
    context_dict['categories'] = category_list
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
    request.session.set_test_cookie()
    if request.method == 'POST':
        form = MovieForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            return redirect('/RaisinRatings/')  
    else:
        form = MovieForm()
    return render(request, 'RaisinRatings/add_movie.html', {'form': form})
    
    
def show_movie(request, movie_title_slug):
    context_dir = {}
    movie = Movie.objects.get(slug=movie_title_slug)
    reviews = Review.objects.filter(movie=movie)
    likes = movie.likes
    url = movie.trailer_link
    url = url.replace("/watch?v=", "/embed/")
    url = url.replace("youtu.be", "youtube.com/embed")
    try:
        index = url.index("&")
        url = url[:index]
    except:
        pass

    context_dir['movie'] = movie
    context_dir['reviews'] = reviews
    context_dir['likes'] = likes
    context_dir['trailer_link'] = url


    return render(request, 'RaisinRatings/movie.html', context=context_dir)

def like(request, movie_title_slug):
    movie = Movie.objects.get(slug=movie_title_slug)
    movie.likes += 1
    movie.save()
    
    return redirect(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug': movie_title_slug}))
    
    
def add_review(request, movie_title_slug):
    movie = Movie.objects.get(slug=movie_title_slug) 

    form = ReviewForm()
    
    if request.method == 'POST':
        form  = ReviewForm(request.POST)
        if form.is_valid():
            form.save(commit=False)
            form.movie = movie 
            form.save(commit=True)
            return redirect(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug': movie_title_slug}))
        else:
            print('form not valid')
            print(form.errors)
    context_dict = {'form': form, 'movie': movie}
    return render(request, 'RaisinRatings/add_review.html', context=context_dict)


def categories(request):
    category_list = Category.objects.all()
    #We need to make it possible to add a category 
    context_dict = {}
    context_dict['categories'] = category_list
    
    return render(request, 'RaisinRatings/categories.html', context=context_dict)

def cat_page(request):
    context_dict = {'boldmessage': 'Hmm'}
    #Once we can add categories we can fix this 
    return render(request, 'RaisinRatings/cat_page.html', context=context_dict)


def search(request):
    if request.session.test_cookie_worked():
        print("TEST COOKIE WORKED!")
        request.session.delete_test_cookie()
    result_list = []
    search_term = ""  # included and passed as a parameter to allow the search term to still be in the search box after searching and reloading pasge.
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            result_list, search_term = run_query(query)
    return render(request, 'RaisinRatings/search.html', {'result_list': result_list, 'search_term': search_term})
