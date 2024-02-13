from django.db import models

class CatalogsTypesDishes(models.Model):
    tipe = models.CharField(max_length=200, null=False, blank=False)

    def __str__(self): 
        return  self.tipe
    
class Dishes(models.Model):
    dishes = models.ForeignKey(CatalogsTypesDishes, on_delete=models.CASCADE, verbose_name='Tipo de plato')
    nombre = models.CharField( max_length=50, verbose_name='nombre')
    description = models.CharField(max_length=400, null=True, blank=True)
    costo = models.DecimalField(max_digits= 25, decimal_places=0, default=0)

    def __str__(self): 
        return  self.nombre