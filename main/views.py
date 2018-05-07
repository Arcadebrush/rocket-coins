from django.shortcuts import render
from .models import Coins


# Create your views here.
def index(request):
    coins = Coins.objects.all()
    context = {
        "coins" : coins
    }
    return render(request,'main/index.html',context)

def detail(request, coin_name):
    return render(request,'main/detail.html', {'coin_name' : coin_name})