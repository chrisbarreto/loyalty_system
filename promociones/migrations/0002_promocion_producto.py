# Generated by Django 5.1.3 on 2024-12-03 20:40

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("promociones", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="promocion",
            name="producto",
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
    ]
