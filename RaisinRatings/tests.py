from django.test import TestCase
from RaisinRatings.models import Category, UserProfile, Movie
from django.urls import reverse
from django.contrib.auth.models import User
# Create your tests here.

class CategoryMethodTests(TestCase):
    def test_slug_line_creation(self):
        category = Category(name = 'Random Category String')
        category.save()

        self.assertEqual(category.slug, 'random-category-string')

class MovieMethodTests(TestCase):
    def test_slug_line_creation(self):
        category = Category(name = 'Random Category String')
        category.save()

        self.assertEqual(category.slug, 'random-category-string')


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

        creator = User.objects.create(username = "Eddie Murphy", password = "Norbit")

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
        horror_cat = add_category('Horror', 2)
        drama_cat = add_category('Drama', 5)
        comedy_cat = add_category('Comedy', 7)

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
        user = User.objects.create(username = "Norbit", password = "spaceship")

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
        user = User.objects.create(username = "Norbit", password = "spaceship")

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


class EditMovieViewTest(TestCase):
    pass