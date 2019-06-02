from django import forms
from .choices import *
from django.core.validators import FileExtensionValidator

class ContactForm(forms.Form):
    name = forms.CharField(max_length = 100)
    firstname = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 100)
    phone = forms.CharField(max_length = 100)
    building = forms.ChoiceField(choices=BUILDING_CHOICES)
    office = forms.CharField(max_length = 100)
    upload = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'pptx'])])
    format = forms.ChoiceField(widget = forms.Select(attrs = {'onchange' : "checkFormat();"}), choices=FORMAT_CHOICES)
    formatHeight = forms.FloatField(required=False)
    formatWidth = forms.FloatField(required=False)
    comments = forms.CharField(widget = forms.Textarea, required=False)
