from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Reparacion, Equipo, Tecnico
from .forms import ClientesFormulario, ClientesFilter, TecnicoForm, EquipoForm, ReparacionForm
from django.db import models
from django.contrib.auth.decorators import login_required #nuevo


# Create your views here.
def index(request):
    context = {"mensaje": "Ofrecemos servicios de reparación de computadoras, mantenimiento y soporte técnico."}
    return render(request, "myapp/index.html", context)

@login_required #nuevo
def clientes(request):
    query = request.GET.get('q')  # Captura lo que se escribe en el buscador
    if query:
        clientes = Cliente.objects.filter(
            models.Q(nombre__icontains=query) |
            models.Q(apellido__icontains=query) |
            models.Q(email__icontains=query)
        )
    else:
        clientes = Cliente.objects.all()


    return render(request, 'myapp/clientes.html', {
        'clientes': clientes,
        'query': query,
    })


@login_required
def equipos(request):
    equipos = Equipo.objects.all()
    return render(request, "myapp/equipos.html", {"equipos": equipos})

@login_required
def editar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)

    if request.method == 'POST':
        form = EquipoForm(request.POST, instance=equipo)
        if form.is_valid():
            form.save()
            return redirect('myapp:equipos')
    else:
        form = EquipoForm(instance=equipo)

    return render(request, 'myapp/editar_equipo.html', {
        'form': form,
        'equipo': equipo
    })

@login_required
def eliminar_equipo(request, id):
    equipo = get_object_or_404(Equipo, id=id)

    if request.method == 'POST':
        equipo.delete()
        return redirect('myapp:equipos')

    return redirect('myapp:equipos')

@login_required
def tecnicos(request):
    tecnicos = Tecnico.objects.all()
    return render(request, "myapp/tecnicos.html", {"tecnicos": tecnicos})

@login_required
def reparacion(request):
    reparacion = Reparacion.objects.all()
    return render(request, "myapp/reparacion.html", {"reparacion": reparacion})

@login_required
def editar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)

    if request.method == 'POST':
        form = ReparacionForm(request.POST, instance=reparacion)
        if form.is_valid():
            form.save()
            return redirect('myapp:reparacion')
    else:
        form = ReparacionForm(instance=reparacion)

    return render(request, 'myapp/editar_reparacion.html', {
        'form': form,
        'reparacion': reparacion
    })

@login_required
def eliminar_reparacion(request, id):
    reparacion = get_object_or_404(Reparacion, id=id)

    if request.method == 'POST':
        reparacion.delete()
        return redirect('myapp:reparacion')

    return redirect('myapp:reparacion')

def agregar_cliente(request):
    if request.method == 'POST':
        form = ClientesFormulario(request.POST)
        if form.is_valid():
            nombre = form.cleaned_data['nombre']
            apellido = form.cleaned_data['apellido']
            telefono = form.cleaned_data['telefono']
            email = form.cleaned_data['email']
            direccion = form.cleaned_data['direccion']
            cliente = Cliente(nombre=nombre, apellido=apellido, telefono=telefono, email=email, direccion=direccion)
            cliente.save()
            return redirect('myapp:clientes')
    else:
        form = ClientesFormulario()
    return render(request, 'myapp/agregar_cliente.html', {'form': form})

def editar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)
   
    if request.method == 'POST':
        form = ClientesFilter(request.POST, instance=cliente)
        if form.is_valid():
            form.save()
            return redirect('myapp:clientes')
    else:
        form = ClientesFilter(instance=cliente)
   
    return render(request, 'myapp/editar_clientes.html', {'form': form, 'cliente': cliente})

@login_required
def editar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)

    if request.method == 'POST':
        form = TecnicoForm(request.POST, instance=tecnico)
        if form.is_valid():
            form.save()
            return redirect('myapp:tecnicos')
    else:
        form = TecnicoForm(instance=tecnico)

    return render(request, 'myapp/editar_tecnico.html', {
        'form': form,
        'tecnico': tecnico
    })

@login_required
def eliminar_tecnico(request, id):
    tecnico = get_object_or_404(Tecnico, id=id)

    if request.method == 'POST':
        tecnico.delete()
        return redirect('myapp:tecnicos')

    return redirect('myapp:tecnicos')

def eliminar_cliente(request, id):
    cliente = get_object_or_404(Cliente, id=id)

    if request.method == 'POST':
        cliente.delete()
        return redirect('myapp:clientes')
    return render(request, 'myapp/clientes.html', {'cliente': cliente})

def contactos(request):
    tecnicos = Tecnico.objects.all()
    return render(request,"myapp/contactos.html", {'tecnicos': tecnicos})

def chatbot(request):
    return render(request, "myapp/chatbot.html")



