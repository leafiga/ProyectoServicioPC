from django import forms

from .models import Cliente, Tecnico, Equipo, Reparacion


class ClientesFormulario(forms.Form):

    nombre = forms.CharField(max_length=100, label="Nombre")

    apellido = forms.CharField(max_length=100, label="Apellido")

    telefono = forms.CharField(max_length=20, label="Teléfono")

    email = forms.EmailField(label="Correo Electrónico")

    direccion = forms.CharField(max_length=200, label="Dirección")


class ClientesFilter(forms.ModelForm):

    class Meta:

        model = Cliente

        fields = ['nombre', 'apellido', 'telefono', 'email']



class TecnicoForm(forms.ModelForm):

    class Meta:
        model = Tecnico
        fields = ['nombre', 'apellido', 'telefono', 'especialidad']




class EquipoForm(forms.ModelForm):
    class Meta:
        model = Equipo
        fields = [
            'cliente',
            'tipo',
            'marca',
            'modelo',
            'numero_serie',
            'observaciones'
        ]

class ReparacionForm(forms.ModelForm):
    class Meta:
        model = Reparacion
        fields = [
            'equipo',
            'tecnico',
            'fecha_ingreso',
            'fecha_entrega',
            'problema_reportado',
            'diagnostico',
            'solucion',
            'costo',
            'estado'
        ]

        