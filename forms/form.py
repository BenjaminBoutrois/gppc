from django import forms
from .choices import *
from django.core.validators import FileExtensionValidator
from django.utils.dateformat import format
from django.conf import settings
from datetime import datetime, timedelta

class ContactForm(forms.Form):
    date = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS, initial = datetime.now())
    name = forms.CharField(max_length = 100)
    firstname = forms.CharField(max_length = 100)
    email = forms.EmailField(max_length = 100)
    phone = forms.CharField(max_length = 100)
    building = forms.ChoiceField(choices=BUILDING_CHOICES)
    office = forms.CharField(max_length = 100)
    delivery = forms.DateField(input_formats = settings.DATE_INPUT_FORMATS, initial = datetime.now() + timedelta(days=2))
    upload = forms.FileField(validators=[FileExtensionValidator(allowed_extensions=['pdf', 'ppt', 'pptx'])])
    format = forms.ChoiceField(widget = forms.Select(attrs = {'onchange' : "checkFormat();"}), choices=FORMAT_CHOICES)
    formatHeight = forms.FloatField(required=False)
    formatWidth = forms.FloatField(required=False)
    comments = forms.CharField(widget = forms.Textarea, required=False)
