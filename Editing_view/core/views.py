
from django.shortcuts import render,HttpResponse
from django.views.generic.edit import FormView,CreateView,UpdateView,DeleteView

from .forms import std
from django.views.generic.base import TemplateView

from .forms import forms
from .models import student
# Create your views here.
 # only ruturn default form in formview

class formse(FormView):
    template_name='core/formview.html'
    form_class=std
    def form_valid(self,form):
        print(form.cleaned_data['name'])
        return HttpResponse('ok')


# create view is used to save data in databases
class creates(CreateView):
    get_form=std
    models=student
    fields=['name','city']
    success_url='/suc/'
    template_name='core/formview.html'


class updates(UpdateView):
    template_name='core/formview.html'
    model=student
    fields=['name','city']
    success_url='/suc/'

class delete(DeleteView):
    model=student
    template_name='core/del.html'
    success_url='/suc/'



class suc(TemplateView):
    template_name='core/home.html'