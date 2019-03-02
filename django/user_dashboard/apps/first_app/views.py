from django.shortcuts import render, redirect
from . models import User
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,'user_dashboard/index.html')
def signin(request):
    return render(request,'user_dashboard/login.html')

def process(request):
    print("process",request.POST)
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect('users:register')
    user_id = User.objects.create_user(request.POST)
    print(user_id)
    
    return redirect('users:register')
def login(request):
    print(request.POST)
    valid, result = User.objects.login(request.POST)
    if not valid:
        messages.error(request,result)
        return redirect ('users:signin')
    return render(request,'user_dashboard/success.html')
def register(request):
    print("register",request.POST)
    return render(request,'user_dashboard/register.html')
def success(request):
    return render(request,'user_dashboard/success.html')



