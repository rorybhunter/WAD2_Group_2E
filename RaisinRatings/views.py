from RaisinRatings.forms import ReviewForm, UserForm, UserProfileForm, MovieForm, CategoryForm
from RaisinRatings.models import Review, Category, Movie, User, Permission
from django.urls import reverse 
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.http import HttpResponse
from django.views import View
from RaisinRatings.bing_search import run_query
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.utils.decorators import method_decorator

def index(request):
    context_dict = {}
    
    category_list = Category.objects.order_by('-likes')[:8]
    movie_list = Movie.objects.order_by('-likes')[:5]

    context_dict['movies'] = movie_list
    context_dict['categories'] = category_list

    visitor_cookie_handler(request)
    context_dict['visits'] = request.session['visits']

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
    print(movie.user)
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

    recently_viewed = recently_viewed_handler(request, movie.movie_name)
    context_dir['recently_viewed'] = recently_viewed

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

def like_movie(request, movie_title_slug):
    movie = Movie.objects.get(slug=movie_title_slug)
    movie.likes += 1
    movie.save()

    return redirect(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug': movie_title_slug}))

def dislike_movie(request, movie_title_slug):
    movie = Movie.objects.get(slug=movie_title_slug)
    movie.likes -= 1
    movie.save()

    return redirect(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug': movie_title_slug}))

def delete_movie(request, movie_title_slug):
    movie = Movie.objects.get(slug=movie_title_slug)
    movie.delete()

    return redirect('/RaisinRatings/')

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
    category_list = Category.objects.order_by('-likes')
    context_dict = {}
    context_dict['categories'] = category_list
    
    return render(request, 'RaisinRatings/categories.html', context=context_dict)


def search(request):
    result_list = []
    search_term = ""  # included and passed as a parameter to allow the search term to still be in the search box after searching and reloading pasge.
    if request.method == 'POST':
        query = request.POST['query'].strip()
        if query:
            result_list, search_term = run_query(query)
    return render(request, 'RaisinRatings/search.html', {'result_list': result_list, 'search_term': search_term})


def get_server_side_cookie(request, cookie, default_val=0):
    val = request.session.get(cookie)
    if not val:
        val = default_val
    return val

def visitor_cookie_handler(request):
    visits = int(get_server_side_cookie(request, 'visits', '1'))


    last_visit_cookie = get_server_side_cookie(request, 'last_visit', str(datetime.now()))
    last_visit_time = datetime.strptime(last_visit_cookie[:-7],'%Y-%m-%d %H:%M:%S')

    if (datetime.now() - last_visit_time).days > 0:
        visits += 1
        request.session['last_visit'] = str(datetime.now())
    else:
        request.session['last_visit'] = last_visit_cookie
    
    request.session['visits'] = visits

def recently_viewed_handler(request, movie):
    recently_viewed = get_server_side_cookie(request, 'recently_viewed', [])

    if not movie in recently_viewed:
        recently_viewed.append(movie)
    else:
        if movie in recently_viewed:
            recently_viewed.remove(movie)
        recently_viewed .insert(0, movie)
        if len(recently_viewed) > 5:
            recently_viewed.pop()
    
    request.session['recently_viewed'] = recently_viewed
    print(recently_viewed)



def edit_movie(request, movie_title_slug):
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

class LikeCategoryView(View):
    @method_decorator(login_required)
    def get(self, request):
        category_name = request.GET['name']
        user = User.objects.get(id = request.user.id)
        try:
            category = Category.objects.get(name = category_name)
        except Category.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        if category not in user.userprofile.categories:
            category.likes = category.likes + 1
            category.save()
            user.userprofile.categories.append(category)


        return HttpResponse(category.likes)

class DislikeCategoryView(View):
    @method_decorator(login_required)
    def get(self, request):
        category_name = request.GET['name']
        user = User.objects.get(id = request.user.id)
        try:
            category = Category.objects.get(name = category_name)
        except Category.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        if category in user.userprofile.categories:
            category.likes = category.likes - 1
            category.save()
            user.userprofile.categories.remove(category)

        return HttpResponse(category.likes)


class LikeMovieView(View):
    @method_decorator(login_required)
    def get(self, request):
        movie_name = request.GET['movie_name']
        user = User.objects.get(id = request.user.id)
        try:
            movie = Movie.objects.get(movie_name = movie_name)
        except Movie.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        if movie not in user.userprofile.movies:
            movie.likes = movie.likes + 1
            movie.save()
            user.userprofile.movies.append(movie)

        return HttpResponse(movie.likes)


class DislikeMovieView(View):
    @method_decorator(login_required)
    def get(self, request):
        movie_name = request.GET['movie_name']
        user = User.objects.get(id = request.user.id)
        try:
            movie = Movie.objects.get(movie_name = movie_name)
        except Movie.DoesNotExist:
            return HttpResponse(-1)
        except ValueError:
            return HttpResponse(-1)

        if movie in user.userprofile.movies:
            movie.likes = movie.likes - 1
            movie.save()
            user.userprofile.movies.remove(movie)
    
        return HttpResponse(movie.likes)
