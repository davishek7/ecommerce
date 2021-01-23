from django import forms
from django.forms import ModelForm
from store.models import Customer
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

class CreateUserForm(UserCreationForm):
	email=forms.EmailField()

	def __init__(self,*args,**kwargs):
		super(CreateUserForm, self).__init__(*args, **kwargs)

		for fieldname in ['username','password1','password2']:
			self.fields[fieldname].help_text=None

	def clean(self):
		email=self.cleaned_data.get('email')
		if User.objects.filter(email=email).exists():
			raise forms.ValidationError("Email already exists")
		return self.cleaned_data

	class Meta:
		model=User
		fields=['username','email','password1','password2']

class CustomerForm(ModelForm):
	class Meta:
		model=Customer
		fields='__all__'
		exclude=['user']