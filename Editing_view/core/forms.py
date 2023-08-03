from django import forms

class std(forms.Form):
    name=forms.CharField()
    city=forms.CharField()