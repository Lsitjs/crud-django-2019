from django.urls import path, include
from.views import lista_usuario, criar_usuario, atualiza_usuario, deletar_usuario

urlpatterns = [
    path('', lista_usuario, name='lista_usuario'),
    path('new/', criar_usuario, name='criar_usuario'),
    path('update/<int:id>', atualiza_usuario, name='atualiza_usuario'),
    path('delete/<int:id>', deletar_usuario, name='deletar_usuario'),

]