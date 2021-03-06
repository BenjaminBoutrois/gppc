from django.db import models
import datetime
from django.utils.dateformat import format
from django.conf import settings
import re
import unidecode

import os

def content_file_name(instance, filename):
    ext = filename.split('.')[-1]

    temp = filename.replace('.' + ext, '')

    if not re.match('^[a-zA-Z0-9-]+$', temp):
        unaccented_string = unidecode.unidecode(temp)
        temp = re.sub('(?![a-zA-Z0-9-]).', '-', unaccented_string)
    
    date = format(instance.date, "Y-m-d")

    filename = date + "-" + instance.firstname + "-" + instance.name + "-" + temp + '.' + ext

    setFilename(instance, filename)

    return os.path.join('uploads/', filename)
    
def setFilename(instance, value):
    instance.filename = value

# Create your models here.
class ContactData(models.Model):
    
    date = models.DateField()
    name = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 100)
    building = models.CharField(max_length = 100)
    office = models.CharField(max_length = 100)
    delivery = models.DateField(null = True)
    upload = models.FileField(upload_to=content_file_name)
    filename = models.CharField(max_length = 200, null = True)
    format = models.CharField(max_length = 100)
    formatHeight = models.FloatField(null = True)
    formatWidth = models.FloatField(null = True)
    comments = models.CharField(max_length = 1000)
    # Définition du nom de l'objet dans l'interface admin de django
    def __str__(self):
        return self.upload.name.replace('uploads/', '')
    

