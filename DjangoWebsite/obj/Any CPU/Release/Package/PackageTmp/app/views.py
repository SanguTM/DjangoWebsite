"""
Definition of views.
"""

from datetime import datetime
from django.shortcuts import render
from django.http import HttpRequest
from django.http import HttpResponse
from .models import Post

post = [
        {
            'author': 'Linas',
            'title': 'testas',
            'content': 'testas 1',
            'data': '2022.11.22'
        },
         {
            'author': 'Linas',
            'title': 'testas!!',
            'content': 'testas 2',
            'data': '2022.11.22'
        },
    ]

def home(request):
    context = {
            'posts':Post.objects.all()
        }

    return render(request, 'app/index.html', context)
    #return HttpResponse('<h1>Website home</h1>')

def about(request):
    return render(request, 'app/about.html', {'title': 'About'})

def galery(request):
    return render(request, 'app/galery.html')

def prenumerate(request):
     return render(request, 'app/prenumerate.html')


