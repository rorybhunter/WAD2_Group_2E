from django.urls import path
from RaisinRatings import views


app_name = 'RaisinRatings'

urlpatterns = [
    path('movie/<slug:movie_title_slug>/', views.show_movie, name='show_movie'),
    path('movie/<slug:movie_title_slug>/add_review/', views.add_review, name = 'add_review'),
    path('movie/<slug:movie_title_slug>/like/', views.like, name='like')

]