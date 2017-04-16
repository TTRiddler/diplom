from django.shortcuts import render
from .models import NumericSystem, AlgebraicSystem, NumericSection, AlgebraicSection
from django.contrib import auth
from loginsys import models
from django.core.exceptions import ObjectDoesNotExist


def mainPage(request):
    return render(request, 'systems/index.html', 
    	{'username': auth.get_user(request).username})

def numeric(request):
	return render(request, 'systems/numeric.html', 
		{'sections': NumericSystem.objects.all(), 
		'subsections': NumericSection.objects.all(), 
		'username': auth.get_user(request).username})

def algebraic(request):
	return render(request, 'systems/algebraic.html', 
		{'sections': AlgebraicSystem.objects.all(), 
		'subsections': AlgebraicSection.objects.all(), 
		'username': auth.get_user(request).username})

def infoPage_num(request, subsection_id=1):
	try:
		profile_user = models.Profile.objects.get(user_id=auth.get_user(request).id)
	except ObjectDoesNotExist:
		profile_user = False
	if profile_user:
		if profile_user.teachers_key:
			user_enter = True
		else:
			user_enter = False
	else:
		user_enter = False
	return render(request, 'systems/infoPage_num.html', 
		{'subsection': NumericSection.objects.get(id=subsection_id),
		'username': auth.get_user(request).username,
		'user_enter': user_enter})

def infoPage_alg(request, subsection_id=1):
	try:
		profile_user = models.Profile.objects.get(user_id=auth.get_user(request).id)
	except ObjectDoesNotExist:
		profile_user = False
	if profile_user:
		if profile_user.teachers_key:
			user_enter = True
		else:
			user_enter = False
	else:
		user_enter = False
	return render(request, 'systems/infoPage_alg.html', 
		{'subsection': AlgebraicSection.objects.get(id=subsection_id),
		'username': auth.get_user(request).username,
		'user_enter': user_enter})

def about(request):
    return render(request, 'systems/about.html', 
    	{'username': auth.get_user(request).username})