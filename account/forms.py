from django import forms
from django.forms import ModelForm
from django.forms.formsets import formset_factory

from .models import *



class ProjectFrom(ModelForm):
    class Meta:
        model = Project
        fields = "__all__"
        exclude = ('created_by','update_by','created','update','slug')

class BranchFrom(ModelForm):
    class Meta:
        model = Branch
        fields = "__all__"
        exclude = ('created_by','update_by','created','update','slug')


class AccountFrom(ModelForm):
    class Meta:
        model = Account
        fields = "__all__"
       # exclude = ('created_by','update_by','created','update','slug','branch')


class CompanyFrom(ModelForm):
    class Meta:
        model = Company
        fields = "__all__"
        exclude = ('created_by','update_by','created','update','slug','branch')
class OrderForm(ModelForm):
    class Meta:
        model = Order
        fields = ('note','creditor','debitor','finance')
        #exclude = ('created_by','update_by','created','update','type','branch','success')

class OrderItemForm(ModelForm):
    class Meta:
        model = OrderItem
        fields = ('product','unit','quantity','price','note')
        widgets = {
			'product': forms.TextInput(attrs={'class': 'formset-field'}),
			'unit': forms.TextInput(attrs={'class': 'formset-field'}),
			'quantity': forms.TextInput(attrs={'class': 'formset-field'}),
			'price': forms.TextInput(attrs={'class': 'formset-field'}),
			'note': forms.TextInput(attrs={'class': 'formset-field'})
		}
        #exclude = ('created_by','update_by','created','update','type','branch','success')


OrderItemFormset = formset_factory(OrderItemForm,extra=1)
        
