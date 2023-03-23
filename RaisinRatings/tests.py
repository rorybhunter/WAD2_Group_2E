from django.test import TestCase
from RaisinRatings.models import Category, UserProfile, Movie
from RaisinRatings.forms import UserForm, MovieForm, CategoryForm, ReviewForm
from django.urls import reverse
from django.contrib.auth.models import User
from django.test.client import Client
from django.contrib import auth
from django.http import HttpRequest
# Create your tests here.

class CategoryMethodTests(TestCase):
    def test_slug_line_creation(self):
        category = Category(name = 'Random Category String')
        category.save()

        self.assertEqual(category.slug, 'random-category-string')

class MovieMethodTests(TestCase):
    def test_slug_line_creation(self):
        user = User.objects.get_or_create(username = "Quentin Tarantino", password = "bill")
        category = Category(name = "Drama")
        category.save()
        movie = Movie.objects.get_or_create(movie_name = "Pulp Fiction", main_actor = "John Travolta", user = user[0], category = category)[0]
        movie.save()

        self.assertEqual(movie.slug, 'pulp-fiction')


def add_category(name, likes=0, description = ''):
    category = Category.objects.get_or_create(name=name)[0]
    category.likes = likes
    category.description = description
    
    category.save()
    return category

def add_movie(movie_name, main_actor, category, user, likes=0, summary=''):
    movie = Movie.objects.get_or_create(movie_name = movie_name, category = category, user= user)[0]
    movie.main_actor = main_actor
    movie.user = user
    movie.likes= likes
    movie.summary = summary

    movie.save()
    return movie

def add_user(username, password):
    user = User.objects.get_or_create(username = username)[0]
    user.set_password(password)
    user.save()
    return user

class IndexViewTests(TestCase):
    def test_index_view_with_no_categories_and_no_movie(self):
        response = self.client.get(reverse('RaisinRatings:index'))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, "There are no categories present.")
        self.assertContains(response, "There are no movies present.")

        self.assertQuerysetEqual(response.context['categories'], [])
        self.assertQuerysetEqual(response.context['movies'], [])
    
    def test_index_view_with_categories_and_no_movie(self):

        add_category('Horror', 2)
        add_category('Drama', 5)
        add_category('Comedy', 7)
        
        response = self.client.get(reverse('RaisinRatings:index'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Horror')
        self.assertContains(response, 'Drama')
        self.assertContains(response, 'Comedy')
        self.assertContains(response, "There are no movies present.")

        num_categories = len(response.context['categories'])
        self.assertEquals(num_categories, 3)
        self.assertQuerysetEqual(response.context['movies'], [])

    def test_index_view_with_categories_and_movie(self):

        horror_cat = add_category('Horror', 2)
        drama_cat = add_category('Drama', 5)
        comedy_cat = add_category('Comedy', 7)

        creator = add_user('Norbit', 'spaceship')

        add_movie("The Shining", "Jack Nicholson", horror_cat, creator)
        add_movie("Birdman", "Michael Keaton", drama_cat, creator)
        add_movie("Toy Story", "Tom Hanks", comedy_cat, creator)

        response = self.client.get(reverse('RaisinRatings:index'))
        self.assertEqual(response.status_code, 200)

        self.assertContains(response, 'Horror')
        self.assertContains(response, 'Drama')
        self.assertContains(response, 'Comedy')

        self.assertContains(response, 'The Shining')
        self.assertContains(response, 'Birdman')
        self.assertContains(response, 'Toy Story')

        self.assertContains(response, "2")
        self.assertContains(response, "5")
        self.assertContains(response, "7")


class CategoriesViewTest(TestCase):
    def test_categories_view_without_categories(self):
        response = self.client.get(reverse('RaisinRatings:categories'))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "There are no categories yet")

    def test_categories_view_with_categories(self):
        add_category('Horror', 2)
        add_category('Drama', 5)
        add_category('Comedy', 7)

        response = self.client.get(reverse('RaisinRatings:categories'))
        self.assertContains(response, "Horror")
        self.assertContains(response, 'Drama')
        self.assertContains(response, 'Comedy')
        self.assertContains(response, "2")
        self.assertContains(response, "5")
        self.assertContains(response, "7")


class ShowMovieViewTest(TestCase):
    def test_movie(self):
        drama_category = add_category("Drama")
        user = add_user("Norbit", "spaceship")

        movie = add_movie("Birdman", "Michael Keaton", drama_category, user, 11, "This movie is about a man who is a birdman")
        
        response = self.client.get(reverse('RaisinRatings:show_movie', kwargs={'movie_title_slug':movie.slug}))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "Birdman")
        self.assertContains(response, "Michael Keaton")
        self.assertContains(response, "Norbit")
        self.assertContains(response, "This movie is about a man who is a birdman")
        self.assertContains(response, "11")


class CatPageViewTest(TestCase):
    def test_cat_page_without_movies(self):
        comedy_category = add_category("Comedy")
        response = self.client.get(reverse('RaisinRatings:category', kwargs={"category_name_slug":comedy_category.slug}))

        self.assertEqual(response.status_code, 200)

        self.assertContains(response, "There are no movies in this category")

    def test_cat_page_with_movies(self):
        comedy_category = add_category("Comedy", 55)
        user = add_user("Norbit", "spaceship")

        add_movie("The Truman Show", "Jim Carrey", comedy_category, user, 15)
        add_movie("Borat", "Sacha Baren Cohen", comedy_category, user, 27)
        
        response = self.client.get(reverse('RaisinRatings:category', kwargs={"category_name_slug":comedy_category.slug}))
        self.assertEqual(response.status_code, 200)
        
        self.assertContains(response, "Comedy")
        self.assertContains(response, "55")

        self.assertContains(response, "The Truman Show")
        self.assertContains(response, "15")
        
        self.assertContains(response, "Borat")
        self.assertContains(response, "27")


class DeleteMovieViewTest(TestCase):
    def setUp(self):
        self.client = Client()

    def test_delete_movie(self):
        comedy_category = add_category("Comedy")

        user = add_user("Norbit", "spaceship")

        movie = add_movie("Ted", "Mark Whalberg", comedy_category, user, 15)

        response = self.client.get(reverse('RaisinRatings:index'))

        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Comedy")
        self.assertContains(response, "Ted")

        self.client.login(username = "Norbit", password = "spaceship")
       
        response = self.client.get(reverse('RaisinRatings:delete_movie', kwargs={'movie_title_slug':movie.slug}))

        self.assertEqual(response.status_code, 302)

        response = self.client.get(reverse('RaisinRatings:index'))

        self.assertEquals(response.status_code, 200)

        self.assertNotContains(response, "Ted")


class AddCategoryForm(TestCase):
    def test_add_category_form(self):
        form = CategoryForm()
        self.assertIn("name", form.fields)
        self.assertIn("description", form.fields)
        
        request = HttpRequest()
        request.POST = {
            "name": "Romance",
            "description":"Lovely"
        }

        form = CategoryForm(request.POST)
        form.save()

        response = self.client.get(reverse('RaisinRatings:index'))

        self.assertContains(response, "Romance")

class AddMovieForm(TestCase):
    def test_add_movie_form(self):
        form = MovieForm()
        self.assertIn("movie_name", form.fields)
        self.assertIn('main_actor', form.fields)
        self.assertIn('summary', form.fields)
        self.assertIn("trailer_link", form.fields)
        self.assertIn("poster", form.fields)
        self.assertIn("category", form.fields)

class AddReviewForm(TestCase):
    def test_add_review_form(self):
        form = ReviewForm()
        self.assertIn("title", form.fields)
        self.assertIn("review", form.fields)
        self.assertIn("starnum", form.fields)