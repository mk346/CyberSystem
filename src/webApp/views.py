from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect
from .models import details,ChangeDet,Apply,Rest,Register
from .forms import myForm,Change,Application,Other,Contact,Registration
from django.core.mail import send_mail
from django.conf import settings
from django.template.loader import render_to_string

# Create your views here.

def home(request):
	return render(request,'webApp/index.html',{})

def form(request):
	form = myForm()
	if request.method == 'POST':
		form = myForm(request.POST)
		if form.is_valid():
			form.save()
			Fname = form.cleaned_data['fname']
			Lname = form.cleaned_data['lname']
			Mobile = form.cleaned_data['mobile']
			Email = form.cleaned_data['email']
			idNumber = form.cleaned_data['IdNumber']
			pin = form.cleaned_data['Pin']
			service = form.cleaned_data['service']

			data = {
				'Name':Fname + " " + Lname ,
				'Mobile':Mobile ,
				'Email':Email ,
				'idNumber':idNumber ,
				'pin':pin ,
				'service':service,

			}

			message = '''
			Full Name: {}
			Phone Number: {}
			ID Number: {}
			KRA Pin: {}
			Sender Email: {}
			'''.format(data['Name'],data['Mobile'],data['idNumber'],data['pin'],data['Email'])

			send_mail(data['service'],message,'',['kinyuacaleb554@gmail.com'])
			return render(request,'webApp/form.html',{'Fname':Fname,'service':service})

	else:
		return render(request,'webApp/form.html',{'form':form})	
	


def registration(request):
	form = Registration()
	if request.method == 'POST':
		form = Registration(request.POST)
		if form.is_valid():
			form.save()
			fName = form.cleaned_data['firstName']
			lName = form.cleaned_data['lastName']
			mobile = form.cleaned_data['mobile']
			email = form.cleaned_data['email']
			idNo = form.cleaned_data['idNumber']
			PCode = form.cleaned_data['PostalCode']
			PAddress = form.cleaned_data['PostalAddress']
			county = form.cleaned_data['county']
			town = form.cleaned_data['town']
			district = form.cleaned_data['district']
			dob = form.cleaned_data['dob']
			service = 'KRA Pin Registration'

			data = {
				'Name':fName+ " "+lName,
				'mobile':mobile,
				'email':email,
				'idNo':idNo,
				'PCode':PCode,
				'PAddress':PAddress,
				'county':county,
				'town':town,
				'district':district,
				'dob':dob,
				'service':service,
            }
			
			message ='''
			Full Name: {}
			Phone Number: {}
			ID Number: {}
			Postal Code: {}
			Postal Address: {}
			County: {}
			Town: {}
			District: {}
			Date of Birth:{}
			Sender Email: {}
			'''.format(data['Name'],data['mobile'],data['idNo'],data['PCode'],data['PAddress'],data['county'],data['town'],data['district'],data['dob'],data['email'])

			send_mail(data['service'],message,'',['kinyuacaleb554@gmail.com'])
			return render(request,'webApp/registration.html',{'fName':fName,'service':service})
	else:
		return render(request,'webApp/registration.html',{'form':form})
			
	

def change(request):
	form = Change()
	if request.method == 'POST':
		form = Change(request.POST)
		if form.is_valid():
			form.save()
			Fname = form.cleaned_data['firstName']
			Lname = form.cleaned_data['lastName']
			mobile = form.cleaned_data['mobile']
			Cemail = form.cleaned_data['Cemail']
			nEmail = form.cleaned_data['Nemail']
			service = 'Change of Email'


			data = {
				'Name':Fname + " " + Lname ,
				'Mobile':mobile ,
				'Cemail':Cemail ,
				'nEmail':nEmail ,
				'service':service,
			}

			message = '''
			Full Name: {}
			Phone Number: {}
			Current Email: {}
			New Email: {}
			'''.format(data['Name'],data['Mobile'],data['Cemail'],data['nEmail'])

			send_mail(data['service'],message,'',['kinyuacaleb554@gmail.com'])
			return render(request,'webApp/change.html',{'Fname':Fname,'service':service})
	else:
		return render(request,'webApp/change.html',{'form':form})			

def application(request):
	form = Application()
	if request.method == 'POST':
		form = Application(request.POST)
		if form.is_valid():
			form.save()
			Fname = form.cleaned_data['firstName']
			Lname = form.cleaned_data['lastName']
			mobile = form.cleaned_data['mobile']
			Email = form.cleaned_data['email']
			service = form.cleaned_data['service']

			data = {
				'Name':Fname + " " + Lname ,
				'Mobile':mobile ,
				'Email':Email ,
				'service':service,
			}

			message = '''
			Full Name: {}
			Phone Number: {}
			Sender Email: {}
			'''.format(data['Name'],data['Mobile'],data['Email'])

			send_mail(data['service'],message,'',['kinyuacaleb554@gmail.com'])

			return render(request,'webApp/application.html',{'Fname':Fname,'service':service})
	else:
		return render(request,'webApp/application.html',{'form':form})
			

def other(request):
	form = Other()
	if request.method == 'POST':
		form = Other(request.POST)
		if form.is_valid():
			form.save()
			Fname = form.cleaned_data['firstName']
			Lname = form.cleaned_data['lastName']
			mobile = form.cleaned_data['mobile']
			Email = form.cleaned_data['email']
			mess = form.cleaned_data['message']
			service = form.cleaned_data['service']

			data = {
				'Name':Fname + " " + Lname ,
				'Mobile':mobile ,
				'Email':Email ,
				'mess':mess,
				'service':service,
			}

			message = '''
			Full Name: {}
			Phone Number: {}
			Design Description:{}
			Sender Email: {}
			'''.format(data['Name'],data['Mobile'],data['mess'],data['Email'])

			send_mail(data['service'],message,'',['kinyuacaleb554@gmail.com'])
			return render(request,'webApp/other.html',{'Fname':Fname,'service':service})

	else:
		return render(request,'webApp/other.html',{'form':form})

	
def contact(request):
	form = Contact()
	if request.method == 'POST':
		form = Contact(request.POST)
		if form.is_valid():
			form.save()
			Fname = form.cleaned_data['firstName']
			Lname = form.cleaned_data['lastName']
			mobile = form.cleaned_data['mobile']
			Email = form.cleaned_data['email']
			subject = form.cleaned_data['subject']
			mess = form.cleaned_data['message']

			data = {
				'Name':Fname + " " + Lname ,
				'Mobile':mobile ,
				'Email':Email ,
				'subject':subject,
				'mess':mess,
			}

			message = '''
			Full Name: {}
			Phone Number: {}
			New Message:{}
			From: {}
			'''.format(data['Name'],data['Mobile'],data['mess'],data['Email'])

			send_mail(data['subject'],message,'',['kinyuacaleb554@gmail.com'])
			return render(request,'webApp/contact.html',{'Fname':Fname})
	else:
		return render(request,'webApp/contact.html',{'form':form})

	

			


		









			

	 


