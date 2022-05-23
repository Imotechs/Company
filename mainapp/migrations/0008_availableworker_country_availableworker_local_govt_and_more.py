# Generated by Django 4.0.1 on 2022-05-01 21:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0007_shares_available'),
    ]

    operations = [
        migrations.AddField(
            model_name='availableworker',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='availableworker',
            name='local_govt',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='availableworker',
            name='state',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='availableworker',
            name='type_of_work',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='availableworker',
            name='upfront',
            field=models.CharField(blank=True, max_length=30),
        ),
    ]