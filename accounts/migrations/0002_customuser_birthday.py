# Generated by Django 4.2.7 on 2023-11-13 13:08

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='birthday',
            field=models.DateField(default=django.utils.timezone.now, verbose_name='birthday'),
            preserve_default=False,
        ),
    ]
