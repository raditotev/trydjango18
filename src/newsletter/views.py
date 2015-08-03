from django import forms
from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render

from .forms import ContactForm, SignUpForm
from .models import SignUp

# Create your views here.
def home(request):
	title = "Hello, "
	form = SignUpForm(request.POST or None)

	if form.is_valid():
		#form.save()
		instance = form.save(commit=False)
		instance.save()

	context = {
		'form': form
	}

	if request.user.is_authenticated() and request.user.is_staff:
		users = SignUp.objects.all()
		context = {
			'users': users
		}

	return render(request, "home.html", context)

def contact(request):
	title = 'Contact Us'
	form = ContactForm(request.POST or None)
	if form.is_valid():
		email = form.cleaned_data.get("email")
		message = form.cleaned_data.get("message")
		full_name = form.cleaned_data.get("full_name")
		subject = 'Site contact form'
		from_email = settings.EMAIL_HOST_USER
		to_email = email
		contact_message = '''
		%s: %s via %s
		'''%(full_name, message, email)
		send_mail(subject,
				contact_message,
				from_email,
    			[to_email],
    			fail_silently=False)
		return render(request, "forms.html", {})



	context = {
		'form': form,
		'title': title,
	}

	return render(request, "forms.html", context)