from django.db import models
import datetime
from django.utils.dateformat import format
from django.conf import settings

# Create your models here.
class ContactData(models.Model):
    name = models.CharField(max_length = 100)
    firstname = models.CharField(max_length = 100)
    email = models.EmailField()
    phone = models.CharField(max_length = 100)
    building = models.CharField(max_length = 100)
    office = models.CharField(max_length = 100)
    upload = models.FileField()
    format = models.CharField(max_length = 100)
    formatHeight = models.FloatField(null=True)
    formatWidth = models.FloatField(null=True)
    comments = models.CharField(max_length = 1000)
    date = models.DateField(default = datetime.date.today)
    # Définition de la représentation de l'objet dans l'interface admin de django
    def __str__(self):
        todayDate = format(self.date, settings.DATE_INPUT_FORMATS)
        return self.name + "-" + self.firstname + "-" + todayDate