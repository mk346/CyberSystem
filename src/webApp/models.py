from django.db import models

# Create your models here.
class details(models.Model):
	fname = models.CharField(max_length=100 )
	lname = models.CharField(max_length=100)
	mobile = models.IntegerField()
	email = models.EmailField()
	IdNumber = models.IntegerField()
	Pin = models.CharField(max_length=100)
	Choice =(
		("Individual Return", "Individual Return"),
		("Company Tax Return", "Company Tax Return"),
		("VAT Return Filing", "VAT Return Filing"),
		("PAYE Return Filing", "PAYE Return Filing"),
	)
	service = models.CharField(max_length=50, choices=Choice)



	def __str__(self):
		return self.fname

class Register(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	mobile = models.IntegerField()
	email =models.EmailField()
	idNumber = models.IntegerField()
	PostalCode = models.IntegerField()
	PostalAddress = models.IntegerField()
	county = models.CharField(max_length=100)
	town = models.CharField(max_length=100)
	district = models.CharField(max_length=100)
	dob =  models.CharField(max_length=50)

	def __str__(self):
		return self.firstName

class Apply(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	mobile = models.IntegerField()
	email = models.EmailField()
	Choice =(
		("Renewal Of Driving Licence", "Renew Driving Licence"),
		("Temporary Permit Application", "Temporary Permit"),
		("PassPort Application", "PassPort Application"),
	)
	service = models.CharField(max_length=50,choices=Choice)


	def __str__(self):
		return self.firstName

class Rest(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	mobile = models.IntegerField()
	email = models.EmailField()
	subject = models.CharField(max_length=500)
	message = models.CharField(max_length=1000)
	Choice =(
		("Business Cards Design", "Business Cards Design"),
		("Invoice Cards Design", "Invoice Cards Design"),
		("Delivery Cards Design", "Delivery Cards Design"),
		("Wedding Cards Design", "Wedding Cards Design"),
		("Funeral Cards Design", "Funeral Cards Design"),
		("Banners Design", "Banners Design"),
	)
	service = models.CharField(max_length=50,choices=Choice)

	def __str__(self):
		return self.firstName


class ChangeDet(models.Model):
	firstName = models.CharField(max_length=100)
	lastName = models.CharField(max_length=100)
	mobile = models.IntegerField()
	Cemail = models.EmailField()
	Nemail = models.EmailField()




	



 















