from django.db import models

# Create your models here.

class ciudad(models.Model):
    ciudades = [
        ('BARRANQUILLLA','Barranquilla'),
        ('CALI','Cali'),
        ('CARTAGENA','Cartagena')
    ]
    nombre = models.CharField(max_length=140,choices=ciudades,default='BARRANQUILLLA')

    def __str__(self):
        return self.nombre

class hotel(models.Model):
    nombre = models.CharField(max_length=140)
    ciudad = models.ForeignKey(ciudad,on_delete=models.CASCADE,related_name="ciudades")
    numHabitaciones = models.PositiveIntegerField()
    numMaximoPersonas = models.PositiveIntegerField(default=100)

    
    def __str__(self):  
        return u"%s %s" % (self.nombre, self.ciudad)





class Habitaciones(models.Model):
    tipo = [
        ('ESTANDAR','Estandar'),
        ('PREMIUM','Premium'),
        ('VIP','Vip')
    ]
    hotel = models.ForeignKey(hotel,on_delete=models.CASCADE,related_name="hoteles",blank=True, null=True)

    tipo = models.CharField(max_length=150, choices=tipo,default='ESTANDAR')
    capacidad = models.IntegerField()
    precio = models.IntegerField() 

    def __str__(self):  
        return u"%s %s" % (self.hotel, self.tipo)

