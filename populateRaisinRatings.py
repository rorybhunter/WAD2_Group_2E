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
    users = [{'username':'Mark', 'password':'boo', 'user_type':'COUCH_POTATO', 'picture': os.path.join('example_profiles', 'mark.jpg')},
    {'username':'Drew','password': 'peek', 'user_type':'COUCH_POTATO', 'picture': os.path.join('example_profiles', 'drew.jpg')},
    {'username':'Elize', 'password': 'yikes', 'user_type':'CRITIC', 'picture': os.path.join('example_profiles', 'elize.jpg')},
    {'username':'Nina', 'password': 'yikes', 'user_type':'CRITIC', 'picture': os.path.join('example_profiles', 'runeey.jpg')},
    {'username':'Anna', 'password': 'beep', 'user_type':'CRITIC', 'picture': os.path.join('example_profiles', 'anna.jpg')},
    {'username':'Erik', 'password' : 'deep', 'user_type':'CREATOR', 'picture': os.path.join('example_profiles', 'erik.jpg')},
    {'username':'Runeey', 'password': 'meep', 'user_type':'CREATOR', 'picture': os.path.join('example_profiles', 'runeey.jpg')},
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
    {'movie_name':'It', 'main_actor': 'Bill Skarsgård', 'summary':'In the summer of 1989, a group of bullied kids band together to destroy a shape-shifting monster, which disguises itself as a clown and preys on the children of Derry, their small Maine town.',
    'poster': os.path.join('example_posters', 'it.jpg') , 'trailer_link':'https://www.youtube.com/watch?v=xKJmEC5ieOk','likes': 50},
    {'movie_name':'Hereditary', 'main_actor': 'Toni Collette', 'summary':'A grieving family is haunted by tragic and disturbing occurrences.',
    'poster': os.path.join('example_posters', 'hereditory.jpg') , 'trailer_link':'https://www.youtube.com/watch?v=V6wWKNij_1M','likes': 51},
    {'movie_name':'Midsommar', 'main_actor': "Florence Pugh", 'summary':"A couple travels to Northern Europe to visit a rural hometown's fabled Swedish mid-summer festival. What begins as an idyllic retreat quickly devolves into an increasingly violent and bizarre competition at the hands of a pagan cult.",
    'poster': os.path.join('example_posters', 'midsommar.jpg') , 'trailer_link':'https://www.youtube.com/watch?v=1Vnghdsjmd0','likes': 51},
    {'movie_name':'World War Z', 'main_actor': "Brad Pitt", 'summary':"Former United Nations employee Gerry Lane traverses the world in a race against time to stop a zombie pandemic that is toppling armies and governments and threatens to destroy humanity itself.",
    'poster': os.path.join('example_posters', 'worldWarZ.jpg') , 'trailer_link':'https://www.youtube.com/watch?v=Md6Dvxdr0AQ','likes': 38},
    ]

    dramaMovies = [
    {'movie_name':'P.S I love you', 'main_actor': 'Hilary Swank', 'summary':'A young widow discovers that her late husband has left her 10 messages intended to help ease her pain and start a new life.',
    'poster':os.path.join('example_posters', 'PSILoveYou.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=1rqqidmUmSk&ab_channel=RottenTomatoesClassicTrailers', 'likes': 5}, 
    {'movie_name': 'The Notebook', 'main_actor': 'Ryan Gosling', 'summary': 'A poor yet passionate young man (Ryan Gosling) falls in love with a rich young woman (Rachel McAdams), giving her a sense of freedom, but they are soon separated because of their social differences.',
    'poster': os.path.join('example_posters', 'theNotebook.jpg'), 'trailer_link': 'https://www.youtube.com/watch?v=FC6biTjEyZw','likes': 10}, 
    {'movie_name':'Pride and prejudice', 'main_actor': 'Keira Knightley', 'summary':'Sparks fly when spirited Elizabeth Bennet meets single, rich, and proud Mr. Darcy. But Mr. Darcy reluctantly finds himself falling in love with a woman beneath his class. Can each overcome their own pride and prejudice?',
    'poster':os.path.join('example_posters', 'prideandpredjudice.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=Ur_DIHs92NM','likes': 34},
    {'movie_name':'The Fault in Our Stars', 'main_actor': 'Shailene Woodley', 'summary':'Two teenage cancer patients begin a life-affirming journey to visit a reclusive author in Amsterdam.',
    'poster':os.path.join('example_posters', 'theFaultInOurStars.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=9ItBvH5J6ss', 'likes': 17},
    {'movie_name':'Little Women', 'main_actor': 'Saoirse Ronan', 'summary':'Jo March reflects back and forth on her life, telling the beloved story of the March sisters - four young women, each determined to live life on her own terms.',
    'poster':os.path.join('example_posters', 'littleWomen.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=AST2-4db4ic', 'likes': 312}]

    comedyMovies = [ 
    {'movie_name':'Mamma Mia!', 'main_actor': 'Meryl Streep', 'summary':'The story of a bride-to-be trying to find her real father told using hit songs by the popular 1970s group ABBA.',
    'poster':os.path.join('example_posters', 'MamaMia.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=iCVpJ8x1Tnc','likes': 9},
    {'movie_name':'Little miss sunshine', 'main_actor': 'Steve Carell', 'summary':'A family determined to get their young daughter into the finals of a beauty pageant take a cross-country trip in their VW bus.',
    'poster':os.path.join('example_posters', 'littleMissSunshine.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=wvwVkllXT80', 'likes': -5}, 
    {'movie_name':'Legally Blonde', 'main_actor': 'Reese Witherspoon', 'summary':'Elle Woods, a fashionable sorority queen, is dumped by her boyfriend. She decides to follow him to law school. While she is there, she figures out that there is more to her than just looks.',
    'poster':os.path.join('example_posters', 'legallyBlonde.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=vWOHwI_FgAo', 'likes': 3}, 
    {'movie_name':"She's all that", 'main_actor': 'Rachael Leigh Cook', 'summary':"A high school jock makes a bet that he can turn an unattractive girl into the school's prom queen.",
    'poster':os.path.join('example_posters', 'shesAllThat.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=lHGweYtpQKI', 'likes': 85}, 
    ]

    kidsMovies = [
    {'movie_name':'Inside Out', 'main_actor': 'Amy Poehler', 'summary':'After young Riley is uprooted from her Midwest life and moved to San Francisco, her emotions - Joy, Fear, Anger, Disgust and Sadness - conflict on how best to navigate a new city, house, and school.',
    'poster':os.path.join('example_posters', 'insideOut.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=yRUAzGQ3nSY','likes': 9},
    {'movie_name':'Toy Story', 'main_actor': 'Tom Hanks', 'summary':"A cowboy doll is profoundly threatened and jealous when a new spaceman action figure supplants him as top toy in a boy's bedroom.",
    'poster':os.path.join('example_posters', 'toyStory.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=v-PjgYDrg70', 'likes': 200},
    {'movie_name':'Encanto', 'main_actor': 'Stephanie Beatriz', 'summary':'A Colombian teenage girl has to face the frustration of being the only member of her family without magical powers.',
    'poster':os.path.join('example_posters', 'encanto.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=CaimKeDcudo', 'likes': 3}, 
    {'movie_name':"Moana", 'main_actor': "Auli'i Cravalho", 'summary':"In Ancient Polynesia, when a terrible curse incurred by the Demigod Maui reaches Moana's island, she answers the Ocean's call to seek out the Demigod to set things right.",
    'poster':os.path.join('example_posters', 'moana.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=LKFuXETZUsI', 'likes': 72}, 
    {'movie_name':"Frozen", 'main_actor': "Kristen Bell", 'summary':"When the newly crowned Queen Elsa accidentally uses her power to turn things into ice to curse her home in infinite winter, her sister Anna teams up with a mountain man, his playful reindeer, and a snowman to change the weather condition.",
    'poster':os.path.join('example_posters', 'frozen.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=TbQm5doF_Uc', 'likes': 90},
    {'movie_name':"Monster's inc", 'main_actor': "Billy Crystal", 'summary':"In order to power the city, monsters have to scare children so that they scream. However, the children are toxic to the monsters, and after a child gets through, two monsters realize things may not be what they think.",
    'poster':os.path.join('example_posters', 'monsters.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=6tCxnHCqqxg', 'likes': 13},
    {'movie_name':"Winnie the pooh", 'main_actor': "Jim Cummings", 'summary':"While searching for honey, Pooh and his friends embark on an adventure to find Eeyore's missing tail and rescue Christopher Robin from an unknown monster called The Backson.",
    'poster':os.path.join('example_posters', 'winnie.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=izCNXpKfIlE', 'likes': 13}

    ]
    musicals = []
    adventureMovies = [{'movie_name':"The hunger games", 'main_actor': "Jennifer Lawrence", 'summary':"Katniss Everdeen voluntarily takes her younger sister's place in the Hunger Games: a televised competition in which two teenagers from each of the twelve Districts of Panem are chosen at random to fight to the death.",
    'poster':os.path.join('example_posters', 'hungerGames.jpg'), 'trailer_link':'https://www.youtube.com/watch?v=mfmrPu43DF8', 'likes': 117}]
    documenteries = []
    romanticMovies = []
    thrillers = []


    reviews = [{'title':'Good', 'review':'I like this movie a lot!', 'starnum': 4},
    {'title': 'Bad', 'review': 'I do not like this movie', 'starnum': 1},
    {'title': 'Underrated', 'review':'this movie is underrated.', 'starnum': 4},
    {'title': 'Overrated', 'review':'This movie is overrated', 'starnum': 2},
    {'title': 'Fun', 'review': "This movie is fun but don't expect much else.", 'starnum': 3},
    {'title': 'Bad', 'review': 'I do not like this movie', 'starnum': 2},
    {'title':'Good', 'review':'I like this movie a lot!', 'starnum': 4},
    {'title': 'Underrated', 'review':'this movie is underrated.', 'starnum': 4},
    {'title': 'Overrated', 'review':'This movie is overrated', 'starnum': 2},
    {'title': 'Loved it!', 'review': 'This is one of my all time favorite movies! Everyone should watch it.', 'starnum': 5},
    {'title': 'Loved it!', 'review': 'This is one of my all time favorite movies! Everyone should watch it.', 'starnum': 5},
    {'title': 'Loved it!', 'review': 'This is one of my all time favorite movies! Everyone should watch it.', 'starnum': 5},
    {'title':'Good', 'review':'I like this movie a lot!', 'starnum': 4},
    {'title': 'Bad', 'review': 'I do not like this movie', 'starnum': 1},
    {'title': 'Underrated', 'review':'this movie is underrated.', 'starnum': 4},
    {'title': 'Overrated', 'review':'This movie is overrated', 'starnum': 2},
    {'title': 'Fun', 'review': "This movie is fun but don't expect much else.", 'starnum': 3},
    {'title': 'Bad', 'review': 'I do not like this movie', 'starnum': 2},
    {'title':'Good', 'review':'I like this movie a lot!', 'starnum': 4},
    {'title': 'Underrated', 'review':'this movie is underrated.', 'starnum': 4},
    {'title': 'Overrated', 'review':'This movie is overrated', 'starnum': 2},
    {'title': 'Loved it!', 'review': 'This is one of my all time favorite movies! Everyone should watch it.', 'starnum': 5},
    {'title': 'Loved it!', 'review': 'This is one of my all time favorite movies! Everyone should watch it.', 'starnum': 5},
    {'title': 'Loved it!', 'review': 'This is one of my all time favorite movies! Everyone should watch it.', 'starnum': 5},]

    
    cats = {
        'Horror': {'description': 'Scary Movies', 'movies': horrorMovies, 'likes': 3}, 
        'Drama': {'description': 'Dramatic Movies', 'movies': dramaMovies, 'likes': 8},
        'Comedy': {'description': 'Funny Movies', 'movies': comedyMovies, 'likes': 10},
        "Kid's Movies": {'description': 'Movies for children', 'movies': kidsMovies, 'likes': 10},
        "Musicals": {'description': "Movies with singing and music", 'movies': musicals, 'likes': 1},
        "Adventure movies": {'description': "Suspensfull stories", 'movies': adventureMovies, 'likes': 2},
        "Documenteries": {'description': "Non-fiction movies", 'movies': documenteries, 'likes': 1},
        "Thrillers": {'description': "Suspencfull movies", 'movies': thrillers, 'likes': 1},
        "Romantic movies": {'description': "Movies about love", 'movies': romanticMovies, 'likes': 1},
    }
    for user in users:
        u = add_user(user['username'], user['password'], user['user_type'], user['picture'])
        print(f'-{u}')

    creators = UserProfile.objects.filter(user_type = 'CREATOR')

    for cat, cat_data in cats.items():
        c = add_category(cat, cat_data['description'], cat_data['likes'])
        for m in cat_data['movies']:
            m = add_movie(m['movie_name'], c, random.choice(creators).user, m['main_actor'], m['summary'], m['likes'],  m['poster'], m['trailer_link'])



    critics = UserProfile.objects.filter(user_type = 'CRITIC')
    movies = Movie.objects.all()


    for review in reviews:
        add_review(review['title'], review['review'], random.choice(critics).user, random.choice(movies), review['starnum'])


def add_user(username, password, user_type, picture):
    u = User.objects.create_user(username = username, password = password, )
    u.save()
    up = UserProfile.objects.get_or_create(user = u, user_type = user_type, picture=picture)
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

def add_review(title, review, username, movie, starnum):
    r = Review.objects.get_or_create(title = title, review = review, username = username, movie = movie, starnum = starnum)[0]
    r.save()
    return r


if __name__ == '__main__':
    print('Starting Rango population script...')
    populate()
