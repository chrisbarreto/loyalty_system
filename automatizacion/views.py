from django.shortcuts import render
from bolsaPuntos.models import BolsaPuntos
import schedule
import time
from datetime import date

# Create your views here.

def controlarBolsas():
    bolsas=BolsaPuntos.objects.all()
    fecha_hoy=date.today()

    for bolsa in bolsas:
        if bolsa.fecha_caducidad>fecha_hoy:
           # BolsaPuntos.objects.filter(id=bolsa.pk).delete()
            print(bolsa)

def arrancar(request):
    schedule.every().day.at("20:11").do(controlarBolsas)

    opcion=input("1 para arrancar: ")

    while opcion:
        schedule.run_pending()
        time.sleep(1)