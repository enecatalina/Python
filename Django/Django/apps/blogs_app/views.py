from django.shortcuts import render, HttpResponse, redirect
  # the index function is called when root is visited

def index(request):
  print "placeholder to later display all the list of blogs (made it to index)" 
  return render(request,"index.html")

def new(request):
    return HttpResponse("placeholder to display a new form to create a new blog")

def create(request):
    return redirect('/')

def show(request,number):
    context ={
      'number':number
    }
    print "number worked"
    return render(request,'shownumber.html', context)

def edit(request,number):
    context ={
      'number':number
    }
    print "number worked"
    return render(request,'showeditnumber.html', context)

def delete(request,number):
    return redirect('/blogs_app')
