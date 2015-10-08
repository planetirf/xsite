from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
from .models import SoilOrders, SubOrders, GreatGroups


def index(request):

    orders_list = SoilOrders.objects.order_by('order')
    context = {'orders_list': orders_list}
    return render(request, 'soils/index.html', context)


def suborder_view(request):
    suborders_list = SubOrders.objects.order_by('suborder')
    context = {'suborders_list': suborders_list}
    return render(request, 'soils/suborder_view.html', context)

def greatgroup_view(request):
    greatgroups_list = GreatGroups.objects.order_by('suborder')
    context = {'greatgroups_list': greatgroups_list}
    return render(request, 'soils/greatgroup_view.html', context)
