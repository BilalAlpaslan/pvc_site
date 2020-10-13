from django.shortcuts import render,get_object_or_404
from .models import Sistem,İletisim,Hakkında,Musteri,Anasayfa,Proje,Katalog




def index(request):
    context={
        'iletisim': İletisim.objects.first(),
        'sistemler': Sistem.objects.all(),
        'müsteriler': Musteri.objects.all(),
        'anasayfa': Anasayfa.objects.first(),
    }
    return render(request, 'pages/index.html', context)

def about(request):
    context={
        'iletisim': İletisim.objects.first(),
        'sistemler':Sistem.objects.all(),
        'hakkında': Hakkında.objects.first(),
        'müsteriler':Musteri.objects.all(),
    }
    return render(request, 'pages/about.html', context)

def contact(request):
    context={
        'iletisim': İletisim.objects.first(),
        'sistemler':Sistem.objects.all(),
    }
    return render(request, 'pages/contact.html', context)

def catalog(request):
    context={
        'iletisim': İletisim.objects.first(),
        'sistemler':Sistem.objects.all(),
        'katalog' : Katalog.objects.all(),
    }
    return render(request, 'pages/catalog.html', context)

def proje(request):
    context={
        'iletisim': İletisim.objects.first(),
        'sistemler':Sistem.objects.all(),
        'proje1':Proje.objects.filter(tür=1),
        'proje2':Proje.objects.filter(tür=2),
        'proje3':Proje.objects.filter(tür=3),
    }
    return render(request, 'pages/proje.html', context)

def sistem(request, sistem_url):
    sistem = get_object_or_404(Sistem, sistem_url = sistem_url)
    context={
        'iletisim': İletisim.objects.first(),
        'sistemler':Sistem.objects.all(),
        'sistem': sistem,
    }
    return render(request, 'pages/sistem.html', context)