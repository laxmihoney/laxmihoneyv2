from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('home/', views.home, name = 'home'),
    path('login/', views.login_view, name = 'login'),
    path('products/', views.products, name = 'products'),
    path('services/', views.services, name = 'serives'),
    path('signup/', views.signup_view, name = 'signup'),
    path('profile/', views.profile, name = 'profile'),
    path('logout/', views.logout_view, name = 'logout'),
    path('about/', views.about,name="about")
    ]
