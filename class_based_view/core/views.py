from msilib.schema import Class
from django.shortcuts import render
from django.views import View
from django.views.generic.base import TemplateView,RedirectView
# Create your views here.
#class demo(View):
#    def get(self,request):
#        return render(request,'core/home.html')

#class demo(TemplateView):
#    template_name='core/home.html'
#    def get_context_data(self, **kwargs):
#        context = super().get_context_data(**kwargs)
#        context["name"] = 'vinayak'
#        return context


class demo(RedirectView):
    url='https://www.utomik.com/hp_edgefavourites'