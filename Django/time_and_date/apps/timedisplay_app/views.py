from django.shortcuts import render, HttpResponse, redirect
from django.utils import timezone
from django.shortcuts import render

  # the index function is called when root is visited

def index(request):
    context = {
        'now' : timezone.now()
    }
    return render(request, "index.html", context)


