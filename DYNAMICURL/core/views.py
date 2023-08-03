from django.shortcuts import render

# Create your views here.
def show(request,id):
    st={'id':'myid'}
    return render(request,'core/home.html',st)

def detail(request):
    return render(request,'core/detail.html')