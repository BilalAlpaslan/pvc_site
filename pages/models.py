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

class Hakkında(models.Model):
    baslık = models.CharField(max_length=100, verbose_name='Başlık')
    icerik = RichTextField()