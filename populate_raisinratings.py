import os
import random
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 
'WAD2_Group_2E.settings')

import django
django.setup()
from RaisinRatings.models import User, Category, Movie, Comment

def populate():
    users = [{'username':'testuser1', 'password':'ilikecats123', 'role':'USER', 'tag':'average movie enjoyer'},
    {'username':'testuser2', 'password':'ilikedogs123', 'role':'USER', 'tag': 'non-average movie enjoyer'},
    {'username':'testcritic1', 'password':'iliketurtles123', 'role':'CRITIC', 'tag':'best critic in the world'},
    {'username':'testcritic2', 'password':'ilikerabbits123', 'role':'CRITIC', 'tag':'worst critic in the world'},
    {'username':'testcreator1', 'password':'ilikebats123', 'role':'CREATOR', 'tag':'your favorite movie creator'},
    {'username':'testcreator2', 'password':'ilikerats123', 'role':'CREATOR', 'tag':'your least favorite movie creator'},
    ]

    cats = [{'name':'Horror'}, {'name':'Drama'}, {'name':'Comedy'}
    ]

    horror_movie = {'name':'Horror Movie 1', 'main_actor': 'Main Actor 1'}

    drama_movie = {'name':'Drama Movie 1', 'main_actor': 'Main Actor 2'}

    comedy_movie = {'name':'Comedy Movie 1', 'main_actor': 'Main Actor 3'}

    comments = [{'content':'I like this movie'}, {'content': 'I do not like this movie'}, 
    {'content':'this movie is underrated'}, {'content':'this movie is overrated'}
    ]

    for user in users:
        u = add_user(user['username'], user['password'], user['role'], user['tag'])
        print(f'-{u}')

    creators = []

    for creator in User.objects.filter(role='CREATOR'):
        creators.append(creator)

    users = []

    for user in User.objects.filter(role='USER'):
        users.append(user)


    for c in cats:
        c = add_category(c['name'], random.choice(creators))
        print(f'-{c}')

    horror_m = add_movie(horror_movie['name'], category = Category.objects.filter(name = 'Horror')[0], creator = random.choice(creators), rater=random.choice(users))
    print(f'-{horror_m}')

    drama_m = add_movie(drama_movie['name'], category= Category.objects.filter(name = 'Drama')[0], creator = random.choice(creators), rater=random.choice(users))
    print(f'-{drama_m}')

    comedy_m = add_movie(comedy_movie['name'], category= Category.objects.filter(name = "Comedy")[0], creator = random.choice(creators), rater = random.choice(users))
    print(f'-{comedy_m}')
    
    movies = []

    for m in Movie.objects.all():
        movies.append(m)


    comment1 = comments[0]
    comment1 = add_comment(content = comment1['content'], user = User.objects.filter(role = 'CRITIC')[0], movie = random.choice(movies))

    comment2 = comments[1]
    comment2 = add_comment(content = comment2['content'], user = User.objects.filter(role = 'CRITIC')[0], movie = random.choice(movies))

    comment3 = comments[2]
    comment3 = add_comment(content = comment3['content'], user = User.objects.filter(role = 'CRITIC')[1], movie = random.choice(movies))

    comment4 = comments[3]
    comment4 = add_comment(content = comment4['content'], user = User.objects.filter(role = 'CRITIC')[1], movie = random.choice(movies))


def add_user(username, password, role, tag):
    u = User.objects.get_or_create(username = username, password = password)[0]
    role = role
    u.tag = tag
    u.save()
    return u

def add_category(name, creator, likes=0):
    c = Category.objects.get_or_create(name = name, creator = creator)[0]
    c.likes = likes
    c.save()
    return c
    
def add_movie(name, category, main_actor, creator, rater):
    m = Movie.objects.get_or_create(name = name, category_id =category, creator = creator)[0]
    m.main_actor = main_actor
    m.save()
    m.user_raters.add(rater)
    return m

def add_comment(content, user, movie):
    c = Comment.objects.get_or_create(content = content, user = user, movie = movie)[0]
    c.save()
    return c


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
