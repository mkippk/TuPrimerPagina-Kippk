from django.urls import path
from inicio.views import inicio, crear_producto, buscar_producto


urlpatterns = [
    path('', inicio, name="inicio"),
    path('agregar-producto', crear_producto, name="agregar-producto"),
    path('home', inicio, name="home"),
    path('buscar-producto', buscar_producto, name='buscar-producto')

]