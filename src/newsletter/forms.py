from django import forms
from .models import SignUp

class ContactForm(forms.Form):
	full_name = forms.CharField()
	email = forms.EmailField()
	message = forms.CharField()

	# def clean_data(self):
	# 	full_name = self.cleaned_data.get('full_name')
	# 	email = self.cleaned_data.get('email')
	# 	message = self.cleaned_data.get('message')
	# 	return full_name, email, message


class SignUpForm(forms.ModelForm):
	class Meta:
		model = SignUp
		fields = ['full_name', 'email']

	def clean_email(self):
		email = self.cleaned_data.get('email')
		return email