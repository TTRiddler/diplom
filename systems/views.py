from django.shortcuts import render
from .models import NumericSystem, AlgebraicSystem, NumericSection, AlgebraicSection
from django.contrib import auth


def mainPage(request):
    return render(request, 'systems/index.html', {'username': auth.get_user(request).username})

def numeric(request):
	return render(request, 'systems/numeric.html', {'sections': NumericSystem.objects.all(), 'subsections': NumericSection.objects.all(), 'username': auth.get_user(request).username})

def algebraic(request):
	return render(request, 'systems/algebraic.html', {'sections': AlgebraicSystem.objects.all(), 'subsections': AlgebraicSection.objects.all(), 'username': auth.get_user(request).username})