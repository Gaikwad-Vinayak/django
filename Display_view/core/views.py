from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from .models import student
# Create your views here.
class demo(ListView):
    # return all objects
    # default template demend =core/student_list.html
    # default form obect is =student_list
    model=student
    template_name='core/home.html'
    context_object_name='stu'

class detail(DetailView):
    # it return single object 
    # its demand on slug or id attribute
    model=student
    context_object_name='stu'
    template_name='core/DetailView.html'