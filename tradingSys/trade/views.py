from django.shortcuts import render

from .forms import CommodityForm
# Create your views here.
from django.http import HttpResponse


def commodityCreateView(request):
    form = CommodityForm(request.POST)
    if form.is_valid():
        form.save(commit=True)

    context = {
        'form' : form
    }
    return render(request,'trade/add_commodity.html',context)


def homePageView(request):
    form = CommodityForm(request.POST or None)
    if(form.is_valid()):
        form.save()

    context = {
        'form' : form
    }
    return render(request,'trade/add_commodity.html',context)
