from django.shortcuts import render,get_object_or_404
from .models import Sistem,İletisim,Hakkında


def index(request):
    return render(request, 'pages/index.html')

def about(request):
    context = {
        'hakkında': Hakkında.objects.first()
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    context = {
        'iletisim': İletisim.objects.first()
    }
    return render(request, 'pages/contact.html', context)

def catalog(request):
    return render(request, 'pages/catalog.html')

def proje(request):
    return render(request, 'pages/proje.html')

def sistem(request, sistem_url):
    sistem = get_object_or_404(Sistem, sistem_url = sistem_url)
    context = {
            'sistem': sistem
        }
    return render(request, 'pages/sistem.html', context)