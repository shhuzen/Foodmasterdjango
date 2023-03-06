from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.views.decorators.http import require_POST

from .forms import CartAddProductForm
from .models import *
from django.shortcuts import render, redirect
from cart.cart import Cart
# Create your views here.

class SignupView(generic.CreateView):
    form_class = UserCreationForm
    template_name ='account/signup.html'
    success_url = reverse_lazy('login')


def main_page(request):
    if request.user.is_anonymous:
        return redirect("/login")
    cart = Cart(request)
    user = request.user
    if user.is_superuser:
        total_amt = 0

        for id, item in request.session['cart'].items():
            if request.session['cart'].items() == "":
                total_amt = 0
            else:
                total_amt += int(item['quantity']) * float(item['price'])
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

@require_POST
async def CartAdd(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Items, id=id)
    form = CartAddProductForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        cart.add(product=product, quantity=cd['quantity'],
                                  update_quantity=cd['update'])


def sda(request):
    total_amt = 0

    for id, item in request.session['cart'].items():
        if request.session['cart'].items() == "":
            total_amt = 0
        else:
            total_amt += int(item['quantity']) * float(item['price'])
    return render(request, 'orders.html', {'total': total_amt})
