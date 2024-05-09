# Generated by Django 4.2.12 on 2024-05-09 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Borrows",
            fields=[
                (
                    "code_borrow",
                    models.CharField(max_length=12, primary_key=True, serialize=False),
                ),
                ("name_borrow", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "borrows",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Causecare",
            fields=[
                (
                    "id_care",
                    models.CharField(max_length=2, primary_key=True, serialize=False),
                ),
                ("type_care", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "causecare",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Countries",
            fields=[
                (
                    "alfa_3",
                    models.CharField(max_length=3, primary_key=True, serialize=False),
                ),
                ("name_country", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "countries",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Disability",
            fields=[
                (
                    "id_dis",
                    models.CharField(max_length=2, primary_key=True, serialize=False),
                ),
                ("name_dis", models.CharField(max_length=50)),
            ],
            options={
                "db_table": "disability",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Entrys",
            fields=[
                (
                    "id_type_entrys",
                    models.CharField(max_length=2, primary_key=True, serialize=False),
                ),
                ("entrys_names", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "entrys",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Eps",
            fields=[
                (
                    "code_eps",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("name_eps", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "eps",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Ethnicity",
            fields=[
                (
                    "id_et",
                    models.CharField(max_length=2, primary_key=True, serialize=False),
                ),
                ("name_ethn", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "ethnicity",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Illnesses",
            fields=[
                (
                    "cod_4",
                    models.CharField(max_length=4, primary_key=True, serialize=False),
                ),
                ("des_illness", models.CharField(max_length=400)),
            ],
            options={
                "db_table": "illnesses",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Modality",
            fields=[
                (
                    "id_typemod",
                    models.CharField(max_length=2, primary_key=True, serialize=False),
                ),
                ("description_modality", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "modality",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Municipalities",
            fields=[
                ("departament", models.CharField(max_length=200)),
                (
                    "code_dep",
                    models.CharField(max_length=5, primary_key=True, serialize=False),
                ),
                ("name_dep", models.CharField(max_length=200)),
                ("type_mnc", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "municipalities",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Occupations",
            fields=[
                (
                    "code_occ",
                    models.CharField(max_length=4, primary_key=True, serialize=False),
                ),
                ("name_occ", models.CharField(max_length=200)),
            ],
            options={
                "db_table": "occupations",
                "managed": False,
            },
        ),
        migrations.CreateModel(
            name="Typesdocs",
            fields=[
                (
                    "id_typedoc",
                    models.CharField(max_length=2, primary_key=True, serialize=False),
                ),
                ("doc_type", models.CharField(max_length=100)),
            ],
            options={
                "db_table": "typesdocs",
                "managed": False,
            },
        ),
    ]
