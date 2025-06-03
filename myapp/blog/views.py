from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.urls import reverse
# Create your views here.
def index (request):
    text=[{'id':1},{'id':2}]
    return render(request,'index.html',{'text':text})

def new (request):
    return HttpResponse("centeral bank")

def old_url(request):
    return redirect(reverse("blog:new_url_blog"))

def new_url(request):
    return HttpResponse("new url")

def all(request):
    return HttpResponse("*")

def detail(request,id):
    return render(request,'detail.html',{'post_id':id})

def base(request):
    return render(request,'base.html')

def NewThings(request):
    text = "Bye Nanba"
    return render(request,'NewThings.html',{'text':text})

def For_Tag(request):
    text = [{'tittle':'Singam1'},{'tittle':'Singam2'}]
    return render(request,'For_Tag.html',{'posts':text})