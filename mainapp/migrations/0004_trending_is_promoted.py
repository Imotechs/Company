# Generated by Django 4.0.1 on 2022-04-14 12:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_remove_trending_quarter_trending_first_quarter_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='trending',
            name='is_promoted',
            field=models.BooleanField(default=False),
        ),
    ]