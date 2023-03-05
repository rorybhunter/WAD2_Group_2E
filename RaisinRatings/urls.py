from django.urls import path
from RaisinRatings import views

app_name = 'RaisinRatings'

urlpatterns = [
    # path(<string to match>, <view to call>, <name, way to reference view, optional>)
    path('',views.index, name='index'),
    path('register/', views.register, name='register'),
]
