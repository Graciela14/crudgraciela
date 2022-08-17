from django.db import models

# Create your models here.
class datos (models.Model):
    objects = None
    id = models.AutoField(primary_key=True)
    nombre = models.CharField(max_length=100, verbose_name='nombre')
    apellido = models.CharField(max_length=100, verbose_name='Apellido')
    telefono = models.CharField(max_length=100, verbose_name='Telefono')

def delete(self, using=None, keep_parents=False):
    self.imagen.storage.delete(self.imagen.name)
    super().delete()





