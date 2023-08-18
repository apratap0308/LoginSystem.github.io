from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required

# Create your views here.

@login_required(login_url='login')
def Home(request):
    return render(request, 'home.html')

def SignupPage(request):
    if request.method=='POST':
        name=request.POST.get('name')
        uname=request.POST.get('username')
        email=request.POST.get('email')
        phone=request.POST.get('phone')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')
        gender=request.POST.get('gender')

        if pass1!=pass2:
            return HttpResponse("Password is not matched!")
        else:
            my_user=User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')



    return render(request, 'signup/index.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse("Username or Password doesn't match")
    return render(request, 'Login/index.html')


def LogoutPage(request):
    logout(request)
    return redirect('login')