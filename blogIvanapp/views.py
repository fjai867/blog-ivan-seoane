from django.shortcuts import render,HttpResponse
from .forms import fmrContacto
from django.core.mail import send_mail, EmailMessage

# Create your views here.

def Inicio(request):
    return render(request, 'blogIvanapp/homme.html')

def Contacto(request):

    if request.method == 'POST':


        fmr=fmrContacto(request.POST)
        if fmr.is_valid():
            datos=fmr.cleaned_data
            
            #send_mail(datos['asunto'],datos['mensaje'],datos.get('email',''),['25592df92a-159f03+1@inbox.mailtrap.io','fjai867@gmail.com'],)

            emailPaco=EmailMessage(
                 datos['asunto'],
                 datos['mensaje'],
                 datos['email'],
                 ['fjai867@gmail.com'],
                 reply_to=['fjai867@gmx.es'],
                
            )

            emailPaco.send()
            
            return render(request, 'blogIvanapp/gracias.html')

    else:
        fmr=fmrContacto()
        return render(request, 'blogIvanapp/contacto.html',{"fmr":fmr})

