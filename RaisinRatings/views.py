from django.shortcuts import render
from django.http import HttpResponse

def categories(request):
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}
    return render(request, 'RaisinRatings/categories.html', context=context_dict)

def cat_page(request):
    context_dict = {'boldmessage': 'Hmm'}
    return render(request, 'RaisinRatings/cat_page.html', context=context_dict)