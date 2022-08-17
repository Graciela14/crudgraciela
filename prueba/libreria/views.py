from django.shortcuts import render, redirect
from .forms import datosform
from .models import datos


def inicio(request):
    return render(request, 'paginas/inicio.html')


def info(request):
    variable = datos.objects.all()
    return render(request, 'Datos/index.html', {'variable': variable})


def ingreso (request):
    formulario = datosform(request.POST or None, request.FILES or None)
    if formulario.is_valid():
        formulario.save()
        return redirect('index')
    return render(request, 'Datos/crear.html', {'formulario': formulario})


def modificar(request, id):
    variable2 = datos.objects.get(id=id)
    formulario = datosform(request.POST or None, request.FILES or None, instance=variable2)
    if formulario.is_valid() and request.method == 'POST':
        formulario.save()
        return redirect('index')
    return render(request, 'Datos/modificar.html', {'formulario': formulario})


def form(request):
    return render(request, 'Datos/form.html')


def eliminar(request, id):
    variable2 = datos.objects.get(id=id)
    variable2.delete()
    return redirect('index')