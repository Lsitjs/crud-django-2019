from django.shortcuts import render, redirect
from.models import Usuario
from.forms import UsuarioForm

# Create your views here.
def lista_usuario(request):
    usuarios = Usuario.objects.all()
    return render(request,'index.html', {'usuarios': usuarios})

def criar_usuario(request):
    form = UsuarioForm(request.POST or None)

    if form.is_valid():
        form.save()
        return redirect('lista_usuario')

    return render(request, 'usuarios-form.html', {'form': form})