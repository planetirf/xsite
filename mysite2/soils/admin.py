from django.contrib import admin

# Register your models here.
from .forms import SubOrdersForm
from .models import  SoilOrders, SubOrders, GreatGroups

# class SoilAdmin(admin.ModelAdmin):
#     fields = ['soil','soil_order','great_group', 'sub_group', 'family','series','phase']


class SoilOrderAdmin(admin.ModelAdmin):
    fields = ['order','order_text','area']

class SubOrdersAdmin(admin.ModelAdmin):
    # form = SubOrdersForm
     fields  = ['suborder','suborder_text']
     exclude = ['order', 'order_text']

class GreatGroupsAdmin(admin.ModelAdmin):
    fields = ['greatgroup','greatgroup_text']
#
#
# # admin.site.register(Soil)
admin.site.register(SoilOrders)
admin.site.register(SubOrders)
admin.site.register(GreatGroups)
