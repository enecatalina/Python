# -*- coding: utf-8 -*-
from django.shortcuts import render, HttpResponse, redirect
from django.shortcuts import render
from django.utils.crypto import get_random_string

# Create your views here.
def index(request): 
    try:
        request.session['count'] 
    except KeyError:
        request.session['count'] = 0
    return render(request,"index.html")

def generate(request): 
    request.session['count'] += 1  
    request.session['word'] = get_random_string(length=10)
    return redirect('/')

#reset sessions
def reset(request):
    request.session.clear()
    return redirect('/')




    # if request.method == "POST":
    #     request.session['count'] += 1
    #     return redirect('/')
    # if not 'count' in request.session:
    #     request.session['count'] = 1
    # return redirect("index.html") 