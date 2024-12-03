# Generated by Django 5.1.3 on 2024-12-03 14:39

from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Niveles",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("puntaje_min", models.IntegerField(unique=True)),
                ("puntaje_max", models.IntegerField(unique=True)),
            ],
        ),
    ]