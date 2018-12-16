from django.shortcuts import render
from django.http import HttpResponse
from itertools import chain
from tablesapp.models import Nd3Plus_in_LaCl3_Nd3Plus_in_LaF3
from tablesapp.form1 import UserForm
from tablesapp.models import Energy_Level_4_Trivalent_Lanthanides_in_various_Media_in_cm_Inverse  as ELTL
from collections import OrderedDict as OD
# Create your views here.


#def Table1(request):
#	records = [('4 I 13/2', '4010', 3937, '4089', 4000,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#		 	   ('4 I 15/2', '0', 0, '0', 0,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#		       ('4 F 3/2', '11439', 1144, '11613', 11600,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#		       ('4 F 5/2','12466','12422','12610','12610', 'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('2 H 9/2','12618',0,'12707',12610,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('4 F 7/2','13437',13386,'13646',13586,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('4 S 3/2','13524',13386,'13646',13586,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('4 F 9/2','14722',14577,'14849',14792, 'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('2 H 11/2','15935',15847,'16050',16025,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('4 G 5/2','17135',17094,'13646',13586,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('2 G 7/2','0',0,'17551d',17391,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('2 K 13/2','0',0,'0',0,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('4 G 7/2','19020',18939,'19239',19230,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('4 G 9/2','19434',19379,'19700b',19607,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('2 K 15/2','0',20876,'0',0,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('2 G 9/2','21056',21141,'0',0,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('(2D2 2F)3/2','21129',21459,'0',0,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('4 G 11/2','21426',21459,'0',0,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('2 P 1/2','23214',23239,'23468',23474,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c'),
#	           ('2 D 5/2','23780',23781,'0',0,'Nd3Plus_in_LaCl3', 'Nd3Plus_in_LaF3','SLJ', 'v(cm-1)(liqid He)a', 'v(cm-1)b','v(cm-1)(liqid He)c')
#	          ]
#	for x in records:
#		a, b, c, d, e, f, g, h, i, j, k= x     
#		Nd3_LaCl3 = Nd3Plus_in_LaCl3_Nd3Plus_in_LaF3( SLJ=a, v_cm_Inverse_liqHe_a=b ,v_cm_Inverse_b1=c, v_cm_Inverse_liqHe_c=d,v_cm_Inverse_b2=e ,column_name1=f,column_name2= g,field_name1=h, field_name2=i,field_name3=j,field_name4=k)
#		Nd3_LaCl3.save()
#	return HttpResponse("hi")		
#	b = [('4 I 13/2', '4089', 4000),('4 I 15/2', '0', 0),('4 F 3/2', '11613', 11600),('4 F 5/2','12610','12610'),
#		('2 H 9/2','12707',12610),('4 F 7/2','13646',13586),('4 S 3/2','13646',13586),('4 F 9/2','14849',14792),
#		('2 H 11/2','16050',16025),('4 G 5/2','17328d',17391),('2 G 7/2','17551d',17391),('2 K 13/2','0',0),
#	     ('4 G 7/2','19239',19230),('4 G 9/2','19700b',19607),('2 K 15/2','0',0),('2 G 9/2','0',0),
#	     ('(2D2 2F)3/2','0',0),('4 G 11/2','0',0),('2 P 1/2','23468',23474),('2 D 5/2','0',0)]
#	for i in b:
#		c, d, e = i     
#		Nd3_LaCl3 =  Nd3Plus_in_LaF3(SLJ=c, v_cm_Inverse_liqHe_a=d ,v_cm_Inverse_b=e)
#		Nd3_LaCl3.save()

#def Table2(request):	
#	records = [ ('Pr3+ in Free ion a', '4864.6', '23.138', '488.11', '758.82',	'23.684', '-858.41', '727.78', '13'),
#				('Pr3+  in LaCl3 b', '4713.8', '21.89', '464', '742.68',  '22.899', '-676.97', '599.51', '13'),
#				('Pr3+  in LaF3  c', '4548.1', '21.659', '470.02', '743.24', '18.642', '-754.2', '1396.2', '13'),
#				('Pr3+  in aq',	'4548.2', '21.937', '466.73', '740.75', '21.255', '-799.94', '1342.9', '13'),
#				('Nd3+  in LaCl3 d', '4974.6', '23.734', '478.03', '879.42', '-0.8174', '-163.94', '0.0', '22'),
#				('Nd3+ in aq', '4739.3', '23.999', '485.96', '884.58', '0.5611', '-117.15', '1321.3', '32'),
#				('Pm3+  in aq', '4921.6', '24.522', '525.96', '1000.8', '10.991', '-244.88', '789.74', '22'),
#				('Sm3+  in  LaCl3 e', '5594.9', '27.365', '545.5', '1162.5', '16.192', '-540.36', '0.0','20'),
#				('Sm3+   in aq', '5496.9', '25.809', '556.4', '1157.3', '22.25', '-742.55', '796.64', '48'),
#				('Dy3+  in  LaCl3 f', '6411.2', '28.544', '603.84', '1923.4', '38.661', '-1184.7', '0.0', '16'),
#				('Dy3+  in  aq', '6119.6', '30.012', '610.14', '1932', '37.62', '-1139.1', '2395.3', '34'),
#				('Ho3+  in  LaCl3 k', '6520.2', '31.438', '620.76', '2138.3', '23.49', '-803.3', '887.56','23'),
#				('Ho3+  in aq', '6440.6', '30.22', '624.39', '2141.3', '23.635', '-807.2', '1278.4', '41'),
#				('Er3+ in Free ion b', '6855.3', '32.126',  '645.57',  '2369.4', '20.385', '-666.6', '0.0', '27'),
#				('Er3+  in  LaF3 i', '6884.4', '32.586', '649.64', '2380', '17.44', '-527.3', '0.0', '21'),
#				('Er3+  in  LaCl3 j', '6885.3', '32.272', '641.14', '2379.5', '17.431', '-655.28', '0.0', '20'),
#				('Er3+ in aq', '6769.9', '32.388', '646.62', '2380.7', '18.347', '-509.28', '649.71', '27'),
#				('Tm3+ in Ethyl sulfate k', '7150.8', '33.886', '675.73', '2628.1', '14.688', '-741.59', '0.0', '12'),
#				('Tm3+  in  aq', '7142.4', '33.795', '674.27', '2628.7', '14.677', '-631.79', '0.0', '12')
#				]
#
#	for x in records:
#		a, b, c, d, e, f, g, h, i = x 
#		fields = {'field_name1': 'Matrix','field_name2': 'E1', 'field_name3': 'E2', 'field_name4': 'E3', 
#				  'field_name5': 'I4f', 'field_name6': 'Alpha', 'field_name7': 'Beta', 'field_name8': 'Gama', 
#				  'field_name9': 'NoOf_levels_fit'}    
#		eltl = ELTL( Matrix=a, E1=b ,E2=c, E3=d, I4f=e , Alpha=f, Beta= g,Gama=h, NoOf_levels_fit=i)
#		eltl.save()
#	return HttpResponse("hi")

	
def OperationsOntable2(Reading):
	E1 		 = [i[0] for i in  ELTL.objects.values_list('E1')]
	E1_index = E1.index(min(E1, key = lambda x: abs(x-Reading)))
	e1  =  E1[::-1][len(E1)-E1_index : (len(E1)-E1_index)+5][::-1] + E1[E1_index : E1_index+5]
	#below	 = ELTL.objects.values_list('E1')[E1_index : (E1_index+5)]
	#above    = ELTL.objects.values_list('E1')[::-1][ len(E1)- E1_index : (len(E1)-E1_index)+5 ][::-1]	

	Matrix = [ i for i in ELTL.objects.values_list('Matrix')]
	matrix = Matrix[::-1][ len(E1)- E1_index : (len(E1)-E1_index)+5 ][::-1] + Matrix[E1_index : (E1_index+5)]

	E2	   	 =  [i[0] for i in  ELTL.objects.values_list('E2')]
	E2_index = 	E2.index(min(E2, key =lambda x:abs(x-Reading)))
	e2 		 = 	E2[::-1][len(E2)-E2_index : (len(E2)-E2_index)+5][::-1] + E2[E2_index : E2_index+5] #above + below
	#below	=	ELTL.objects.only('E2')[E2_index : (E2_index+5)]
	#above    = ELTL.objects.only('E2')[::-1][ len(E2)- E2_index : (len(E2)-E2_index)+5 ][::-1]
	
	E3 	     = [i[0] for i in  ELTL.objects.values_list('E3')]
	E3_index = E3.index(min(E3, key = lambda x:abs(x-Reading)))
	e3       = E3[::-1][len(E3)-E3_index : (len(E3)-E3_index)+5][::-1] + E3[E3_index : E3_index+5] #above + below

	I4f 	  = [i[0] for i in  ELTL.objects.values_list('I4f')]
	I4f_index = I4f.index(min(I4f, key = lambda x:abs(x-Reading)))
	i4f    	  = I4f[::-1][len(I4f)-I4f_index : (len(I4f)-I4f_index)+5][::-1] + I4f[I4f_index : I4f_index+5] #above + below
	
	Alpha 	    = [i[0] for i in  ELTL.objects.values_list('Alpha')]
	Alpha_index = Alpha.index(min(Alpha, key = lambda x:abs(x-Reading)))
	alpha       = Alpha[::-1][len(Alpha)-Alpha_index : (len(Alpha)-Alpha_index)+5][::-1] + Alpha[Alpha_index : Alpha_index+5] #above + below

	Beta 	   = [i[0] for i in  ELTL.objects.values_list('Beta')]
	Beta_index = Beta.index(min(Beta, key = lambda x:abs(x-Reading)))
	beta       = Beta[::-1][len(Beta)-Beta_index : (len(Beta)-Beta_index)+5][::-1] + Beta[Beta_index : Beta_index+5] #above + below 

	Gama 	   =  [i[0] for i in  ELTL.objects.values_list('Gama')]
	Gama_index =  Gama.index(min(Gama, key = lambda x:abs(x-Reading)))
	gama       =  Gama[::-1][len(Gama)-Gama_index : (len(Gama)-Gama_index)+5][::-1] + Gama[Gama_index : Gama_index+5] #above + below 
	
	Levels_Fit 	   =  [i[0] for i in  ELTL.objects.values_list('NoOf_levels_fit')]
	Levels_Fit_index =  Levels_Fit.index(min(Levels_Fit, key = lambda x:abs(x-Reading)))
	levels_fit       =  Levels_Fit[::-1][len(Levels_Fit)-Levels_Fit_index : (len(Levels_Fit)-Levels_Fit_index)+5][::-1] + Levels_Fit[Levels_Fit_index : Levels_Fit_index+5] #above + below

	recors_list = zip(matrix, e1,e2,e3,i4f,alpha,beta,gama,levels_fit)
	attributes = ELTL._meta.get_fields()[1:]
	print(type(attributes))
	return ['display1.html', recors_list, attributes ]

def OperationsOntable1(Reading):
	Nd = Nd3Plus_in_LaCl3_Nd3Plus_in_LaF3.objects.values_list('v_cm_Inverse_liqHe_a')
	
	nd = [int(z[0]) for z in  Nd ]
	a = min(nd, key=lambda x:abs(x-Reading))
	b = nd.index(a) #l = len(nd)
	below = Nd3Plus_in_LaCl3_Nd3Plus_in_LaF3.objects.all()[b:b+5]
	above =Nd3Plus_in_LaCl3_Nd3Plus_in_LaF3.objects.all()[::-1][ (len(nd)-b) : (len(nd)-b)+5][::-1] 
	final = list(chain(above, below))
	attributes = Nd3Plus_in_LaCl3_Nd3Plus_in_LaF3._meta.get_fields()[1:]
	return ['dispaly.html' ,final, attributes]
	#render(request,'dispaly.html',{"final": final })
	#return HttpResponse(nam)

d = {'Nd3+ in LaCl3 & in LaF3': OperationsOntable1, 'Energy_Level_4_Trivalent_Lanthanides': OperationsOntable2}	

def MyForm(request):

	if  request.method == 'POST':
		form = UserForm(request.POST)
		if form.is_valid():
			Reading= form.cleaned_data["reading"]
			TableName= form.cleaned_data["table_name"]
			#a = str(TableName)
			for ke in d.keys():
				if ke == str(TableName):
					final = d[ke](int(Reading))
					break
			if str(TableName) == 'Nd3+ in LaCl3 & in LaF3' :
				return render(request, final[0],context = {'form': form, 'final': final[1]})
			else:			
				return render(request, final[0], context={'form': form, 'records':final[1], 'Attributes':final[2]} )
				
	else:	
		form = UserForm()
		return render(request, 'dispaly.html', {'form': form })	
		
		