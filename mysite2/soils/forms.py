from django import forms
from .models import SoilOrders, SubOrders, GreatGroups

class SoilOrdersForm(forms.ModelForm):
    class Meta:
        model = SoilOrders
        fields = ['order', 'order_text']

class SubOrdersForm(forms.ModelForm):
    class Meta:
        model = SubOrders
        fields = ['order','suborder',]

class GreatGroupsForm(forms.ModelForm):
    class Meta:
        model = GreatGroups
        fields = ['greatgroup',]
        # exclude = []
