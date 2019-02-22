from django.shortcuts import render, HttpResponse, redirect
from .models import Course
from django.contrib import messages

# Create your views here.
def index(request):
    
    return render(request,"courses/index.html",{"courses":Course.objects.all()})
def process(request):
    print(request.POST)
    print(request.POST)
    errors = Course.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect('/')
    course_list= Course.objects.create_course(request.POST)
    print(course_list)
    return redirect('/')
def remove(request,id):
    return render(request,"courses/remove.html",{"course":Course.objects.get(id=id)})
def dont(request):
    return redirect('/')
def destroy(request,id):
    course = Course.objects.get(id = id)
    course.delete()
    return redirect('/')
