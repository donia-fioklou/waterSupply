# Generated by Django 4.0.4 on 2023-01-18 22:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0007_alter_provisioneau_distributeur'),
    ]

    operations = [
        migrations.AlterField(
            model_name='provisioneau',
            name='date_prov',
            field=models.DateField(auto_now_add=True),
        ),
    ]
