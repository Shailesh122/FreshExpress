from typing import AbstractSet
from django.db.models import fields
from django.forms import ModelForm, widgets
from store.models import Store, StoreItem
from django import forms


class StoreForm(ModelForm):
    class Meta:
        model = Store
        fields = '__all__'
        exclude = ['merchant', 'lat', 'long',
                   'rating', 'shop_status', 'total_orders']


class StatusForm(forms.Form):
    productid = forms.CharField()
    status = forms.BooleanField(required=False)


class StoreItemForm(ModelForm):
    class Meta:
        model = StoreItem
        fields = "__all__"
        exclude = ['status']
        widgets = {'shop': forms.HiddenInput()}


class RemoveItemForm(forms.Form):
    storeitemid = forms.CharField()


class OrderItemForm(forms.Form):
    orderitems = forms.CharField(required=False)
    orderid = forms.CharField(required=False)

class DeliveredForm(forms.Form):
    order = forms.CharField()