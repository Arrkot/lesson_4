# Generated by Django 4.2.3 on 2023-07-28 16:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app_advertisements', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='advertisements',
            name='uuu',
            field=models.CharField(default='', max_length=22, verbose_name='uuu'),
        ),
        migrations.AlterModelTable(
            name='advertisements',
            table='Advertisements',
        ),
    ]
