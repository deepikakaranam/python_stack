from django.shortcuts import render, HttpResponse, redirect
from .models import User
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request,"main/index.html",{"users":User.objects.all()})
def new(request):
    
    
    return render(request,"main/new.html")
def create(request):
    print(request.POST)
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect('/new')
    user_list= User.objects.create_user(request.POST)
    print(user_list)
    
        
    return redirect('/users')
def edit(request,id):
    
    return render(request,"main/edit.html",{"user":User.objects.get(id = id)})
def update(request,id):
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
            return redirect('/edit')   
    else:
        user = User.objects.get(id = id)
        user.first_name = request.POST['first_name']
        user.last_name = request.POST['last_name']
        user.email = request.POST['email']
        user.save()
        
        # redirect to a success route
        return redirect('/users')  
    
    

def show(request,id):
    return render(request,"main/show.html",{"users":User.objects.get(id=id)})
def destroy(request,id):
    user = User.objects.get(id = id)
    user.delete()
    return redirect('/users')
