from django.shortcuts import render, redirect
from . import forms,  models
from django.http import HttpResponseRedirect,HttpResponse
from django.contrib.auth.models import Group
from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
# Create your views here.
def dashboard(request):
	context = {
		'heading':'ini dashboard',
	}
	return render(request, 'dashboard/index.html', context)


