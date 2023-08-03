from django import forms
from django.core import validators
from django.forms.fields import CharField

class formsstudent(forms.Form):
    name=forms.CharField(required=True,label='Enter Name',label_suffix='-',initial='vinayak',disabled=False)
    roll=forms.IntegerField(help_text='enter name here',widget=forms.NumberInput(attrs={'class':'myclass'}))
    city=CharField(error_messages={'required':'enter city'})

    #def clean(self):
     #   clean_data=super().clean()
      #  val=self.cleaned_data['city']
       # if len(val) < 4:
        #    raise forms.ValidationError('more than for')
        #return clean_data