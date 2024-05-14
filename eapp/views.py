from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup(request):
    if request.method=="POST":
        username = request.POST['username']
        fname = request.POST['fname']
        lname = request.POST['lname']
        email = request.POST['email']
        password = request.POST['pass2']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "user created successfully")
        return redirect('signin')

    return render(request, 'signup.html')

def signin(request):
    if request.method=="POST":
        email = request.POST['email']
        password = request.POST['pass2']

        user = authenticate(email = email, password=password)

        if user is not None:
            login(request,user)
            fname = user.first_name
            return render(request,'home.html',{'fname':fname})
        else:
            messages.error(request,"Bad credentials")
            return redirect('signin')

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
