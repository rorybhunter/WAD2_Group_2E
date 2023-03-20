import os
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
'WAD2_Group_2E.settings')
import django
django.setup()
from django.contrib.auth.models import User
from RaisinRatings.models import UserProfile, Category, Movie, Review
from PIL import Image
from WAD2_Group_2E.settings import MEDIA_DIR

def populate():
    users = [{'username':'testuser1', 'password':'boo', 'user_type':'COUCH_POTATO'},
    {'username':'testuser2','password': 'peek', 'user_type':'COUCH_POTATO'},
    {'username':'testcritic1', 'password': 'yikes', 'user_type':'CRITIC'},
    {'username':'testcritic2', 'password': 'beep', 'user_type':'CRITIC'},
    {'username':'testcreator1', 'password' : 'deep', 'user_type':'CREATOR'},
    {'username':'testcreator2', 'password': 'meep', 'user_type':'CREATOR'},
    ]

    cats = [{'name':'Horror', 'description': 'Scary Movies'}, {'name':'Drama', 'description': 'Dramatic Movies'}, 
    {'name':'Comedy', 'description': 'Funny Movies'}
    ]


    movies = [{'movie_name':'Horror Movie 1', 'main_actor': 'Main Actor 1', 'summary':'blank',
    'poster': os.path.join('example_posters', 'm3gan.jpg') , 'trailer_link':'https://www.youtube.com/watch?v=BRb4U99OU80&ab_channel=UniversalPictures'},
    {'movie_name':'Drama Movie 1', 'main_actor': 'Main Actor 2', 'summary':'blank',
    'poster':os.path.join('example_posters', 'PSILoveYou.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=1rqqidmUmSk&ab_channel=RottenTomatoesClassicTrailers'},
    {'movie_name':'Comedy Movie 1', 'main_actor': 'Main Actor 3', 'summary':'blank',
    'poster':os.path.join('example_posters', 'MamaMia.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=8RBNHdG35WY&ab_channel=ScreenBites'}]

    

    reviews = [{'title':'good', 'review':'I like this movie'}, {'title': 'bad', 'review': 'I do not like this movie'}, 
    {'title': 'underrated', 'review':'this movie is underrated'}, {'title': 'overrated', 'review':'this movie is overrated'}
    ]


    for cat in cats:
        c = add_category(cat['name'], cat['description'])
        print(f'-{c}')

    for user in users:
        u = add_user(user['username'], user['password'], user['user_type'])
        print(f'-{u}')

    categories = Category.objects.all()

    for movie in movies:
        m = add_movie(movie['movie_name'], random.choice(categories), movie['main_actor'], movie['summary'],  movie['poster'], movie['trailer_link'])
        print(f'-{m}')

    critics = UserProfile.objects.filter(user_type = 'CRITIC')
    movies = Movie.objects.all()

    for review in reviews:
        add_review(review['title'], review['review'], random.choice(critics).user, random.choice(movies))


def add_user(username, password, user_type):
    u = User.objects.create_user(username = username, password = password)
    u.save()
    up = UserProfile.objects.get_or_create(user = u, user_type = user_type)
    return up

def add_category(name, description):
    c = Category.objects.get_or_create(name = name, description = description)[0]
    c.save()
    return c

def add_movie(movie_name, category, main_actor, summary, poster = None, trailer_link = None):
    m = Movie.objects.get_or_create(movie_name = movie_name, category =category)[0]
    m.trailer_link = trailer_link
    m.summary = summary
    m.main_actor = main_actor
    m.poster = poster
    m.save()
    return m

def add_review(title, review, username, movie):
    r = Review.objects.get_or_create(title = title, review = review, username = username, movie = movie)[0]
    r.save()
    return r


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
