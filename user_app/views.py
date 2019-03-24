from django.shortcuts import render, redirect
from django.http import HttpResponse
from . import models
# Create your views here.

temp = 0

def loginuser(request):
    return render(request,'user_app/loginuser.html')

def registration(request):
    return render(request, 'user_app/registration.html')

def after_registration(request):
    full_name = request.POST.get('name')
    dob = request.POST.get('dob')
    salary = request.POST.get('salary')
    country = request.POST.get('country')
    email = request.POST.get('email')
    password = request.POST.get('pass')

    data = models.UserData(full_name = full_name, dob = dob, salary = salary, country = country, email = email, password = password)
    data.save()

    return render(request,'user_app/after_registration.html')

def userdashboard(request):
    email = request.POST.get('email')
    password = request.POST.get('pass')
    password = request.POST.get('pass')
    if models.UserData.objects.filter(email=email, password=password):
        request.session['username'] = password;
        return render(request, 'user_app/user_dashboard.html')
    else:
        return HttpResponse(
            "<html><body><h1 align='center' style='color:red'>OOPS! Incorrect username or password </h1></body></html>")


def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('/')


