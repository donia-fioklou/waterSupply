# Generated by Django 4.0.4 on 2023-01-10 22:56

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='distributeur',
            name='contact',
            field=models.CharField(max_length=8),
        ),
    ]
