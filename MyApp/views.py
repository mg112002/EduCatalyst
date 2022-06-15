from django.http import request
from django.http.response import Http404
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from MyApp.models import Contact, Course, Quizze
from datetime import datetime
from django.contrib import messages

def index(request):
    return render(request, 'login.html')

def home(request):
    course= Course.objects.all()
    params= {'course': course}
    return render(request,"newhome.html",params)

def contact(request):
    if request.method == "POST":
        name= request.POST.get('name')
        email= request.POST.get('email')
        phone= request.POST.get('phone')
        desc= request.POST.get('desc')
        contact=Contact(name=name, email=email, phone=phone, desc=desc, date=datetime.today())
        contact.save()
        messages.success(request, 'Thanks for contacting us!! Your response has been sent.')
    return render(request, 'contact.html')
        
def register(request):
    if request.method == 'POST':
        username= request.POST['username']
        email= request.POST['email']
        password= request.POST['password']
        user= User.objects.create_user(username=username, email=email, password=password)
        user.save()
        messages.success(request, "Your account has been created! Please login to continue.")
        return redirect('/login/')
    else:
        return Http404


def loginUser(request):
    if request.method == 'POST':
        loginusername= request.POST['loginusername']
        loginpassword= request.POST['loginpassword']
        user= authenticate(username= loginusername, password= loginpassword)
        if user is not None:
            login(request, user)
            messages.success(request, "Successfully logged in!")
            return redirect("/home/")
        else:
            messages.error(request, "Invalid Credentials:( Please enter the correct credentials!")
            return render(request, 'login.html')
    return render(request, 'login.html')

def courseview(request, myid):
    if request.user.is_anonymous:
        return redirect("/login/")
    else:
        courses= Course.objects.filter(id=myid)
        return render(request, "courseview.html", {'course':courses[0]})

def quiz(request, myid):
    if request.user.is_anonymous:
        return redirect("/login/")
    else:
        quizzes= Quizze.objects.filter(id=myid)
        return render(request,"quiz.html", {'quiz':quizzes[0]})
          
def about(request):
    return render(request, "about.html")

def logoutUser(request):
    logout(request)
    messages.success(request, "Successfully logged out!")
    return redirect("/login/")
