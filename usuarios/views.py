from django.shortcuts import render, redirect, get_object_or_404
from.models import Usuario
from.forms import UsuarioForm
from rest_framework import viewsets
from .serializers import UsuarioSerializer

# Create your views here.

class UsuarioViewSet(viewsets.ModelViewSet):
    queryset = Usuario.objects.all()
    serializer_class = UsuarioSerializer

def lista_usuario(request):
    usuarios = Usuario.objects.all()
    return render(request,'index.html', {'usuarios': usuarios})

def criar_usuario(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_usuario')

    return render(request, 'usuarios-form.html', {'form': form})

def atualiza_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)
    form = UsuarioForm(request.POST or None, instance=usuario)

    if form.is_valid():
        form.save()
        return redirect('lista_usuario')

    return render(request, 'usuarios-form.html', {'form': form})

def deletar_usuario(request, id):
    usuario = get_object_or_404(Usuario, pk=id)

    if request.method == 'POST':
        usuario.delete()
        return redirect('lista_usuario')

    return render(request, 'confirm_delete.html', {'usuario': usuario})
