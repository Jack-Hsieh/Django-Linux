from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse_lazy
from django.views import generic
from django.contrib.auth.models import User

from django.shortcuts import render, redirect
from users.forms import RegisterForm,ContactForm

# 導入後台程式
from users.models import Post,Pricing,About,Request

from django.contrib.auth.decorators import login_required #User Login Required

from django.http import HttpResponseRedirect


# Create your views here.

# Create signup views for registration
# class SignUp(generic.CreateView):
#     form_class = UserCreationForm
#     success_url = reverse_lazy('login')
#     template_name = 'signup.html'


def register(response):
	if response.method == "POST":
		form = RegisterForm(response.POST)
		if form.is_valid():
			form.save()
			return redirect("/accounts/login/")
		else:
			return redirect("/accounts/signup/")

	else:
		form = RegisterForm()

	return render(response, "signup.html", {"form":form})


def logout(request):
	auth.logout(request)
	return redirect("")


def home(request):
	post_list = list(Post.objects.all())
	return render(request, 'home.html', {'post_list':post_list})

def pricing(request):
	pricing_list = list(Pricing.objects.all())

	return render(request, 'pricing.html', {'pricing_list': pricing_list})


def about(request):
	about_list = list(About.objects.all())

	return render(request, 'about.html', {'about_list': about_list})

@login_required(login_url='/accounts/login/')
def get_ContactForm(request):
	# if this is a POST request we need to process the form data
	if request.method == 'POST':
		# create a form instance and populate it with data from the request:
		form = ContactForm(request.POST)
		# check whether it's valid:
		if form.is_valid():

			#取得 form 包含的資料
			username = form.cleaned_data.get('username'),
			email = form.cleaned_data.get('email'),
			comment = form.cleaned_data.get('comment'),

			# 在系統後台建立資料
			obj = Request.objects.create(
				username = username,
				email = email,
				comment = comment,
				)

			# redirect to a new URL:
			return HttpResponseRedirect('/Comment')


	# if a GET (or any other method) we'll create a blank form
	else:
		form = ContactForm()

	return render(request, 'Comment.html', {'form': form})
