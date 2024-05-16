# Generated by Django 3.2.8 on 2024-05-15 20:59

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clinica', '0004_alter_person_number_doc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='number_doc',
            field=models.CharField(max_length=20, validators=[django.core.validators.RegexValidator(message='Solo se permiten números', regex='^[0-9]*$')], verbose_name='Número de documento persona'),
        ),
    ]