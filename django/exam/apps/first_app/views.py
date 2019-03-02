from django.shortcuts import render,HttpResponse, redirect
from .models import User,Job
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"exam/index.html")
def process(request):
    print(request.POST)
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect("users:index")
    user_id = User.objects.create_user(request.POST)
    print(user_id)
   
    return redirect("users:index")
def login(request):
    print(request.POST)
    valid,result = User.objects.login(request.POST)
    if not valid:
        messages.error(request,result)
        return redirect("users:index")
    request.session['user_id']= result
    return redirect("users:dashboard")
def dashboard(request):
    context={
        
        "user" :  User.objects.get(id=request.session['user_id']),
        "jobs" : Job.objects.all(),
        "user_jobs": Job.objects.filter(user_id = request.session['user_id'] )
        
    }
    
    return render(request,"exam/dashboard.html",context)
def add_job(request):
    
    return render(request,"exam/add.html")
def add(request,id):
    job = Job.objects.get(id = id)
    job.user= User.objects.get(id=request.session['user_id'])
    job.save()

    return redirect("users:dashboard")
def create_job(request):
    print(request.POST)
    errors = Job.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect("users:add_job")
    job_id = Job.objects.create_job(request.POST,user_id = request.session['user_id'])
    
    print(job_id)
   
   
    return redirect("users:dashboard")
def view_job(request,id):
    
    context={
        "jobs":Job.objects.get(id=id)
    }

    return render(request,"exam/view.html",context)

    
def edit_job(request,id):
    
    context={
        "jobs":Job.objects.get(id=id),
        "user":  User.objects.get(id=request.session['user_id'])
    }
    return render(request,"exam/edit.html",context)
def update(request,id):
    errors = Job.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
            return render(request,"exam/edit.html")   
    else:
        job = Job.objects.get(id = id)
        job.title = request.POST['title']
        job.location = request.POST['location']
        job.description = request.POST['description']
        job.save()
    return redirect("users:dashboard")
def delete_job(request,id):
    
    job=Job.objects.get(id=id)
    job.delete()
    
    return redirect("users:dashboard")
def logout(request):
    request.session.clear()
    return redirect("users:index")
