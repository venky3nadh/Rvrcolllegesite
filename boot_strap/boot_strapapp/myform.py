from django import forms
#from django.forms.formsets import BaseFormSet
from boot_strapapp import *

class Myform(forms.Form):
	name = forms.CharField(max_length=100, widget=forms.TextInput(attrs={'size':10}))
