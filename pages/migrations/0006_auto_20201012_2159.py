# Generated by Django 3.1.2 on 2020-10-12 18:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_i̇letisim_harita'),
    ]

    operations = [
        migrations.AlterField(
            model_name='i̇letisim',
            name='harita',
            field=models.CharField(max_length=300, verbose_name='harita'),
        ),
    ]
