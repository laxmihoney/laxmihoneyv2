from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout

# Create your views here.
def home(request):
    return render(request,'home.html')

def signup_view(request):
    if request.method=="POST":
        username = request.POST['username']
        username = username.casefold()
        fname = request.POST['fname']
        fname = fname.capitalize()
        lname = request.POST['lname']
        lname = lname.capitalize()
        email = request.POST['email']
        password = request.POST['pass2']

        myuser = User.objects.create_user(username, email, password)
        myuser.first_name = fname
        myuser.last_name = lname
        myuser.save()
        messages.success(request, "user created successfully")
        return redirect('login')

    return render(request, 'signup.html')

def login_view(request):
    if request.user.is_authenticated:
        return redirect('profile')

    else:
        if request.method=="POST":
            username = request.POST['username']
            password = request.POST['pass2']

            user = authenticate(username=username, password=password)

            if user is not None:
                login(request,user)
                fname = user.first_name
                messages.success(request, f"{fname} logged In successfully")
                return redirect('home')
            else:
                messages.error(request,"Bad credentials")
                return redirect('login')

        return render(request, 'login.html')

def logout_view(request):
    logout(request)
    messages.success(request,"Logged Out successfully")
    return redirect('home')

def services(request):
    return render(request, 'service.html')

def profile(request):
    return render(request, 'profile.html')

def about(request):
    return render(request, 'about.html')

def products(request):
    return render(request,'products.html')
