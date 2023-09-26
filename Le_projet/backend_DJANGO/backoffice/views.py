from django.shortcuts import render
import time
# Create your views here.
from django.http import HttpResponse
from backoffice.models import Contrat


def my_view(request):
    return HttpResponse("Hello, world!")


def home(request):
    return render(request, 'home.html')

def login(request):
    return HttpResponse("Hello, world!")

def liste_contrats(request):
    Contrat.generate_fake_data(20)
    time.sleep(5)
    contrats = Contrat.objects.filter(en_cours=True)
    context = {'contrats': contrats}
    return render(request, 'liste_contrats.html', context)