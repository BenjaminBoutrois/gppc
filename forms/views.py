from django.shortcuts import render
from django.http import HttpResponse
from .form import ContactForm
from .choices import *
from django.utils.dateformat import format
from forms.models import ContactData
import datetime
from django.conf import settings
import string
from django.core.mail import send_mail
from django.template.loader import render_to_string

def index(request):
    return render(request, 'forms/index.html')

def gppc(request):
    if request.POST:
        form = ContactForm(request.POST, request.FILES)
        if form.is_valid():
            # Traitement des données
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

            # Envoi mail acquittement
            msg_plain = render_to_string('../templates/emails/gppc-acknowledgement.txt', {'data': newData})

            send_mail(
                '[GeePs Posters] poster printing request – Demande d’impression poster',
                msg_plain,
                'test.django.mailing@gmail.com',
                [newData.email],
            )

            # Envoi mail demande CRI
            msg_plain = render_to_string('../templates/emails/gppc-demand.txt', {'data': newData})

            send_mail(
                '[GeePs Posters] Demande d’impression poster',
                msg_plain,
                'test.django.mailing@gmail.com',
                ['poster@geeps.centralesupelec.fr'],
            )
    else:
        form = ContactForm()

    return render(request, 'forms/gppc-form.html', locals())

def history_gppc(request):
    demands = list(ContactData.objects.all())
    return render(request, 'forms/gppc-history.html', {'demands': demands})
