from django.urls import path
from RaisinRatings import views

app_name = 'RaisinRatings'

urlpatterns = [
    path('',views.index, name='index'),   
    path('add_movie/', views.add_movie, name='add_movie'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('movie/<slug:movie_title_slug>/', views.show_movie, name='show_movie'),
    path('movie/<slug:movie_title_slug>/add_review/', views.add_review, name = 'add_review'),
    path('movie/<slug:movie_title_slug>/like/', views.like, name='like'),
    path('', views.categories, name='categories'),
    path('cat_page/', views.cat_page, name='category'),
]
