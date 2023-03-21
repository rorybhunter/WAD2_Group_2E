from RaisinRatings.forms import ReviewForm, UserForm, UserProfileForm, MovieForm, CategoryForm
from RaisinRatings.models import Review, Category, Movie, User, Permission, UserProfile
from django.urls import reverse 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from RaisinRatings.bing_search import run_query
from django.contrib.auth.decorators import login_required



def index(request):
    context_dict = {}
    
    category_list = Category.objects.order_by('-likes')[:8]
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
            return render(request, 'RaisinRatings/login.html')
    else:
        return render(request, 'RaisinRatings/login.html')


@login_required
def user_logout(request):
    logout(request)
    return redirect(reverse('RaisinRatings:index'))

@login_required
def add_movie(request):
    categories = Category.objects.all()
    context_dict = {}
    try:
        author = User.objects.get(id = request.user.id)
    except User.DoesNotExist:
        author = None

    if author is None:
        return redirect('/RaisinRatings/')

    if request.method == 'POST':
        form = MovieForm(request.POST, request.FILES)
        if form.is_valid():
            if author:
                movie = form.save(commit=False)
                movie.user = author
                movie.save()

            return redirect('/RaisinRatings/')  
    else:
        form = MovieForm()

    context_dict['form'] = form
    context_dict['categories'] = categories
    return render(request, 'RaisinRatings/add_movie.html', context_dict)

@login_required
def add_category (request):

    if request.method == "POST":
        form = CategoryForm(request.POST)
        if form.is_valid():
            form.save(commit=True)

            return redirect('/RaisinRatings/')
    else:
        form = CategoryForm()
    return render(request, 'RaisinRatings/add_category.html', {'form': form})

def delete_movie(request, movie_title_slug):
    Movie.objects.get(slug = movie_title_slug).delete()
    return redirect('/RaisinRatings/')


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


def cat_page(request, category_name_slug):
    context_dict = {}
    category = Category.objects.get(slug=category_name_slug)
    movies = Movie.objects.filter(category=category).order_by('-likes')
    context_dict['category'] = category
    context_dict['description'] = category.description
    context_dict['name'] = category.name
    context_dict['movies'] = movies
    context_dict['likes'] = category.likes

    return render(request, 'RaisinRatings/cat_page.html', context=context_dict)

@login_required
def like_movie(request, movie_title_slug):
    movie = Movie.objects.get(slug=movie_title_slug)
    user = User.objects.get(id = request.user.id)
    if movie not in user.userprofile.movies:
        movie.likes += 1
        movie.save()
        user.userprofile.movies.append(movie)

    return redirect(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug': movie_title_slug}))

@login_required
def dislike_movie(request, movie_title_slug):
    movie = Movie.objects.get(slug=movie_title_slug)
    user = User.objects.get(id = request.user.id)
    if movie in user.userprofile.movies:
        movie.likes -= 1
        movie.save()
        user.userprofile.movies.remove(movie)

    return redirect(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug': movie_title_slug}))

@login_required
def delete_movie(request, movie_title_slug):
    movie = Movie.objects.get(slug=movie_title_slug)
    movie.delete()

    return redirect('/RaisinRatings/')

@login_required
def like_category(request, category_name_slug):
    category = Category.objects.get(slug=category_name_slug)
    print("here")
    category.likes += 1
    category.save()

    return redirect(reverse('RaisinRatings:category', kwargs={'category_name_slug': category_name_slug}))

@login_required
def dislike_category(request, category_name_slug):
    category = Category.objects.get(slug=category_name_slug)
    print("here")
    category.likes -= 1
    category.save()

    return redirect(reverse('RaisinRatings:category', kwargs={'category_name_slug': category_name_slug}))

@login_required
def add_review(request, movie_title_slug):

    try:
        author = User.objects.get(id = request.user.id)
    except User.DoesNotExist:
        author = None

    if author is None:
        return redirect('/RaisinRatings/')

    review = ReviewForm()
    movie = Movie.objects.get(slug=movie_title_slug)

    if request.method == 'POST':

        form = ReviewForm(request.POST, request.FILES)
        if form.is_valid():
            if author:
                review = form.save(commit=False)
                review.username = author
                review.movie = movie
                review.save()
                return redirect(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug': movie_title_slug}))
            else:
                print('form not valid')
                review = ReviewForm()
                print(form.errors)

    context_dict = {'form': review, 'movie': movie}
    return render(request, 'RaisinRatings/add_review.html', context=context_dict)


def categories(request):
    category_list = Category.objects.order_by('-likes')
    context_dict = {}
    context_dict['categories'] = category_list
    
    return render(request, 'RaisinRatings/categories.html', context=context_dict)


def search(request):
    result_list = []
    print("Search")
    query = ""
    if request.method == 'POST':
        print("post")
        query = request.POST['query'].strip()
        print(query)
        if query:
            result_list, query = run_query(query)
    return render(request, 'RaisinRatings/search.html', {'result_list': result_list, 'search_term': query})


@login_required
def edit_movie(request, movie_title_slug=""):
    movie = Movie.objects.get(slug=movie_title_slug)
    try:
        author = User.objects.get(id = request.user.id)
    except User.DoesNotExist:
        author = None


    if author is None:
        return redirect('/RaisinRatings/')

    form = MovieForm()

    if form.is_valid():
        if author:
                movie = form.save(commit=False)
                movie.user = author
                movie.save()
        print("we are here")
        return redirect(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug': movie_title_slug}))
    else:
        print(form.errors)
    context_dict = {'form': form, 'movie': movie}
    movie.delete()
    return render(request, 'RaisinRatings/edit_movie.html', context_dict)


def user_page(request, username):
    context_dir = {}
    user = User.objects.get(username=username)
    userprofile = user.userprofile
    username = user.username
    picture = userprofile.picture
    user_type = userprofile.user_type
    movies = userprofile.movies


    context_dir['page_user'] = user
    context_dir['picture'] = picture
    context_dir['user_type'] = user_type
    context_dir['movies'] = movies
    return render(request, 'RaisinRatings/user_page.html', context=context_dir)