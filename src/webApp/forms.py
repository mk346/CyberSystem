from django import forms
from django.forms import ModelForm
from .models import details,ChangeDet,Apply,Rest,Register


class myForm(ModelForm):
	class Meta:
		model = details
		fields = ('fname','lname','mobile','email','IdNumber','Pin','service')
		labels = {
			'fname': 'First Name',  'class':'form-label',
			'lname': 'Last Name',  'class':'form-label',
			'mobile': 'Phone Number eg 0723456789', 'class':'form-label',
			'email': 'Your Email',  'class':'form-label',
			'IdNumber': 'Your National ID Number','class':'form-label',
			'Pin': 'KRA PIN eg AOX67FR45672F',  'class':'form-label',
			'service': 'Please Choose Your Service',  'class':'form-label',

		}

		widgets = {
			'fname':forms.TextInput(attrs={'class':'form-control',}),
			'lname':forms.TextInput(attrs={'class':'form-control',}),
			'mobile':forms.NumberInput(attrs={'class':'form-control',}),
			'email':forms.EmailInput(attrs={'class':'form-control',}),
			'IdNumber':forms.NumberInput(attrs={'class':'form-control',}),
			'Pin':forms.TextInput(attrs={'class':'form-control',}),

		}	

	def clean_email(self):
		email = self.cleaned_data.get('email')

		with open("webApp/disposable_emails.txt", 'r') as f:
			blacklist = f.read().splitlines()

		for disposable_email in blacklist:
			if disposable_email in email:
				raise forms.ValidationError("Spams Not Allowed")
		return email


class Registration(ModelForm):
	class Meta:
		model = Register
		fields = '__all__'
		labels = {
			'firstName':'First Name',
			'lastName':'Last Name',
			'mobile':'Your Phone Number',
			'email':'Your Email',
			'idNumber':'Your National ID/Alien ID Number',
			'PostalCode':'Postal Code; if you dont have enter 000',
			'PostalAddress':'Postal Address; if you dont have enter 000',
			'county':'Enter Your County',
			'town':'Your Town/City of Residence',
			'district':'Enter Your District',
			'dob':'Enter Your Date of Birth i.e DD/MM/YY',
		}
		widgets = {
			'firstName':forms.TextInput(attrs={'class':'form-control',}),
			'lastName':forms.TextInput(attrs={'class':'form-control',}),
			'mobile':forms.NumberInput(attrs={'class':'form-control',}),
			'email':forms.EmailInput(attrs={'class':'form-control',}),
			'idNumber':forms.NumberInput(attrs={'class':'form-control',}),
			'PostalCode':forms.NumberInput(attrs={'class':'form-control',}),
			'PostalAddress':forms.NumberInput(attrs={'class':'form-control',}) ,
			'county':forms.TextInput(attrs={'class':'form-control',}) ,
			'town':forms.TextInput(attrs={'class':'form-control',}) ,
			'district':forms.TextInput(attrs={'class':'form-control',}) ,
			'dob':forms.DateInput(attrs={'class':'form-control',}),
		}

	def clean_email(self):
		email = self.cleaned_data.get('email')

		with open("webApp/disposable_emails.txt", 'r') as f:
			blacklist = f.read().splitlines()

		for disposable_email in blacklist:
			if disposable_email in email:
				raise forms.ValidationError("Spams Not Allowed")
		return email

class Change(ModelForm):
	class Meta:
		model = ChangeDet
		fields = '__all__'
		labels = {
			'firstName':'First Name',
			'lastName':'Last Name',
			'mobile':'Your Phone Number',
			'Cemail':'Your Current Email: i.e the email you wish to change',
			'Nemail':'New Email: i.e the email you wish to change to', 
		}
		widgets = {
			'firstName':forms.TextInput(attrs={'class':'form-control'}),
			'lastName':forms.TextInput(attrs={'class':'form-control'}),
			'mobile':forms.NumberInput(attrs={'class':'form-control'}),
			'Cemail':forms.EmailInput(attrs={'class':'form-control'}),
			'Nemail':forms.EmailInput(attrs={'class':'form-control'}),
		}

	def clean_email(self):
		currentEmail = self.cleaned_data.get('Cemail')
		newEmail = self.cleaned_data.get('Nemail')

		with open("webApp/disposable_emails.txt", 'r') as f:
			blacklist = f.read().splitlines()

		for disposable_email in blacklist:
			if disposable_email in currentEmail and disposable_email in newEmail:
				raise forms.ValidationError("Spams Not Allowed")
		return currentEmail,newEmail

class Application(ModelForm):
	class Meta:
		model = Apply
		fields = '__all__'
		labels = {
			'firstName':'First Name',
			'lastName':'Last Name',
			'mobile':'Your Phone Number',
			'email':'Your Email',
			'service':'Please Choose Your Service',
		}
		widgets = {
			'firstName':forms.TextInput(attrs={'class':'form-control'}),
			'lastName':forms.TextInput(attrs={'class':'form-control'}),
			'mobile':forms.NumberInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
		}


	def clean_email(self):
		email = self.cleaned_data.get('email')

		with open("webApp/disposable_emails.txt", 'r') as f:
			blacklist = f.read().splitlines()

		for disposable_email in blacklist:
			if disposable_email in email:
				raise forms.ValidationError("Spams Not Allowed")
		return email



class Other(ModelForm):
	class Meta:
		model = Rest
		fields = ('firstName','lastName','mobile','email','service','message')
		labels = {
			'firstName':'First Name',
			'lastName':'Last Name',
			'mobile':'Your Phone Number',
			'email':'Your Email',
			'service':'Please Choose Your Service',
			'message':'Type In Some Description Of the Design You Want ',

		}
		widgets = {
			'firstName':forms.TextInput(attrs={'class':'form-control'}),
			'lastName':forms.TextInput(attrs={'class':'form-control'}),
			'mobile':forms.NumberInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'message': forms.Textarea(attrs={'class':'form-control'})
		}

	def clean_email(self):
		email = self.cleaned_data.get('email')

		with open("webApp/disposable_emails.txt", 'r') as f:
			blacklist = f.read().splitlines()

		for disposable_email in blacklist:
			if disposable_email in email:
				raise forms.ValidationError("Spams Not Allowed")
		return email

class Contact(ModelForm):
	class Meta:
		model = Rest
		fields = ('firstName','lastName','mobile','email','subject','message')
		labels = {
			'firstName':'First Name',
			'lastName':'Last Name',
			'mobile':'Your Phone Number',
			'email':'Your Email',
			'subject':'Message Subject',
			'message':'Type In Your Message',
		}
		widgets = {
			'firstName':forms.TextInput(attrs={'class':'form-control'}),
			'lastName':forms.TextInput(attrs={'class':'form-control'}),
			'mobile':forms.NumberInput(attrs={'class':'form-control'}),
			'email':forms.EmailInput(attrs={'class':'form-control'}),
			'subject':forms.TextInput(attrs={'class':'form-control'}),
			'message': forms.Textarea(attrs={'class':'form-control'}),
		}
	
	def clean_email(self):
		email = self.cleaned_data.get('email')

		with open("webApp/disposable_emails.txt", 'r') as f:
			blacklist = f.read().splitlines()

		for disposable_email in blacklist:
			if disposable_email in email:
				raise forms.ValidationError("Spams Not Allowed")
		return email
















  

		






	
