from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from cart.cart import Cart
# Create your views here.

def main_page(request):
    total_amt = 0
    for id, item in request.session['cart'].items():
        total_amt += int(item['quantity']) * float(item['price'])
    user = request.user
    if user.is_superuser:
        if request.method == "POST":
            name = request.POST.get("name")
            allquantity = request.POST.get("allquantity")
            desc = request.POST.get("desc")
            price = request.POST.get("price")
            if request.FILES:
                info = request.FILES["file_more"]
            requr = Items(name=name, amount=allquantity, desc=desc, price=price,image=info)
            requr.save()
    return render(request,'index.html',{'total': total_amt})

def cart(request):
    return render(request,'cart.html')

def dell_items(request,id):
    t = get_object_or_404(Items,id=id)
    t.delete()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))

def cart_add(request, id):
    cart = Cart(request)
    product = Items.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


def item_clear(request, id):
    cart = Cart(request)
    product = Items.objects.get(id=id)
    cart.remove(product)
    return redirect("/")


def item_increment(request, id):
    cart = Cart(request)
    product = Items.objects.get(id=id)
    cart.add(product=product)
    return redirect("/")


def item_decrement(request, id):
    cart = Cart(request)
    product = Items.objects.get(id=id)
    cart.decrement(product=product)
    return redirect("/")


def cart_clear(request):
    cart = Cart(request)
    cart.clear()
    return redirect("/")


def cart_detail(request):
    total_amt = 0
    for id, item in request.session['cart'].items():
     total_amt += int(item['quantity']) * float(item['price'])
    return render(request, 'cart.html', {'total': total_amt})
