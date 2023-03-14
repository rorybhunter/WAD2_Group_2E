import os
import random
from django.contrib.auth.models import User
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
'WAD2_Group_2E.settings')
import django
django.setup()
from RaisinRatings.models import UserProfile, Category, Movie, Review

def populate():
    users = [{'username':'testuser1', 'password':'boo', 'role':'COUCH_POTATO'},
    {'username':'testuser2','password': 'peek', 'role':'COUCH_POTATO'},
    {'username':'testcritic1', 'password': 'yikes', 'role':'CRITIC'},
    {'username':'testcritic2', 'password': 'beep', 'role':'CRITIC'},
    {'username':'testcreator1', 'password' : 'deep', 'role':'CREATOR'},
    {'username':'testcreator2', 'password': 'meep', 'role':'CREATOR'},
    ]

    cats = [{'name':'Horror', 'description': 'Scary Movies'}, {'name':'Drama', 'description': 'Dramatic Movies'}, 
    {'name':'Comedy', 'description': 'Funny Movies'}
    ]

    movies = [{'movie_name':'Horror Movie 1', 'main_actor': 'Main Actor 1', 'summary':'blank'}, 
    {'movie_name':'Drama Movie 1', 'main_actor': 'Main Actor 2', 'summary':'blank'},
    {'movie_name':'Comedy Movie 1', 'main_actor': 'Main Actor 3', 'summary':'blank'}]

    

    reviews = [{'title':'good', 'review':'I like this movie'}, {'title': 'bad', 'review': 'I do not like this movie'}, 
    {'title': 'underrated', 'review':'this movie is underrated'}, {'title': 'overrated', 'review':'this movie is overrated'}
    ]


    for cat in cats:
        c = add_category(cat['name'], cat['description'])
        print(f'-{c}')

    for user in users:
        u = add_user(user['username'], user['password'], user['role'])
        print(f'-{u}')

    categories = Category.objects.all()
    creators = UserProfile.objects.filter(role = 'CREATOR')

    for movie in movies:
        m = add_movie(movie['movie_name'], random.choice(categories), movie['main_actor'], movie['summary'], random.choice(creators).user)
        print(f'-{m}')

    critics = UserProfile.objects.filter(role = 'CRITIC')
    movies = Movie.objects.all()
    
    for review in reviews:
        add_review(review['title'], review['content'], random.choice(critics), random.choice(movies))


def add_user(username, password, role):
    u = User.objects.create_user(username = username, password = password)
    u.save()
    up = UserProfile.objects.get_or_create(user = u, user_type = role)
    return up

def add_category(name, description):
    c = Category.objects.get_or_create(name = name, description = description)[0]
    c.save()
    return c
    
def add_movie(movie_name, category, main_actor, summary, creator):
    m = Movie.objects.get_or_create(movie_name = movie_name, category_id =category, username = creator)[0]
    m.summary = summary
    m.main_actor = main_actor
    m.save()
    return m

def add_review(title, content, user, movie):
    r = Review.objects.get_or_create(title = title, content = content, user = user, movie = movie)[0]
    r.save()
    return r


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
