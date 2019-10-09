from django.contrib.auth.models import User
from rest_framework import routers, serializers, viewsets
from .models import Usuario

class UsuarioSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Usuario
        fields = ['id', 'nome']

