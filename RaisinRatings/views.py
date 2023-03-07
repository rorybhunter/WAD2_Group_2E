from django.shortcuts import render
from django.http import HttpResponse
from RaisinRatings.models import Category

def categories(request):
    category_list = Category.objects.order_by('-likes')[:5]

    context_dict = {}
    context_dict['boldmessage'] = 'Select a category:'
    context_dict['categories'] = category_list
    
    return render(request, 'RaisinRatings/categories.html', context=context_dict)

def cat_page(request):
    context_dict = {'boldmessage': 'Hmm'}
    return render(request, 'RaisinRatings/cat_page.html', context=context_dict)