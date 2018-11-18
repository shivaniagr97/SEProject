from django.shortcuts import render
from django.contrib.auth import logout
from django.contrib.auth.models import User
from django.urls import reverse
from .forms import CommodityForm
# Create your views here.
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from .models import Commodity
# from django.core.urlresolvers import reverse_lazy
from django.views.generic import (
    UpdateView,
    ListView,
    DeleteView
)

def commodityCreateView(request):
    form = CommodityForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.exporterName = request.user
        obj.save()
        return HttpResponseRedirect(reverse('mycommodities-view'))
    context = {
        'form' : form
    }
    return render(request,'trade/add_commodity.html',context)


def homePageView(request):
    return render(request,'trade/trader.html')


def logout_view(request):
    logout(request)
    return render(request, 'logged_out.html')

def myCommoditiesView(request):
    queryset = Commodity.objects.filter(exporterName = request.user)
    context = {
        'object_list' : queryset
    }
    return render(request, "trade/commodity_list.html", context)
