from django.shortcuts import render
from .models import videos


# Create your views here.
def Videos(request):
    video=videos.objects.all()
    return render(request, 'videos/videos.html',{'video':video})
    

