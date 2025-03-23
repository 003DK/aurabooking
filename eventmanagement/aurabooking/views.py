from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def login(request):
    return render(request,'login.html')
def register(request):
    return render(request,'register.html')
def guest(request):
    return render(request,"guest.html")
def event(request):
    return render(request,'eventmanagement.html')
def create(request):
    return render(request,"createevent.html")
def details(request):
    return render(request,'details.html')
def payment(request):
    return  render(request,"registerpayment.html")