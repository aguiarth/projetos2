# Generated by Django 5.0.3 on 2024-04-25 15:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('apps', '0027_merge_0025_merge_20240425_1028_0026_usercliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cafe',
            name='whatsapp',
            field=models.CharField(default='5500000000000', max_length=13),
        ),
    ]