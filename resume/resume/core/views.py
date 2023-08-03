from django.shortcuts import render

# Create your views here.
def Home(request):
    dict={'home':'active'}
    return render(request,'core/home.html',dict)
def contact(request):
     dict1={'con':'active'}
     return render(request,'core/contact.html',dict1)    