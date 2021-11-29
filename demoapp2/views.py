from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def fnabc(request):
    return HttpResponse("hello world")
def fnmno(req):
    return render(req,'demofile1.html')
