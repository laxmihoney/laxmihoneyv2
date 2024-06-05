from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib.auth import authenticate, login,logout
from laxmihoneyv2 import settings
from django.core.mail import send_mail
import random




# Create your views here.
def home(request):
    return render(request,'home.html')

def signup_view(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            username = request.POST['username']
            username = username.casefold()
            fname = request.POST['fname']
            fname = fname.capitalize()
            lname = request.POST['lname']
            lname = lname.capitalize()
            email = request.POST['email']
            password = request.POST['pass2']
            
            
            if User.objects.filter(username=username):
                messages.error(request, "username already exists")
                return redirect('signup')
            if User.objects.filter(email=email):
                messages.error(request, "email already exists")
                return redirect('signup')
            myuser = User.objects.create_user(username, email, password)
            myuser.first_name = fname
            myuser.last_name = lname
            myuser.is_active = False
            myuser.save()
            messages.success(request, "Account created successfully!!\nplease verify it to activate! ")


            return redirect('verify')

    return render(request, 'signup.html')

def verify(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:
        if request.method=="POST":
            email = request.POST['emailv']
            if User.objects.filter(email=email).exists():
                user = User.objects.get(email=email)
                vercode = rendom_verification_code_generator()
                subject="Activate Your account for Laxmi Honey Industry"
                message ="Hello " + user.first_name +"!\n"+"Welcome to Laxmi honey industry\n\n"+"your details for verification\n"+"Username: "+user.username+"\nVerification code: "+str(vercode)+"\nThank you"
                from_email = settings.EMAIL_HOST_USER
                to_emails = [user.email]
                send_mail(subject,message,from_email,to_emails, fail_silently=True)
                userverify = user.username
                return render(request,'verifycode.html',{"userverify":userverify,"vercode":vercode})
                

        return render(request, 'verify.html')

def verifycode(request):
    if request.user.is_authenticated:
        return redirect('home')
    else:

        if request.method=="POST":
            username = request.POST['username']
            vericode = request.POST['vericode']
            vercode = request.POST['vercode']
            if User.objects.filter(username = username).exists():
                user = User.objects.get(username=username)
                if int(vericode) == int(vercode):
                    user.is_active=True
                    user.save()
                    messages.success(request,"account verified succesfully login to your account!!")
                    return redirect('login')
                else:
                    messages.error(request,"code didn't match try again!!")
                    userverify = user.username
                    return render(request,'verifycode.html',{"userverify":userverify,"vercode":vercode})
            else:
                messages.error(request,"Failed to verify!!\nEnter username first")
                return redirect('verify')

        return render(request, 'verifycode.html')

def rendom_verification_code_generator():
    vercode = random.randint(100000,999999)
    return vercode
    


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
            
            elif User.objects.filter(username = username).exists():
                user = User.objects.get(username=username)
                uname = user.username
                messages.success(request, f"{uname} you are not verified yet!!\nVerify now")
                return redirect('verify')

            else:
                messages.error(request,"Bad credentials or user not registered!!")
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
