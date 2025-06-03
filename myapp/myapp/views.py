from django.shortcuts import render

def For_Error(request,exception):
   return render(request,'404.html',status=404)