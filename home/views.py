from django.shortcuts import render, HttpResponse,redirect
from home.models import Contact
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from django import forms

# Create your views here.
@login_required(login_url='loginPage')
def home(request):
    return render(request, 'home.html')
@login_required(login_url='loginPage')
def contact(request):
    context = {'success': False}
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        desc = request.POST['desc']
        print(name, email, phone, desc)
        ins = Contact(name=name, email=email, phone=phone, desc=desc)
        ins.save()
        context = {'success': True}
        print("data added to the database")
    return render(request, 'contact.html',context)
@login_required(login_url='loginPage')
def about(request):
    return render(request, 'about.html')
@login_required(login_url='loginPage')
def project(request):
    return render(request, 'project.html')

#Signup and Login
def signupPage(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
         raise forms.ValidationError("The two password fields must match.")
        else:
         my_user = User.objects.create_user(uname, email ,pass1 )
         my_user.save()
         return redirect('loginPage')
    return render(request, 'signup.html')
def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pass')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('home')
        else:
            return HttpResponse("Username password incorrect")

    return render(request, 'login.html')

def logoutPage(request):
    logout(request)
    return redirect('loginPage')