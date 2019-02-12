from django.shortcuts import render, HttpResponse, redirect
from django.utils.crypto import get_random_string
def random_word(n):
    random_word=get_random_string(length=n)
    return random_word
# Create your views here.
def index(request):
    
    print('*'*10)
    request.session['word'] = random_word(14)
    request.session['tries'] += 1
    #print(request.session['tries'])
            
    return render(request,'main/index.html')

def reset(request):
    request.session['tries'] = 0
    return redirect('/')