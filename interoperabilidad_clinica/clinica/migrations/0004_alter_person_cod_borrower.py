# Generated by Django 4.2.12 on 2024-05-11 14:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("clinica", "0003_alter_person_id_history"),
    ]

    operations = [
        migrations.AlterField(
            model_name="person",
            name="cod_borrower",
            field=models.CharField(default="000000000000", max_length=12),
        ),
    ]
