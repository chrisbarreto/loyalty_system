# Generated by Django 5.1.3 on 2024-12-04 02:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bolsaPuntos', '0002_alter_bolsapuntos_saldo_puntos'),
    ]

    operations = [
        migrations.AddField(
            model_name='bolsapuntos',
            name='metodo_pago',
            field=models.CharField(choices=[('Efectivo', 'Efectivo'), ('Web', 'Web'), ('Tarjeta de Crédito', 'Tarjeta de Crédito'), ('App Móvil', 'App Móvil')], default='Efectivo', max_length=50),
        ),
    ]
