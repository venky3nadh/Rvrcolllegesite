from __future__ import unicode_literals

from django.db import models

# Create your models here.
class Nd3Plus_in_LaCl3_Nd3Plus_in_LaF3(models.Model):
	column_name1 = models.CharField(max_length=500)
	column_name2 = models.CharField(max_length=500)
	SLJ = models.CharField(max_length=500)
	v_cm_Inverse_liqHe_a = models.CharField(max_length=500)
	v_cm_Inverse_b1 = models.IntegerField()
	v_cm_Inverse_liqHe_c = models.CharField(max_length=500)
	v_cm_Inverse_b2 = models.IntegerField()
	field_name1 = models.CharField(max_length=500) #'SLJ'
	field_name2 = models.CharField(max_length=500) #'v_cm_Inverse_liqHe_a'
	field_name3 = models.CharField(max_length=500) #'v_cm_Inverse_b'
	field_name4 = models.CharField(max_length=500) #'v_cm_Inverse_liqHe_c'

class Energy_Level_4_Trivalent_Lanthanides_in_various_Media_in_cm_Inverse(models.Model):
	Matrix =  models.CharField(max_length=500)
	E1 	=  models.FloatField()
	E2 	=  models.FloatField()
	E3 	=  models.FloatField()
	I4f =  models.FloatField()
	Alpha = models.FloatField()
	Beta  = models.FloatField()
	Gama  = models.FloatField()
	NoOf_levels_fit = models.IntegerField()
