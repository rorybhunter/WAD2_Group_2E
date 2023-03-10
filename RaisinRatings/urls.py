from django.urls import path
from RaisinRatings import views

app_name = 'RaisinRatings'

urlpatterns = [
    path('',views.index, name='index'),   
    path('add_movie/', views.add_movie, name='add_movie'),
    path('movie/<slug:movie_title_slug>/detete_movie/', views.delete_movie, name = 'delete_movie'),
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('logout', views.user_logout, name = 'logout'),
    path('movie/<slug:movie_title_slug>/', views.show_movie, name='show_movie'),
    path('movie/<slug:movie_title_slug>/add_review/', views.add_review, name = 'add_review'),
    path('movie/<slug:movie_title_slug>/like/', views.like, name='like'),
    path('movie/<slug:movie_title_slug>/dislike/', views.dislike, name='dislike'),
    path('categories/', views.categories, name='categories'),
    path('cat_page/<slug:category_name_slug>/', views.cat_page, name='category'), 
    path('add_category/', views.add_category, name='add_category')
    
]
