from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse("Hello world")
def contact(request,customer_no):
    return HttpResponse(f"your entering into contact page and customer no {customer_no}")

