from django.shortcuts import render, get_object_or_404

# Create your views here.
from django.http import HttpResponse
from .models import SoilOrders, SubOrders, GreatGroups

from django.views.generic import ListView


def index(request):
    orders_list = SoilOrders.objects.order_by('order')
    context = {'orders_list': orders_list}
    return render(request, 'soils/index.html', context)


def suborder_view(request):
    suborders_list = SubOrders.objects.order_by('order')
    context = {'suborders_list': suborders_list}
    return render(request, 'soils/suborder_view.html', context)

def greatgroup_view(request):
    greatgroups_list = GreatGroups.objects.order_by('suborder')
    context = {'greatgroups_list': greatgroups_list}
    return render(request, 'soils/greatgroup_view.html', context)


def soil_view(request):
    return render(request, 'soils/soil_view.html', {})


def detail(request,):
    orders_list = SoilOrders.objects.order_by('order')
    suborders_list = SubOrders.objects.order_by('order')
    greatgroups_list = GreatGroups.objects.order_by('suborder')
    soil_type = GreatGroups.objects.all()
    b = GreatGroups.objects.filter(suborder_id=1)
    print(b)
    context = {'soil_type': soil_type,'orders_list': orders_list,'greatgroups_list': greatgroups_list,'suborders_list': suborders_list,'b':b}
    return render(request, 'soils/detail.html', context)
