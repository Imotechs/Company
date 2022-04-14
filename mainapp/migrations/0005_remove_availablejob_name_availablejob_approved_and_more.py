# Generated by Django 4.0.1 on 2022-04-14 12:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('mainapp', '0004_trending_is_promoted'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='availablejob',
            name='name',
        ),
        migrations.AddField(
            model_name='availablejob',
            name='approved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='availablejob',
            name='photo',
            field=models.ImageField(default='media/Jobs/default.jpg', upload_to='media/Jobs'),
        ),
        migrations.AddField(
            model_name='availablejob',
            name='type_of_work',
            field=models.CharField(blank=True, max_length=30),
        ),
        migrations.AddField(
            model_name='availablejob',
            name='user',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='availablejob',
            name='country',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='availablejob',
            name='local_govt',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='availablejob',
            name='state',
            field=models.CharField(blank=True, max_length=20),
        ),
    ]