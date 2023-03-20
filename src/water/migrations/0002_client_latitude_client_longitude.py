# Generated by Django 4.1.4 on 2023-03-14 11:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('water', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='client',
            name='latitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
        migrations.AddField(
            model_name='client',
            name='longitude',
            field=models.DecimalField(decimal_places=6, max_digits=9, null=True),
        ),
    ]
