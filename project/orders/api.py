
import json
from django.template import Library
import re

from django.http import JsonResponse, HttpResponseRedirect
from django.shortcuts import get_object_or_404
from datetime import datetime

from orders.models import Cartloyal

register = Library()

from orders.models import *

from orders.models import Items

from orders.models import Orders

from project.settings import MEDIA_URL



def order_status(request,id):
    req = get_object_or_404(Orders,id=id)
    if req.status == "Оплачен":
        req.status = "Не оплачен"
        req.save()
    elif req.status == "Не оплачен":
        req.status = "Оплачен"
        req.save()
        return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
@register.simple_tag
def media_url():
    return MEDIA_URL
def add_order(request):
    if request.method == "POST":
        total_amt = 0
        fiveprocent = 0
        if request.POST.get("check_file") == "":
            check_info = ""
        else:
            check_info = request.FILES["check_file"]
        if request.POST.get("cartloyal") == "":
            cartloyal = ""
        else:
            cartloyal = request.POST.get("cartloyal")
        for id, item in request.session['cart'].items():
            if request.POST.get("cartloyal") == "":
                total_amt += int(item['quantity']) * float(item['price'])
                fiveprocent = total_amt
                mesto = request.POST.get("mesto")
            else:
                total_amt += int(item['quantity']) * float(item['price']) * 0.05
                fiveprocent += int(item['quantity']) * float(item['price']) - total_amt
                mesto = request.POST.get("mesto")
        requr = Orders.objects.create(mesto=mesto, date_creation=datetime.today(), price=float(fiveprocent),
                                              date_last_update=datetime.today(), check_info=check_info)


        for id, item in request.session['cart'].items():
            productid = int(item['product_id'])
            requr.products.add(productid)
            if cartloyal != "":
                d = Cartloyal.objects.get_or_create(cartloyalid=cartloyal,procent=5)
                objectphone = get_object_or_404(Cartloyal, cartloyalid=cartloyal)
                requr.cartloyal.add(objectphone)


    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def edit_product(request):
    req = get_object_or_404(Items,id=request.POST.get("id"))

    req.name = request.POST.get("nameedit")
    req.price = request.POST.get("priceedit")
    req.amount = request.POST.get("allquantityedit")
    req.desc = request.POST.get("descedit")
    if request.POST.get("file_moreedit") == "":
        req.image == req.image
    else:
        req.image = request.FILES["file_moreedit"]

    req.save()
    return HttpResponseRedirect(request.META.get('HTTP_REFERER'))
def api_get_info(request):
    all = Items.objects.all()
    table = []
    for i in all:
        temp = {}
        temp[0] = i.amount
        temp[1] = i.name
        temp[2] = i.price
        temp[3] = i.desc
        temp[4] = str(i.image)
        if i.amount >= 1:
            temp[5] = f'''<div style="display:flex; width:100%; height:100%;"><button  style="    height: 10%;
    margin-top: 10px" onclick ="{{plus({i.id})}}" class="plusid btn btn-success"><i class="bi bi-plus-lg"></i></button>
<button style="    height: 10%;
    margin-top: 10px"   onclick ="{{minus({i.id})}}" class="btn btn-danger"><i class="bi bi-dash"></i></button>

        
'''
            temp[6] = f'''        <button onclick = "if(confirm('Вы уверены?')){{del({i.id})}}" class="btn btn-danger">Удалить </button>
                    <button data-bs-toggle="modal" onclick="edit({i.id})"  data-bs-target="#ModalEdit" class="btn btn-warning">Изменить</button>
            '''
        else:
            temp[5] = f'''<div style="display:flex; width:100%; height:100%;"><button disabled  style="    height: 10%;
                margin-top: 10px" onclick ="{{plus({i.id})}}" id="plus" class="plusid plus btn btn-success"><i class="bi bi-plus-lg"></i></button>
            <button disabled style="    height: 10%;
                margin-top: 10px"   onclick ="{{minus({i.id})}}" id="minus" class="minus btn btn-danger"><i class="bi bi-dash"></i></button>


            '''

            temp[6] = f'''        <button onclick = "if(confirm('Вы уверены?')){{del({i.id})}}" class="btn btn-danger">Удалить </button>
        <button data-bs-toggle="modal" onclick="edit({i.id})"  data-bs-target="#ModalEdit" class="btn btn-warning">Изменить</button>
'''
        table.append(temp)
    response = {
        "data":table
    }
    return JsonResponse(response)
def api_get_more(request,id):
    t = get_object_or_404(Items,id=id)
    response = {
        "amount":t.amount,
        "name":t.name,
        "desc":t.desc,
        "file_more":str(t.image),
        "price":t.price,
        "id":t.id,
    }
    return JsonResponse(response)

def api_get_orders(request):
    all = Orders.objects.all()
    table = []
    for i in all:
        d = str(i.products.all())
        regex = r"[a-zA-Z0-9+_@.-]*\>"
        z = re.findall(regex,d)
        regexsecond = r"[a-zA-Z0-9+_-]+"
        g = re.findall(regexsecond, str(z))
        print(g)
        temp = {}
        temp[0] = i.mesto
        temp[1] = f'''{i.price} Рублей'''

        temp[2] = str(g)
        temp[3] = i.date_creation
        temp[4] = i.date_last_update
        if i.status == "Не оплачен":
            temp[5] = i.status
            temp[6] = f'''
<div style="display:flex; width:100%; height:100%;"><button  style="    height: 10%;
    margin-top: 10px" onclick ="{{orderchange({i.id})}}" class="btn btn-warning"><i class="bi bi-credit-card"></i>
</button>
<button style="    height: 10%;
'''
            temp[7] = "Не оплачено"
            temp[8] = f'''-'''
            temp[9] = f'''-'''
        else:
            temp[5] = i.status
            temp[6] = f'''
        <div disabled style="display:flex; width:100%; height:100%;"><button  style="    height: 10%;
            margin-top: 10px" onclick ="{{orderchange({i.id})}}" class="btn btn-success"><i class="bi bi-credit-card"></i>
</button>
        <button style="    height: 10%;
        '''
            temp[7] = datetime.today()
            if i.check_info == "":
                temp[8] = f'''-'''
                temp[9] = f'''-'''
            else:
                temp[8] = f'''<a href="items/{str(i.check_info)}">ЧЕК</a>'''
                cartloyalati = i.cartloyal.all()
                for d in cartloyalati:
                    temp[9] = d.cartloyalid







        table.append(temp)
    response = {
        "data":table
    }
    return JsonResponse(response)
