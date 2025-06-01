from django.shortcuts import render,redirect
from django.http import HttpResponse
# Create your views here.
def index (request):
    return HttpResponse("Hello ")

def new (request):
    return HttpResponse("New")

def old_url(request):
    return redirect("new_url")

def new_url(request):
    return HttpResponse("new url")