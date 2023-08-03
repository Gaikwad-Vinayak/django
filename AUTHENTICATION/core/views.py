from django.contrib.auth import authenticate
from django.shortcuts import render,HttpResponseRedirect
from django.contrib.auth.forms import UserCreationForm
from .forms import formd
from django.contrib.auth import authenticate,login,logout
from django.contrib import auth
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.
def home(request):
    if request.method=='POST':
        fm=formd(request.POST)
        if fm.is_valid():
            fm.save()
    else:
        fm=formd
    return render(request,'core/home.html',{'form':fm})

def login(request):
    if request.method=='POST':
        fm=AuthenticationForm(request=request,data=request.POST)
        if fm.is_valid():
            un=fm.cleaned_data['username']
            pa=fm.cleaned_data['password']
            user=auth.authenticate(username=un,password=pa)
            if user is not None:
                auth.login(request,user)
                return HttpResponseRedirect('/suc/')
    else:
        fm=AuthenticationForm()
    return render(request,'core/login.html',{'form':fm})


def suc(request):
    if request.user.is_authenticated:
        return render(request,'core/suc.html')
    return HttpResponseRedirect('/login/')

def logout(request):
    auth.logout(request)
    return HttpResponseRedirect('/login/')
