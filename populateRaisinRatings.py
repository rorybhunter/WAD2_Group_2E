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

    horrorMovies = [
    {'movie_name':'M3gan', 'main_actor': 'Amie Donald', 'summary':'A robotics engineer at a toy company builds a life-like doll that begins to take on a life of its own.',
    'poster': os.path.join('example_posters', 'm3gan.jpg') , 'trailer_link':'https://www.youtube.com/watch?v=BRb4U99OU80&ab_channel=UniversalPictures', 'likes': 10}, 
    {'movie_name':'Saw', 'main_actor': 'Cary Elwes', 'summary':'Two strangers awaken in a room with no recollection of how they got there, and soon discover theyre pawns in a deadly game perpetrated by a notorious serial killer.',
    'poster': os.path.join('example_posters', 'saw.jpg') , 'trailer_link':'https://www.youtube.com/watch?v=S-1QgOMQ-ls', 'likes': 7}, 
    {'movie_name':'Us', 'main_actor': 'Lupita Nyongo', 'summary':'A familys serene beach vacation turns to chaos when their doppelgängers appear and begin to terrorize them.',
    'poster': os.path.join('example_posters', 'us.jpg') , 'trailer_link':'https://www.youtube.com/watch?v=hNCmb-4oXJA', 'likes': 25}, 
    {'movie_name':'Sream', 'main_actor': 'Neve Campbell', 'summary':'A year after the murder of her mother, a teenage girl is terrorized by a new killer, who targets the girl and her friends by using horror films as part of a deadly game.',
    'poster': os.path.join('example_posters', 'scream.jpg') , 'trailer_link':'https://www.youtube.com/watch?v=AWm_mkbdpCA','likes': 8},
    ]

    dramaMovies = [
    {'movie_name':'P.S I love you', 'main_actor': 'Hilary Swank', 'summary':'A young widow discovers that her late husband has left her 10 messages intended to help ease her pain and start a new life.',
    'poster':os.path.join('example_posters', 'PSILoveYou.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=1rqqidmUmSk&ab_channel=RottenTomatoesClassicTrailers', 'likes': 5}, 
    {'movie_name': 'The Notebook', 'main_actor': 'Ryan Gosling', 'summary': 'A poor yet passionate young man (Ryan Gosling) falls in love with a rich young woman (Rachel McAdams), giving her a sense of freedom, but they are soon separated because of their social differences.',
    'poster': os.path.join('example_posters', 'theNotebook.jpg'), 'trailer_link': 'https://www.youtube.com/watch?v=FC6biTjEyZw','likes': 10}, 
    {'movie_name':'Pride and prejudice', 'main_actor': 'Keira Knightley', 'summary':'Sparks fly when spirited Elizabeth Bennet meets single, rich, and proud Mr. Darcy. But Mr. Darcy reluctantly finds himself falling in love with a woman beneath his class. Can each overcome their own pride and prejudice?',
    'poster':os.path.join('example_posters', 'prideandpredjudice.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=Ur_DIHs92NM','likes': 34},
    {'movie_name':'The Fault in Our Stars', 'main_actor': 'Shailene Woodley', 'summary':'Two teenage cancer patients begin a life-affirming journey to visit a reclusive author in Amsterdam.',
    'poster':os.path.join('example_posters', 'theFaultInOurStars.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=9ItBvH5J6ss', 'likes': 17}]

    comedyMovies = [ 
    {'movie_name':'Mamma Mia!', 'main_actor': 'Meryl Streep', 'summary':'The story of a bride-to-be trying to find her real father told using hit songs by the popular 1970s group ABBA.',
    'poster':os.path.join('example_posters', 'MamaMia.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=8RBNHdG35WY&ab_channel=ScreenBites','likes': 9},
    {'movie_name':'Little miss sunshine', 'main_actor': 'Steve Carell', 'summary':'A family determined to get their young daughter into the finals of a beauty pageant take a cross-country trip in their VW bus.',
    'poster':os.path.join('example_posters', 'littleMissSunshine.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=wvwVkllXT80', 'likes': -5}, 
    {'movie_name':'Legally Blonde', 'main_actor': 'Reese Witherspoon', 'summary':'Elle Woods, a fashionable sorority queen, is dumped by her boyfriend. She decides to follow him to law school. While she is there, she figures out that there is more to her than just looks.',
    'poster':os.path.join('example_posters', 'legallyBlonde.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=vWOHwI_FgAo', 'likes': 3}, 
     {'movie_name':"She's all that", 'main_actor': 'Rachael Leigh Cook', 'summary':"A high school jock makes a bet that he can turn an unattractive girl into the school's prom queen.",
    'poster':os.path.join('example_posters', 'shesAllThat.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=lHGweYtpQKI', 'likes': 85}, 
    ]

    comedyMovies = [ 
    {'movie_name':'Inside Out', 'main_actor': 'Amy Poehler', 'summary':'After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house, and school.',
    'poster':os.path.join('example_posters', 'insideOut.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=yRUAzGQ3nSY','likes': 9},
    {'movie_name':'Toy Story', 'main_actor': 'Tom Hanks', 'summary':"A cowboy doll is profoundly threatened and jealous when a new spaceman action figure supplants him as top toy in a boy's bedroom.",
    'poster':os.path.join('example_posters', 'toyStory.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=v-PjgYDrg70', 'likes': 500}, 
    {'movie_name':'Encanto', 'main_actor': 'Stephanie Beatriz', 'summary':'A Colombian teenage girl has to face the frustration of being the only member of her family without magical powers.',
    'poster':os.path.join('example_posters', 'encanto.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=CaimKeDcudo', 'likes': 3}, 
     {'movie_name':"Moana", 'main_actor': "Auli'i Cravalho", 'summary':"In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches Moana's island, she answers the Ocean's call to seek out the Demigod to set things right.",
    'poster':os.path.join('example_posters', 'moana.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=LKFuXETZUsI', 'likes': 72}, 
    ]

    reviews = [{'title':'Good', 'review':'I like this movie a lot!'}, 
    {'title': 'Bad', 'review': 'I do not like this movie'},
    {'title': 'Underrated', 'review':'this movie is underrated.'}, 
    {'title': 'Overrated', 'review':'This movie is overrated'},
     {'title': 'Fun', 'review': "This movie is fun but don't expect much else."},
    {'title': 'Bad', 'review': 'I do not like this movie'}, 
    {'title':'Good', 'review':'I like this movie a lot!'}, 
    {'title': 'Underrated', 'review':'this movie is underrated.'},
    {'title': 'Overrated', 'review':'This movie is overrated'},
    {'title': 'Loved it!', 'review': 'This is one of my all time favorite movies! Everyone should watch it.'}, 
    {'title': 'Loved it!', 'review': 'This is one of my all time favorite movies! Everyone should watch it.'}, 
    {'title': 'Loved it!', 'review': 'This is one of my all time favorite movies! Everyone should watch it.'}]

    
    cats = {
        'Horror': {'description': 'Scary Movies', 'movies': horrorMovies, 'likes': 3}, 
        'Drama': {'description': 'Dramatic Movies', 'movies': dramaMovies, 'likes': 8},
        'Comedy': {'description': 'Funny Movies', 'movies': comedyMovies, 'likes': 10}
    }
    for user in users:
        u = add_user(user['username'], user['password'], user['user_type'])
        print(f'-{u}')

    creators = UserProfile.objects.filter(user_type = 'CREATOR')

    for cat, cat_data in cats.items():
        c = add_category(cat, cat_data['description'], cat_data['likes'])
        for m in cat_data['movies']:
            m = add_movie(m['movie_name'], c, random.choice(creators).user, m['main_actor'], m['summary'], m['likes'],  m['poster'], m['trailer_link'])

    critics = UserProfile.objects.filter(user_type = 'CRITIC')
    movies = Movie.objects.all()

    for review in reviews:
        add_review(review['title'], review['review'], random.choice(critics).user, random.choice(movies))


def add_user(username, password, user_type):
    u = User.objects.create_user(username = username, password = password)
    u.save()
    up = UserProfile.objects.get_or_create(user = u, user_type = user_type)
    return up

def add_category(name, description, likes):
    c = Category.objects.get_or_create(name = name, description = description, likes = likes)[0]
    c.save()
    return c


def add_movie(movie_name, category, user, main_actor, summary, likes, poster = None, trailer_link = None):
    
    m = Movie.objects.get_or_create(movie_name = movie_name, category =category, user=user)[0]
    m.trailer_link = trailer_link
    m.summary = summary
    m.main_actor = main_actor
    m.poster = poster
    m.likes = likes
    m.save()
    return m

def add_review(title, review, username, movie):
    r = Review.objects.get_or_create(title = title, review = review, username = username, movie = movie)[0]
    r.save()
    return r


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
