from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('home/', views.home, name = 'home'),
    path('signin/', views.signin, name = 'signin'),
    path('products/', views.products, name = 'products'),
    path('services/', views.services, name = 'serives'),
    path('signup/', views.signup, name = 'signup'),
    path('profile/', views.profile, name = 'profile'),
    path('signout/', views.signout, name = 'signout'),
    path('about/', views.about,name="about")
    ]
