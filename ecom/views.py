from django.shortcuts import render, redirect, reverse
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required, user_passes_test
from django.contrib.auth.models import Group
from django.contrib import messages
from django.conf import settings
from django.core.mail import send_mail



def dashboard(request):
	context = {
		'page_title': 'Home',
	}

	print(request.user.is_authenticated())

	template_name = None
	if request.user.is_authenticated():
		# logika untuk user
		template_name = 'index_user.html'
	else:
		# logika untuk anonymous
		template_name = 'index_anonymous.html'
	
	return render(request, template_name, context)


def loginView(request):
	context = {
		'page_title':'LOGIN',
	}
	user = None
	if request.method == "POST":
		
		username_login = request.POST['username']
		password_login = request.POST['password']
		
		user = authenticate(request, username=username_login, password=password_login)

		if user is not None:
			login(request, user)
			return redirect('dashboard')
		else:
			return redirect('login')
		
	return render(request, 'dashboard/login.html', context)


@login_required
def logoutView(request):
	context = {
		'page_title':'logout'
	}

	if request.method == "POST":
		if request.POST["logout"] == "Submit":
			logout(request)

		return redirect('dashboard')	


	return render(request, 'dashboard/logout.html', context)


def tentangjualin(request):
	context = {
		'page_title':'tentang',
	}
	return render(request, 'tentang_jualin.html', context)


def informasikontak(request):
	context = {
		'page_title':'kontak',
	}
	return render(request, 'informasi_kontak.html', context)



