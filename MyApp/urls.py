from django.contrib import admin
from django.urls import path
from MyApp import views

urlpatterns = [
    path("", views.home, name='MyApp'),
    path("home/", views.home, name='home'),
    path("register/", views.register, name='register'),
    path("login/", views.loginUser, name='login'),
    path("logout/", views.logoutUser, name='logout'),
    path("about/", views.about, name='about'),
    path("contact/", views.contact, name='contact'),
    path("courses/<int:myid>", views.courseview, name='courseview'),
    path("quiz/<int:myid>", views.quiz, name='quiz')
]