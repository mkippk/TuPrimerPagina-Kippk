from django.shortcuts import render
from django.template import Template, Context, loader
from django.http import HttpResponse
from inicio.models import Productos
from inicio.forms import ProductoBusquedaFormulario, ProdcutoFormulario


# Create your views here.

def inicio(request):
    return render(request, r'inicio\inicio.html')




def crear_producto(request):
    print(request.POST)
    #print(request.POST)

    if request.method =='POST':
        formulario = ProdcutoFormulario(request.POST)
        if formulario.is_valid():
            data = formulario.cleaned_data
            producto = Productos(Producto=data.get('Producto'), Descripcion=data.get('Descripcion'), Precio=data.get('Precio'))
            producto.save()
        else:
            return render(request, r'inicio\agregar-producto.html', {'formulario': formulario})
    
    return render(request, r'inicio\agregar-producto.html')


def buscar_producto(request):
    formulario = ProductoBusquedaFormulario(request.GET)
    if formulario.is_valid():
        producto_a_buscar = formulario.cleaned_data.get('Producto')
        
        producto_encontrado = Productos.objects.filter(Producto__icontains=producto_a_buscar)
        print(producto_encontrado)
    else:
        producto_encontrado = Productos.objects.all()

    formulario = ProductoBusquedaFormulario()
    return render(request, r'inicio\buscar-producto.html', {'formulario': formulario, 'producto_encontrado': producto_encontrado})

