from django import forms
from tablesapp import *
tables = [('Nd3+ in LaCl3 & in LaF3','Nd3+ in LaCl3 & in LaF3'),('Energy_Level_4_Trivalent_Lanthanides','Energy_Level_4_Trivalent_Lanthanides'),
		   	
		 ]

class UserForm(forms.Form):
	reading = forms.CharField(max_length=100)
	table_name = forms.CharField(label='Enter Table Name:',
				  widget=forms.Select(choices=tables))