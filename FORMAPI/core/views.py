from django.shortcuts import render
from .forms import formsstudent
from .models import student
# Create your views here.
def show(request):
    #dic=formsstudent(auto_id=True,label_suffix='-',initial={'name':'enter name'})
    if request.method=='POST':
        dic=formsstudent(request.POST)
        if dic.is_valid():
            un=dic.cleaned_data['name']
            ct=dic.cleaned_data['city']
            ro=dic.cleaned_data['roll']
            reg=student(name=un,roll=ro,city=ct)
            if reg is not None:
                reg.save()
    else:
        dic=formsstudent()
    return render(request,'core/home.html',{'form':dic})