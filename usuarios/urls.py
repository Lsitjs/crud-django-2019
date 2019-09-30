from django.urls import path, include
from.views import lista_usuario, criar_usuario

urlpatterns = [
    path('', lista_usuario, name='lista_usuario'),
    path('new/', criar_usuario, name='criar_usuario'),

]