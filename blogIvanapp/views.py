from django.shortcuts import render,HttpResponse
from .forms import fmrContacto
from django.core.mail import send_mail

# Create your views here.

def Inicio(request):
    return render(request, 'blogIvanapp/homme.html')



def Videos(request):
    return render(request, 'blogIvanapp/videos.html')


def Eventos(request):
    
            return render(request, 'blogIvanapp/eventos.html')

def Contacto(request):

    if request.method == 'POST':


        fmr=fmrContacto(request.POST)
        if fmr.is_valid():
            datos=fmr.cleaned_data
            
            send_mail(datos['asunto'],datos['mensaje'],datos.get('email',''),['25592df92a-159f03+1@inbox.mailtrap.io','fjai867@gmail.com'],)
            
            return render(request, 'blogIvanapp/gracias.html')

    else:
        fmr=fmrContacto()
        return render(request, 'blogIvanapp/contacto.html',{"fmr":fmr})

