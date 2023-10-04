from django.http import HttpResponse 
from django.shortcuts import render,redirect
from django.contrib.auth.models import User,auth
from django.contrib import messages

def home(request):
    return render(request,'index.html') 

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def signin(request):
    return render(request,'signin.html')

def registration(request):
    return render(request,'registration.html')