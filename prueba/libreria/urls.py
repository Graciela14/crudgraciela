from django.urls import path
from . import views

urlpatterns = [
    path('', views.info, name='index'),
    path('crear', views.ingreso, name='crear'),
    path('modificar/<int:id>', views.modificar, name='modificar'),
    path('form', views.form, name='form'),
    path('eliminar/<int:id>', views.eliminar, name='eliminar'),
]