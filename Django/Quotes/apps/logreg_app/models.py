# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
import re
import bcrypt
from django.core.exceptions import ObjectDoesNotExist
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9\.\+_-]+@[a-zA-Z0-9\._-]+\.[a-zA-Z]*$')
NAME_REGEX = re.compile(r'^[A-Za-z]\w+$')

# Create your models here.
class BlogManager(models.Manager):
    def register_validator(self, postData):
        errors = {}
        # check length of first and last name
        if len(postData['first_name']) < 2:
            errors['first_name']= "Field name is too short has to be more than 2 letters"
        if len(postData['last_name']) < 2:
            errors['last_name']= "Field name is too short has to be more than 2 letters"
        # check length of the password
        if len(postData['password']) < 8:
            errors['password']= "password must be at least 8 characters"
        if not re.match(EMAIL_REGEX, postData['email']):
            errors['email'] = ("invalid email")
        if not re.match(NAME_REGEX, postData['first_name']):
            errors['first_name'] = ("invalid name field")
        if not re.match(NAME_REGEX, postData['last_name']):
            errors['last_name'] = ("invalid name field")
        # check password == password_confirm
        if postData['password'] != postData['cfpassword']:
            errors['password']=("passwords do not match")
        try:
            Users.objects.get(email = postData['email'])
        except ObjectDoesNotExist:
            pass
        else: 
            errors['email'] = "email is already been used"
        if errors:
            return errors
        else:
            hashed = bcrypt.hashpw(postData['password'].encode('utf8'), bcrypt.gensalt(5))
            print hashed
            Users.objects.create(first_name=postData['first_name'],last_name=postData['last_name'],email=postData['email'], password=hashed)
            return errors

    def login_validator(self, postData):
        errors = {}
        # if not EMAIL_REGEX.match(postData['email']):
        #     errors['email']('Please enter a valid email!')
        if len(postData['email']) < 8:
            errors['email'] = "email invaild"
        if len(postData['password']) < 8:
            errors['password'] = "password invalid"
        if errors:
            print "FAILING BASIC VALIDATIONS"
            return errors 
        try:
            print "GOT TO THE TRY BLOCK"
            correct_user = Users.objects.get(email = postData['email'])
            print postData['password']
            print correct_user.password
            if not bcrypt.checkpw(postData['password'].encode('utf8'), correct_user.password.encode('utf8')):
                errors['password'] = 'invalid credentials!!!!!!!!'
        except:
            errors['email'] = "No user registered with that email"
        return errors
    
class Users(models.Model):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.CharField(max_length=255)
    birthday = models.DateTimeField(blank=True, null=True)  
    favorites = models.ManyToManyField("Quote", related_name="favorites", default=None)
    password = models.CharField(max_length=20)
    cfpassword = models.CharField(max_length=20)
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = BlogManager()

class QuoteManager(models.Manager):
    def validateQuote(self, postData):
        is_valid = True
        errors = []
        if len(postData.get('content')) < 10:
            is_valid = False
            errors.append('Message must be more than 10 characters')
        return (is_valid, errors)

class Quote(models.Model):
    content = models.TextField()
    author = models.CharField(max_length = 255)
    poster = models.ForeignKey(Users, related_name = 'authored_quotes')
    created_at = models.DateTimeField(auto_now_add = True)
    updated_at = models.DateTimeField(auto_now = True)
    objects = QuoteManager()
