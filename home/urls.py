from django.contrib import admin
from django.urls import path, include
from home import views

urlpatterns = [
    path('', views.signupPage, name='signupPage'),
    path('home/', views.home, name='home'),
    path('contact/', views.contact, name='contact'),
    path('about/', views.about, name='about'),
    path('project/', views.project, name='project'),
    path('loginPage/', views.loginPage, name='loginPage'),

]