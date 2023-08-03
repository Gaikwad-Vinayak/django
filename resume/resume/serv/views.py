from django.shortcuts import render

# Create your views here.
def services(request):
    dict2={'ser':'contact'}
    return render(request,'serv/services.html',context=dict2)