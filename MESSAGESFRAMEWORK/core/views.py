from django.http import request
from django.shortcuts import render
from .models import student
from django.contrib import messages
from .forms import modelform,teacherregistration
# Create your views here.

def show(request):
    if request.method=='POST':
        fm=modelform(request.POST)
        if fm.is_valid():
            fm.save()
            messages.success(request,'data save')

    else:
        fm=modelform()
    return render(request,'core/home.html',{'form':fm})

# model form inheritance

def disp(request):
    dic=teacherregistration()
    return render(request,'core/about.html',{'form':dic})