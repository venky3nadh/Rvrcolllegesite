from django.shortcuts import render
from django.http import HttpResponse
from .myform import Myform
# Create your views here.


def operation(request):
	if request.method=='POST':
		form = Myform(request.POST)
	else:
		form = Myform()	
	return render(request, 'FirstForm.html',context = {'form': form})