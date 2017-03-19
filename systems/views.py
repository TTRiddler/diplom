from django.shortcuts import render
from .models import NumericSystem, AlgebraicSystem, NumericSection, AlgebraicSection

# Create your views here.
def mainPage(request):
    return render(request, 'systems/index.html')

def numeric(request):
	return render(request, 'systems/numeric.html', {'sections': NumericSystem.objects.all(), 'subsections': NumericSection.objects.all()})

def algebraic(request):
	return render(request, 'systems/algebraic.html', {'sections': AlgebraicSystem.objects.all(), 'subsections': AlgebraicSection.objects.all()})