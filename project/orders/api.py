import json

from django.http import JsonResponse

from orders.models import *


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
        temp[5] = f'''<button onclick = "if(confirm('Вы уверены?')){{del({i.id})}}" class="btn btn-danger"><i class="bi bi-x"></i></button>
<button onclick = "{{addcarto({i.id})}}" class="btn btn-success"><i class="bi bi-plus-square"></i></button>
<button  onclick ="{{plus({i.id})}}" class="btn btn-danger"><i class="bi bi-plus-lg"></i></button>
<button  onclick ="{{minus({i.id})}}" class="btn btn-danger"><i class="bi bi-dash"></i></button>

'''
        table.append(temp)
    response = {
        "data":table
    }
    return JsonResponse(response)

def api_get_orders(request):
    all = Orders.objects.all()
    table = []
    for i in all:
        temp = {}
        temp[0] = i.price
        temp[2] = i.desc
        temp[3] = f'''<button onclick = "if(confirm('Вы уверены?')){{del({i.id})}}" class="btn btn-danger"><i class="bi bi-x"></i></button>
<button onclick = "if(confirm('Вы уверены?')){{addcarto({i.id})}}" class="btn btn-danger"><i class="bi bi-x"></i></button>
<a href="{{plus({i.id})}}"">Increament</a>
<a href="{{minus({i.id})}}"">Decrement</a>
'''
        table.append(temp)
    response = {
        "data":table
    }
    return JsonResponse(response)

