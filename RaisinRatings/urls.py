from django.urls import path
from RaisinRatings import views

app_name = 'RaisinRatings'

urlpatterns = [
    path('',views.index, name='index'),   
    path('add_movie/', views.add_movie, name='add_movie')
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login')
]

