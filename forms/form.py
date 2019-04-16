from django import forms
from .choices import *

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100)
    firstname = forms.CharField(max_length = 100)
    email = forms.CharField(max_length = 100)
    phone = forms.CharField(max_length = 100)
    building = forms.ChoiceField(choices=BUILDING_CHOICES)
    office = forms.CharField(max_length = 100)
    upload = forms.FileField()
    format = forms.ChoiceField(choices=FORMAT_CHOICES)
    formatHeight = forms.CharField(max_length = 100)
    formatWidth = forms.CharField(max_length = 100)
    comments = forms.CharField(widget = forms.Textarea)
