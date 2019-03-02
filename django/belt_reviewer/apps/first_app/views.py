from django.shortcuts import render,HttpResponse, redirect
from .models import User,Book,Review
from django.contrib import messages
from django.core.urlresolvers import reverse
# Create your views here.
def index(request):
    return render(request,"belt_reviewer/index.html")
def process(request):
    print("register", request.POST)
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect("users:index")
    user_id = User.objects.login(request.POST)
    print("first one",user_id)
    request.session['user_id']= user_id
    request.session['first_name'] = request.POST['first_name']
    print("this one '*' *30",request.session['user_id'])
    
    return redirect("users:index")
def login(request):
    print(request.POST)
    valid, result = User.objects.login(request.POST)
    if not valid:
        messages.error(request, result)
        return redirect("users:index")
    return redirect("users:books")
def books(request):
    context={
        
        "user" :  User.objects.get(id=request.session['user_id']),
        "books": Book.objects.all(),
        
        
    }
    return render(request,"belt_reviewer/books.html", context)
def create(request):
    
    return render(request,"belt_reviewer/add.html")
def create_book(request):
    print(request.POST)
    book_id = Book.objects.create_book(request.POST)
    print(book_id)
    request.session['book_id']= book_id
    request.session['book_name']= request.POST['book_name']

    review = Review.objects.create_review(request.POST,book_id=request.session['book_id'],user_id=request.session['user_id'])
    print(review)
    return redirect("users:show")
def show(request):
    context={
        "book": Book.objects.get(id=request.session['book_id']),
        "reviews": Review.objects.get(book_id=request.session['book_id'])
        }
    
    
    

    return render(request,"belt_reviewer/show.html",context)
# def create_review(request,book_id,user_id):
#     print(request.POST)
#     print("want this one",request.session['book_id'])
    
#     print (review)
#     return redirect("users:show")
def logout(request):
    request.session.clear()
    return redirect("users:index")