from django.shortcuts import render, HttpResponse, redirect

# Create your views here.
def index(request):
    # request.session['total_quantity'] = 0
    # request.session['total_purchase'] = 0
    
    return render(request,"amadon/index.html")
def process(request):
    print(request.POST)
    request.session['quantity'] = request.POST['quantity']
    print(request.session['quantity'])
    print(request.POST['product_id'])
    request.session['product_id'] = request.POST['product_id']
    print(request.session['product_id'])
    request.session['total_price'] = int(request.session['quantity']) * float(request.session['product_id']) 
    try:
        request.session['total_quantity']
    except KeyError:
        request.session['total_quantity']=0

    try:
        request.session['total_purchase']
    except KeyError:
        request.session['total_purchase']=0
    request.session['total_quantity'] += int(request.session['quantity'])
    request.session['total_purchase'] += float(request.session['total_price'])

    print (request.session['total_quantity'])
    print(request.session['total_purchase'])
       
    return redirect('/')

def checkout(request):
    return render(request,"amadon/checkout.html")

