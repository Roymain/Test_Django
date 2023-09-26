from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def my_view(request):
    return HttpResponse("Hello, world!")


def home(request):
    return render(request, 'home.html')

def login(request):
    return HttpResponse("Hello, world!")