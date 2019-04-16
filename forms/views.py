from django.shortcuts import render
from django.http import HttpResponse
from .form import ContactForm

def index(request):
    return render(request, 'forms/index.html')

def test(request):
    form = ContactForm(request.POST or None)
    if form.is_valid():
        # Ici nous pouvons traiter les données du formulaire
        sujet = form.cleaned_data['sujet']
        message = form.cleaned_data['message']
        envoyeur = form.cleaned_data['envoyeur']
        renvoi = form.cleaned_data['renvoi']

        # Nous pourrions ici envoyer l'e-mail grâce aux données
        # que nous venons de récupérer
        envoi = True

    return render(request, 'forms/gppc-form.html', locals())