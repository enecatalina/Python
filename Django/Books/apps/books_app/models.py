# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
from ..logreg_app.models import Users
# Create your models here.

# class ReviewManager(models.Manager):
#     def review_validator(self, postdata):
#         errors = {}
#         if len(postdata['title']) < 5:
#             errors['title'] = "fields are required"
#         if len(postdata['review']) < 5:
#             errors['review'] = "fields are required"
#         if len(postdata['new_author']) <3:
#             errors['new_author'] = "New author field needs to be 3 or more characters"
#         if not 'author' in  postdata:
#             errors['author'] = "New author field needs to be 3 or more characters"
#         return errors
class Author(models.Model):
    name = models.CharField(max_length=100)

class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, related_name="books_created_by")

class Review(models.Model):
    review = models.TextField()
    rating = models.IntegerField()
    book = models.ForeignKey(Books, related_name="book_reviews")
    reviewer = models.ForeignKey(Users, related_name="reviews")
    created_at = models.DateTimeField(auto_now_add=True)
    # objects = ReviewManager