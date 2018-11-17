from django.shortcuts import render
from django.contrib.auth import logout
from .forms import CommodityForm
# Create your views here.
from django.http import HttpResponse
from .models import Commodity


def commodityCreateView(request):
    form = CommodityForm(request.POST or None)
    if form.is_valid():
        form.save(commit=True)

    context = {
        'form' : form
    }
    return render(request,'trade/add_commodity.html',context)


def homePageView(request):
    return render(request,'trade/trader.html')


def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')
