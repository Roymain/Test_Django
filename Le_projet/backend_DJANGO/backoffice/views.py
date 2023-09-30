from django.shortcuts import render
import time
# Create your views here.
from django.http import HttpResponse
from backoffice.models import Contrat
from django.contrib.auth import authenticate,logout,  login as auth_login
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import redirect


def my_view(request):
    return HttpResponse("Hello, world!")

def home(request):
    return render(request, 'home.html')

def login(request):
    # User.objects.create_user(username='test', password='password')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)

        if user is not None:
            auth_login(request, user)
            return render(request, 'home.html')
        else:
            messages.error(request, "bad credential")
            return redirect('login')

    return render(request, 'login.html')

def signout(request):
    logout(request)
    messages.success(request, "logout")
    return redirect('/')






def liste_contrats(request):
    Contrat.generate_fake_data(20)
    time.sleep(5)
    contrats = Contrat.objects.filter(en_cours=True)
    context = {'contrats': contrats}
    return render(request, 'liste_contrats.html', context)

def pokepage(request):
    return render(request, 'pokepage.html')
