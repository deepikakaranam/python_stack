

# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
  
def index(request):
    response = "LIST OF ALL BLOGS!"
    return HttpResponse(response)
    
def new(request):
    response = "Create a new blog"
    return HttpResponse(response)
def create(request):
    response="Added to list"
    return redirect('/')
def add_number(request,number):
    print (number)
    return HttpResponse("blog" + number)
def edit(request,number):
    print(number)
    return HttpResponse("edit blog" + number)
def destroy(request,number):
    print(number)
    return HttpResponse("delete blog" + number)