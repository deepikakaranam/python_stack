from django.shortcuts import render, HttpResponse, redirect
from time import gmtime, strftime

# Create your views here.
def index(request):
    return render(request,"session_words/index.html")
def add(request):
    if 'words' not in request.session:
        request.session['words'] = []
    word = request.POST['word']
    color = request.POST['color'] 
    size = request.POST['big_font']
    print(request.POST)
    print(size)
    if size is not "0":
        color += "big"


    time = strftime("%Y-%m-%d %H:%M %p", gmtime())
    new_word = {"word":word,"wclass":color,"time":time}
    request.session['words'].append(new_word)
    request.session.modified = True
    return redirect("/session_words")
def clear(request):
    del  request.session['words']
    return redirect("/session_words")