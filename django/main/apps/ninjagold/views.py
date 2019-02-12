from django.shortcuts import render, HttpResponse, redirect
import random

# Create your views here.
def index(request):
    context = {
        "message": "message"
    }
    return render(request,"ninjagold/index.html",context)

def process(request):
    location=request.POST["building"]
    building_map = {
        'farm':random.randint(10,21),
        'cave':random.randint(5,11),
        'house':random.randint(2,6),
        'casino':random.randint(-50,51)
    }
    print (location)
    print(building_map[location])
    cur_gold=building_map[location]

    if 'gold' in request.session:
        request.session['gold']+= cur_gold
    else:
        request.session['gold']=cur_gold
    

    if cur_gold>0:
        message={
            'class':'green',
            'content':"You won {} golds at the {}.".format(cur_gold,location)
        }
    else:
        message={
            'class':'red',
            'content': "You lost{} golds at the {}.".format(cur_gold,location)
        }
    if not 'activities' in request.session:
        request.session['activities']=[message]
    else:
        request.session['activities'].append(message)
        request.session.modified = True
    return redirect('/')

def clear(request):
    del request.session['activities']
    return redirect('/')    