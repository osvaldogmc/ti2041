from django.shortcuts import render
from .models import Entry, Category, Hashtag, Post

def index(request):
    publicaciones = Entry.objects.all()
    categories = Category.objects.all()
    hashtag = Hashtag.objects.all()
    context = {
        'publicaciones': publicaciones,
        'categories': categories,
        'hashtag': hashtag
    }
    return render(request, 'index.html', context)

def secPost(request):
    publi = Post.objects.all()
    categories = Category.objects.all()
    hashtag = Hashtag.objects.all()
    context = {
        'publi': publi,
        'categories': categories,
        'hashtag': hashtag
    }
    return render(request, 'index2.html', context)

