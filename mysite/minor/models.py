from __future__ import unicode_literals

from django.db import models

# Create your models here.
class brand(models.Model):
	
	brand_text=models.CharField(max_length=50)
	#brand_id
	

class bike(models.Model):
	
	bike_text=models.CharField(max_length=100)
	bike_brand=models.ForeignKey(brand)
	bike_engine=models.IntegerField(null=True)

class station(models.Model):
	name=models.CharField(max_length=200)
	address=models.CharField(max_length=500)
	pin=models.IntegerField(null=True)
	lat=models.FloatField(null=True)
	lon=models.FloatField(null=True)


class workshop(models.Model):
	name=models.CharField(max_length=200)
	address=models.CharField(max_length=500)
	pin=models.IntegerField(null=True)
	lat=models.FloatField(null=True)
	lon=models.FloatField(null=True)
		
class mechanic(models.Model):
	usrname=models.CharField(max_length=50, unique= True)
	password=models.CharField(max_length=50)
	name=models.CharField(max_length=200)
	address=models.CharField(max_length=500)
	reg_type=models.CharField(max_length=50)
	reg_id=models.CharField(max_length=500)
	mlat=models.FloatField(null=True)
	mlon=models.FloatField(null=True)
	phone=models.CharField(max_length=15)
	email=models.CharField(max_length=50,null=True)
	shop=models.CharField(max_length=50)
	
	#self.photo = models.ImageField(upload_to='mechanic/'self.username)
	#def imgdef(self):
	#	self.photo = models.ImageField(upload_to='mechanic/'+self.usrname)


class rider(models.Model):
	
	usrname=models.CharField(max_length=50, unique= True)
	password=models.CharField(max_length=50)
	f_name=models.CharField(max_length=200)
	l_name=models.CharField(max_length=200)
	home_lat=models.FloatField(null=True)
	home_lon=models.FloatField(null=True)
	job=models.BooleanField(default=False)
	#bike=models.ForeignKey(bike)
	

#class find(models.Model):
#	user_id =models.IntegerField(null=True)
#	m_id =models.IntegerField(null=True)
#	date = models.DateTimeField()

class trnx(models.Model):
	time =models.DateTimeField()
	usrid=models.IntegerField(null=True)
	mechid=models.IntegerField(null=True)
	damagetext=models.CharField(max_length=500)
	ack=models.BooleanField(default=False)
	budget=models.IntegerField(default=0)


class price(models.Model):
	item=models.CharField(max_length=50)
	price=models.IntegerField()

class avail(models.Model):
	
	mechid=models.IntegerField()
	isavail=models.BooleanField(default=False)
	last=models.DateTimeField()
	mlat=models.FloatField(null=True)
	mlon=models.FloatField(null=True)


	



#	def __str__(self):
#
#        return ' '.join([
#            self.first_name,
#            self.last_name,
#        ])


