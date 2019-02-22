from django.shortcuts import render, HttpResponse,redirect
from .models import Register
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"login_reg/index.html")
def process(request):
    print(request.POST)
    errors = Register.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect('/')
    user_list= Register.objects.create_user(request.POST)
    print(user_list)
    return redirect('/')
def login(request):
    print(request.POST)
    valid, result = Register.objects.login(request.POST)
    if not valid:
        messages.error(request, result)
        return redirect('/')
    
    
    return render(request,"login_reg/success.html")
def logout(request):
    request.session.clear()
    return redirect('/')

    
    

    