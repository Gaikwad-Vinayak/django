
from django import forms
from django.utils.translation import gettext_lazy as _
from django.forms import fields
from .models import student
class modelform(forms.ModelForm):
    class Meta:
        model=student
        fields=['name','roll','city']
        #fields='__all__'
        #exclude=['name']     # remove attribule name
        labels={'name':'enter name','roll':'enter roll'}
        help_text={'name':'name here'}
        error_messages = {
            'name': {
                'max_length': _("This writer's name is too long."),
            },
        }
        widgets={'name':forms.TextInput(attrs={'class':'myclass'})}

# model form inheritance

class teacherregistration(modelform):
    class Meta(modelform.Meta):
        fields=['name','roll']