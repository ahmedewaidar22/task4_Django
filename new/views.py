from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth import authenticate,login as auth_login
from django.contrib.auth.models import User
from .forms import *
from django.views.decorators.http import require_http_methods
from django.views import View
from django.views.generic import ListView

class Intakelist(ListView):
    model = Intake

# class Tracklist(ListView):
#     model = Track

def nav(request):
    return render(request, 'nav.html')

def forms(request):
    context={}
    # form = Traineeinsert1()
    form = Traineeinsert()
    context['form']=form
    if (request.method == 'GET'):
        return render(request, 'forms.html',context)
    else:
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']
        Intake.objects.create(username=username, email=email, password=password)
        if request.POST.get('check', '') == 'on':
            User.objects.create_user(username=username, password=password, is_staff=True)
        else:
            User.objects.create_user(username=username, password=password, is_staff=False)

    return render(request, 'forms.html', context)

def delete(request):
    if (request.method == 'GET'):
        return render(request, 'delete.html')
    else:
        context = {}
        id = request.POST['id']

        Intake.objects.filter(id=id).delete()
        intakes = Intake.objects.all()
        context['intakes'] = intakes
        return render(request, 'delete.html',context)
def insertstudent(request):
    if (request.method == 'GET'):
        return render(request, 'insertstudent.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']
        Intake.objects.create(username=username, email=email, password=password)
        if request.POST.get('check', '') == 'on':
            User.objects.create_user(username=username, password=password, is_staff=True)
        else:
            User.objects.create_user(username=username, password=password, is_staff=False)

    return render(request, 'insertstudent.html')

def selectbyname(request):
    context={}
    if (request.method == 'GET'):
        return render(request, 'selectbyname.html')
    else:
         username = request.POST['username']
         intakes = Intake.objects.all().filter(username=username)
         context['intakes'] = intakes
         return render(request, 'selectbyname.html',context)
def selectall(request):
    context = {}
    intakes = Intake.objects.all()
    context['intakes'] = intakes
    return render(request, 'selectall.html',context)
def update(request):
    if (request.method == 'GET'):
        return render(request, 'update.html')
    else:
        id = request.POST['id']
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']
        Intake.objects.filter(id=id).update(username=username,email=email,password=password)
    return render(request, 'update.html')
def homenav(request):
    return render(request, 'homenav.html')

def signup(request):
    if (request.method == 'GET'):
        return render(request, 'signup.html')
    else:
        username = request.POST['username']
        email = request.POST['email']
        password =request.POST['password']

        Intake.objects.create(username=username, email=email, password=password)
        if request.POST.get('check', '') == 'on':
            User.objects.create_user(username=username,password=password,is_staff=True)
        else:
            User.objects.create_user(username=username, password=password, is_staff=False)

        return  redirect("login")
def login(request):
    if (request.method == 'GET'):
        return render(request, 'login.html')
    else:

        username = request.POST['username']
        password = request.POST['password']
        intakes = Intake.objects.all().filter(username=username, password=password)
        authuser=authenticate(username=username,password=password)
        for intake in intakes:

            if intake.username==username and intake.password==password and authuser is not None:
                request.session['username']= username
                auth_login(request,authuser)
                return  redirect("homenav")
            else:
                return render(request, "login.html")



def logout(request):
    request.session.clear()
    return redirect('login')

