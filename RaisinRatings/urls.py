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
    # path('movie/<slug:movie_title_slug>/like/', views.like_movie, name='like_movie'),
    # path('movie/<slug:movie_title_slug>/dislike/', views.dislike_movie, name='dislike_movie'),
    path('movie/<slug:movie_title_slug>/delete/', views.delete_movie, name = 'delete_movie'),
    path('movie/<slug:movie_title_slug>/edit/', views.edit_movie, name='edit_movie'),
    path('categories/', views.categories, name='categories'),
    path('cat_page/', views.cat_page, name='category'), path('cat_page/', views.cat_page, name='category'),
    path('search/', views.search, name='search'),
    # path('search/<str:search_term>/', views.search, name='search'),
    path('cat_page/<slug:category_name_slug>/', views.cat_page, name='category'),
    path('add_category/', views.add_category, name='add_category'),
    # path('cat_page/<slug:category_name_slug>/like_category/', views.like_category, name = 'like_category'),
    # path('cat_page/<slug:category_name_slug>/dislike_category/', views.dislike_category, name = 'dislike_category'),
    path('like_category/', views.LikeCategoryView.as_view(), name='like_category'),
    path('dislike_category/', views.DislikeCategoryView.as_view(), name='dislike_category'),
    path('like_movie/', views.LikeMovieView.as_view(), name='like_movie'),
    path('user_page/<username>/', views.user_page, name='user_page'),
    path('dislike_movie/', views.DislikeMovieView.as_view(), name='dislike_movie')
]