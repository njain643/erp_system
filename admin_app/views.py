from django.shortcuts import render, redirect
from . import models
from user_app.models import UserData
from django.http import HttpResponse
from django.core.files.storage import FileSystemStorage


# Create your views here.


def index(request):
    return render(request,'admin_app/index.html')


def loginadmin(request):
    return render(request,'admin_app/loginadmin.html')

def set_session(request,uname,pwd):
    if uname!="" and pwd != "":
        request.session['usernam'] = uname
        request.session['passowrd'] = pwd
        return  True
    else:
        return False



def admindashboard(request):
    print(request.method)
    print(request.body)
    if request.method == 'GET':

    if request.method == "POST":
        email = request.POST.get('email')
        password = request.POST.get('pass')
        request.session['username'] = email
        request.session['password'] = password
        if request.session.has_key('username') and request.session.has_key('password'):
            if models.Admin.objects.filter(admin_email=request.session['username'], admin_password=request.session['password']):
                # request.session.set_expiry(30)
                user_list = UserData.objects.order_by('full_name')
                user_dict = {'users':user_list}
                return render(request,'admin_app/admin_dashboard.html',context=user_dict)
            else:
                return HttpResponse("ok")
    else:
        return HttpResponse("<html><body><h1 align='center' style='color:red'>OOPS! Incorrect username or password </h1></body></html>")

def logout(request):
    try:
        del request.session['username']
    except:
        pass
    return redirect('/')


def upload(request):
    folder = '/uploadedfile'
    file = request.FILES['myfile']
    fs = FileSystemStorage(location=folder)
    filename = fs.save(file.name,file)
    file_url = fs.url(filename)
    return render(request,'admin_app/upload.html',{'file_url': file_url})