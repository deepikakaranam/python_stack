from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    return render(request,'survey/index.html')
def process(request):
    print(request.POST)
    request.session['name']=request.POST['name']
    request.session['location']=request.POST['location']
    request.session['Languages']=request.POST['Languages']
    request.session['description']=request.POST['description']
    request.session['tries'] += 1

    return render(request,'survey/result.html')