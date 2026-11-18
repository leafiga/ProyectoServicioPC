from django.urls import path
from . import views

app_name = "myapp"

urlpatterns = [
    path('', views.index, name='index'),
    path('clientes/', views.clientes, name = 'clientes'),
    path('equipos/', views.equipos, name='equipos'),
    path('agregar_equipo/', views.agregar_equipo, name='agregar_equipo'),
    path('equipo/editar/<int:id>/', views.editar_equipo, name='editar_equipo'),
    path('equipo/eliminar/<int:id>/', views.eliminar_equipo, name='eliminar_equipo'),
    path('tecnicos/', views.tecnicos, name='tecnicos'),
    path('agregar_tecnico/', views.agregar_tecnico, name='agregar_tecnico'),
    path('reparacion/', views.reparacion, name='reparacion'),
    path('agregar_reparacion/', views.agregar_reparacion, name='agregar_reparacion'),
    path('reparacion/editar/<int:id>/', views.editar_reparacion, name='editar_reparacion'),
    path('reparacion/eliminar/<int:id>/', views.eliminar_reparacion, name='eliminar_reparacion'),
    path('agregar_cliente/', views.agregar_cliente, name='agregar_cliente'),
    path('cliente/editar/<int:id>/', views.editar_cliente, name='editar_cliente'),
    path('tecnico/editar/<int:id>/', views.editar_tecnico, name='editar_tecnico'),
    path('tecnico/eliminar/<int:id>/', views.eliminar_tecnico, name='eliminar_tecnico'),
    path('cliente/eliminar/<int:id>/', views.eliminar_cliente, name='eliminar_cliente'),
    path('contactos/', views.contactos, name='contactos'),
    path('chatbot/', views.chatbot, name='chatbot'),


]