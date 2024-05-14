from collections import UserDict
from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    return render(request, 'signup.html')

def signin(request):
    return render(request, 'signin.html')

def signout(request):
    return render(request, 'signout.html')

def services(request):
    return render(request, 'service.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'signin.html')

def products(request):
    return render(request,'products.html')
