from django.http import HttpResponse 
from django.shortcuts import render


def home(request):
    return render(request,'index.html') 

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

def login(request):
    return render(request,'signin.html')

def register(request):
    return render(request,'register.html')