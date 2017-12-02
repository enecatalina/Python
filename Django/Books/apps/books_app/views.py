from __future__ import unicode_literals

from django.shortcuts import render, HttpResponse, redirect
from models import Author, Books
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.

def index(request):
    
    return render(request,'books/index.html')

def add(request):
    context = {
        "authors": Author.objects.all()
    }
    return render(request, 'books/add.html', context)
def show(request, book_id):
    context = {
        'book': Books.objects.get(id=book_id),
    }
    return render(request, "books/show.html", context)
def logout(request):
    request.session.clear()
    return redirect('/')