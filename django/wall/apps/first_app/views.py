from django.shortcuts import render, HttpResponse,redirect
from .models import User,Message,Comment
from django.contrib import messages

# Create your views here.
def index(request):
    return render(request,"wall/index.html")
def process(request):
    print(request.POST)
    errors = User.objects.validate(request.POST)
    if errors:
        for error in errors:
            messages.error(request,error)
        return redirect('/')
    user_id= User.objects.create_user(request.POST)
    print("first one",user_id)
    request.session['user_id']= user_id
    request.session['first_name'] = request.POST['first_name']
    print("this one '*' *30",request.session['user_id'])
    return redirect('/')
def login(request):
    print("second one",request.POST)
    valid, result = User.objects.login(request.POST)
    if not valid:
        messages.error(request, result)
        return redirect('/')
    print(result)
    request.session['user_id'] = result
    return redirect('/wall')
def wall(request):
    
    context={
        "user" :  User.objects.get(id=request.session['user_id']),
        "messages": Message.objects.all(),
        "comments": Comment.objects.all()
        
    }
    print("this is context", context)
        
   
    return render(request,"wall/wall.html",context)

def message(request):
    print("views1",request.session['user_id'])
    print("views2",request.POST['description'])
    
    
    message_list= Message.objects.create_message(request.POST,request.session['user_id'])
    
    print("message list is", message_list)
    return redirect('/wall')
def comment(request,id):
    print(request.POST)
    print("-"*100,request.POST['message_id'])
    request.session['message_id'] = request.POST['message_id']
    # print("@"*100,request.session['message_id'])
    comment_list= Comment.objects.create_comment(request.POST,request.session['user_id'],request.POST['message_id'])
    # comment_list=Comment.objects.get(id=id)
    print("comment",comment_list)
    return redirect('/wall')
def logout(request):
    request.session.clear()
    return redirect('/')



    
    

    