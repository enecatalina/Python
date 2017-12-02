# -*- coding: utf-8 -*-
from __future__ import unicode_literals


from django.shortcuts import render, redirect, HttpResponseRedirect, reverse
from django.contrib import messages
import bcrypt
from models import *

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
        return redirect(reverse('friends:success'))
    print "user was able to create profile"

def success(request):
    current_user = Users.objects.get(id=request.session['user_id'])
    users = Users.objects.exclude(friends=current_user).exclude(id=current_user.id)
    context = {
        'current_user': current_user,
        'users': users,
        'friends': current_user.friends.all()
    }
    return render(request, "success.html", context)

def add_friend(request, id):
    current_user = Users.objects.get(id=request.session['user_id'])
    friend = Users.objects.get(id=id)
    current_user.friends.add(friend)
    current_user.save()
    friend.friends.add(current_user)
    friend.save()
    return redirect(reverse('friends:success'))

def remove(request, id):
    current_user = Users.objects.get(id=request.session['user_id'])
    annoying_friend = Users.objects.get(id=id)
    current_user.friends.remove(annoying_friend)
    current_user.save()
    annoying_friend.friends.remove(current_user)
    annoying_friend.save()
    return redirect(reverse('friends:success'))

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
        return redirect(reverse('friends:success'))
    print "user was able to login"

def show(request, user_id):
    print "user made it to show profile page"
    context = {
        'current_user': Users.objects.get(id=user_id)
    }
    return render(request, "show.html", context)



def logout(request):
    request.session.clear()
    return redirect('/')