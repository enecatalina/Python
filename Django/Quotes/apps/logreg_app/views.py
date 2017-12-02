# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from models import *
from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages
import bcrypt

def index(request):
    return render(request, "index.html")

def create(request):
    errors = Users.objects.register_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error, extra_tags=tag)
        return redirect('/')
    else:
        messages.success(request,"You have logged in!")
        current_user = Users.objects.get(email = request.POST['email'])
        request.session['user_id'] = current_user.id
        print "user was created"
        return render(request,"success.html")
    print "user was able to create profile"

def success(request):
    print "show page working"
    current_user = Users.objects.get(id=request.session['user_id'])
    context = {
        'current_user': Users.objects.get(id=request.session['user_id']),
        'quotable_quotes' : Quote.objects.exclude(favorites=current_user),
        'favorites': current_user.favorites.all()
    }
    return render(request, "success.html", context)

def create_quote(request):
	##adds item to quotes
    current_user = Users.objects.get(id=request.session['user_id'])
    check = Quote.objects.validateQuote(request.POST)
    if check[0] == False:
		for error in check[1]:
			messages.add_message(request, messages.INFO, error, extra_tags="add_item")
			return redirect(reverse('quotes:success'))
    else:
        content = request.POST['content']
        author = request.POST['author']
        poster = current_user
        Quote.objects.create(content=content,author=author, poster=current_user)
		# return redirect(reverse('quotes:success'))
    return redirect(reverse('quotes:success'))

def add_favorites(request,id):
    current_user = Users.objects.get(id=request.session['user_id'])
    favorites = Quote.objects.get(id=id)
    current_user.favorites.add(favorites)
    return redirect(reverse('quotes:success'))

def remove_favorites(request,id):
    current_user = Users.objects.get(id=request.session['user_id'])
    favorite = Quote.objects.get(id=id)
    current_user.favorites.remove(favorite)
    print "user doesn't like this quote anymore"
    return redirect(reverse('quotes:success'))

def show(request,id):
    print "user made it to show profile page"
    user =  Users.objects.get(id = id)
    
    favorite = Users.objects.all()
    context = {
		'user': user,
		'favorites': user.favorites.all()	
	}
    return render(request, 'show.html', context)

def login(request):
    print "show page working"
    errors = Users.objects.login_validator(request.POST)
    if len(errors):
        for tag, error in errors.iteritems():
            messages.error(request, error)            
            return redirect('/')
    else:
        current_user = Users.objects.get(email=request.POST['email'])
        request.session['user_id']= current_user.id
        return redirect(reverse('quotes:success'))
    print "user was able to login"

def logout(request):
    request.session.clear()
    return redirect('/')