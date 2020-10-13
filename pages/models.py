from django.db import models
from ckeditor.fields import RichTextField

class Sistem(models.Model):
    sistem_url = models.CharField(max_length=100, verbose_name='url')
    baslık = models.CharField(max_length=100, verbose_name='Başlık')
    icerik = RichTextField()
    image1 = models.FileField(blank = True,null = True, verbose_name='Resim1')
    image2 = models.FileField(blank = True,null = True, verbose_name='Resim2')
    image3 = models.FileField(blank = True,null = True, verbose_name='Resim3')

    def __str__(self):
        return self.baslık
 
class İletisim(models.Model):
    adres = models.CharField(max_length=100, verbose_name='adres')
    telefon = models.CharField(max_length=100, verbose_name='telefon')
    mail = models.CharField(max_length=100, verbose_name='mail')
    harita = models.CharField(max_length=300, verbose_name='harita')

class Hakkında(models.Model):
    baslık = models.CharField(max_length=100, verbose_name='Başlık')
    icerik = RichTextField()
    image1 = models.FileField(blank = True,null = True, verbose_name='Resim1')
    image2 = models.FileField(blank = True,null = True, verbose_name='Resim2')
    image3 = models.FileField(blank = True,null = True, verbose_name='Resim3')

class Musteri(models.Model):
    isim = models.CharField(max_length=100, verbose_name='isim')
    image = models.FileField(blank = True,null = True, verbose_name='Resim')

    def __str__(self):
        return self.isim

class Anasayfa(models.Model):
    anabaşlık = models.CharField(max_length=100, verbose_name='anabaşlık')
    altbaşlık = models.CharField(max_length=100, verbose_name='altbaşlık')
    paragraf = RichTextField()
    image = models.FileField(blank = True,null = True, verbose_name='Resim')

class Proje(models.Model):
    başlık = models.CharField(max_length=100,verbose_name='başlık')
    icerik = RichTextField()
    resim = models.FileField(blank=True,null=True,verbose_name='resim')
    tür = models.CharField(choices=[
        ("1" , "bitti"),
        ("2" , "devam ediyor"),
        ("3" , "anlaşıldı"),
    ],default=1,max_length=2)

    def __str__(self):
        return self.başlık


class Katalog(models.Model):
    yazı = models.CharField(max_length=100,verbose_name="yazı")
    resim = models.FileField(blank=True,null=True,verbose_name="resim")

    def __str__(self):
        return self.yazı