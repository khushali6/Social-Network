from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    return render(request,"index.html")

def connection(request):
    return render(request,"connection.html")

def editprofile(request):
    return render(request,"edit-profile.html")

def profile(request):
    return render(request,"profile.html")

def signin(request):
    return render(request,"sign-in.html")

def signup(request):
    return render(request,"sign-up.html")