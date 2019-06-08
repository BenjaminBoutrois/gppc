from django.shortcuts import render
from django.http import HttpResponse
from .form import ContactForm
from .choices import *
from django.utils.dateformat import format
from forms.models import ContactData
import datetime
from django.conf import settings
import string

def index(request):
    return render(request, 'forms/index.html')

def gppc(request):
    if request.POST:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # Ici nous pouvons traiter les données du formulaire
            rDate = form.cleaned_data['date']
            rName = form.cleaned_data['name']
            rFirstname = form.cleaned_data['firstname']
            rEmail = form.cleaned_data['email']
            rPhone = form.cleaned_data['phone']
            buildingDict = dict(BUILDING_CHOICES)
            rBuilding = buildingDict[int(form.cleaned_data['building'])]
            rOffice = form.cleaned_data['office']
            rDelivery = form.cleaned_data['delivery']
            rUpload = form.cleaned_data['upload']
            formatDict = dict(FORMAT_CHOICES)
            rFormat = formatDict[int(form.cleaned_data['format'])]
            rFormatHeight = form.cleaned_data['formatHeight']
            rFormatWidth = form.cleaned_data['formatWidth']
            rComments = form.cleaned_data['comments']

            newData = ContactData(
                date = rDate,
                name = rName,
                firstname = rFirstname,
                email = rEmail,
                phone = rPhone,
                building = rBuilding,
                office = rOffice,
                delivery = rDelivery,
                upload = rUpload,
                filename = None,
                format = rFormat,
                formatHeight = rFormatHeight,
                formatWidth = rFormatWidth,
                comments = rComments
            )
            
            newData.save()

            # Nous pourrions ici envoyer l'e-mail grâce aux données
            # que nous venons de récupérer
            envoi = True
    else:
        form = ContactForm()

    return render(request, 'forms/gppc-form.html', locals())

def history_gppc(request):
    demands = list(ContactData.objects.all())
    return render(request, 'forms/gppc-history.html', {'demands': demands})
