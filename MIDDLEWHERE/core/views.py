from django.shortcuts import render

# Create your views here.
def middlewhere(request):
    return render(request,'core/middlewhere.html')