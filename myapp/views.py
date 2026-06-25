from django.shortcuts import render
from .models import Cliente, Reparacion, Equipo, Tecnico


# Create your views here.
def index(request):
    context = {"mensaje":"Ofrecemos servicios de reparación de computadoras, mantenimiento y soporte técnico."}
    return render(request,"myapp/index.html",context)

def clientes(request):
    clientes = clientes.objects.all()
    return render (request, "myapp/clientes.hmtl", {"clientes": clientes})

def equipos(request):
    equipos = equipos.objects.all()
    return render (request, "myapp/equipos.hmtl", {"equipos": equipos})




