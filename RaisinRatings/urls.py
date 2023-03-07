from django.urls import path
from RaisinRatings import views

app_name = 'RaisinRatings'

urlpatterns = [
    path('', views.categories, name='categories'),
    path('cat_page/', views.cat_page, name='category'),
]