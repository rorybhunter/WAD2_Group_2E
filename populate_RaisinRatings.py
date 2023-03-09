import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'WAD2_Group_2E.settings')

import django
django.setup()
from RaisinRatings.models import Category, Movie

from PIL import Image

def populate():
    romance_movies = [
        {'name':'The Notebook', 'main_actor':'Ryan Gosling', 'likes':134, 'poster': Image.open("example_posters/theNotebook")},
        {'name':'P.S I Love You','main_actor':'Hilary Swank', 'likes':23, 'poster': Image.open("example_posters/PSILoveYou")},
        {'name':'Mama Mia','main_actor':'Meryl Streep', 'likes':118, 'poster': Image.open("example_posters/MamaMia")} 
    ]

    horror_movies = [
        {'name':'The menu', 'main_actor':'Anya Taylor-Joy', 'likes':134, 'poster': Image.open("example_posters/theMenu")},
        {'name':'M3gan', 'main_actor':'Allison Williams', 'likes':134, 'poster': Image.open("example_posters/m3gan")},
        {'name':'Nope', 'main_actor':'Keke Palmer', 'likes':134, 'poster': Image.open("example_posters/nope")}
    ]


    cats = {'Romance': {'movies': romance_movies, 'likes': 128},
            'Horror': {'movies': horror_movies, 'likes': 64}
    }

    for cat, cat_data in cats.items():
        c = add_cat(cat, cat_data['likes'])
        for m in cat_data['pages']:
            add_page(c, m['name'], m['main_actor'], m['poster'], m['likes'])
    

    for c in Category.objects.all():
        for m in Movie.objects.filter(category=c):
            print(f'- {c}: {m}')

def add_page(cat, name, main_actor, poster, likes=0):
    m = Movie.objects.get_or_create(category=cat, name=name)[0]
    m.main_actor=main_actor
    m.poster = poster
    m.likes = likes
    m.save()
    return m

def add_cat(name, likes=0):
    c = Category.objects.get_or_create(name=name)[0]
    c.likes=likes
    c.save()
    return c

if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
