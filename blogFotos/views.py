from django.shortcuts import render
from .models import Post

# Create your views here.

def Fotos(request):
     posts=Post.objects.all()
     return render(request, 'blogFotos/fotos.html',{'posts':posts})
