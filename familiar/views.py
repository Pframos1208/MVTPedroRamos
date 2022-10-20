from django.shortcuts import render

from .models import Familiar
from django.http import HttpResponse
from datetime import datetime


# Create your views here.



def agregar_familiar(request, nombre, apellido, edad, fecha):
    
        familiarguardar = Familiar(nombre = nombre, apellido = apellido, edad = edad)
        DOB = datetime.strptime(fecha, '%d-%m-%Y').date()
        familiarguardar.DOB = DOB
        familiarguardar.save()
        #raise TypeError("Only integers are allowed")
        return HttpResponse(
            f"""<p>Nombre: {familiarguardar.nombre} {familiarguardar.apellido} - agregado correctamente"""
        )
    

def listar_familiar(request):
    
    lista = Familiar.objects.all()
    
    return render(request, 'familia.html', {'lista_familiares':lista})