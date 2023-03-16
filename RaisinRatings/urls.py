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
    path('movie/<slug:movie_title_slug>/like/', views.like_movie, name='like_movie'),
    path('movie/<slug:movie_title_slug>/dislike/', views.dislike_movie, name='dislike_movie'),
    path('categories/', views.categories, name='categories'),
    path('cat_page/', views.cat_page, name='category'), path('cat_page/', views.cat_page, name='category'),
    path('search/', views.search, name='search'),
    path('cat_page/<slug:category_name_slug>/', views.cat_page, name='category'),
    path('add_category/', views.add_category, name='add_category'),
    path('cat_page/<slug:category_name_slug>/like_category/', views.like_category, name = 'like_category'),

]
