from django.db import models
from django.utils import timezone
from django.conf import settings
from django.utils.html import mark_safe

class Marca(models.Model):
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    nombre = models.CharField(max_length=200)
    descripcion = models.TextField()
    imagen_de_marca = models.ImageField(upload_to='images/')

    SILICON = "Silicona"
    THERMO = "Termoplástico"
    NO_RESULTS = "No hay información"

    MATERIALS = (('Silicona', SILICON), ('Termoplástico', THERMO),  ('No hay información', NO_RESULTS))

    material = models.CharField(max_length=20, choices=MATERIALS)
    origen = models.CharField(max_length=200)

    STRONG = 'Fuerte'
    MEDIUM = 'Media'
    MEDIUMF = 'Media a fuerte'
    WEAK = 'Blanda'

    STATUS = (('Fuerte', STRONG), ('Media a Fuerte', MEDIUMF),  ('Media', MEDIUM), ('Blanda', WEAK))

    rigidez_cuerpo = models.CharField(max_length=20, choices=STATUS)
    rigidez_anillo = models.CharField(max_length=20, choices=STATUS)

    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)


    def modified(self):
        self.fecha_modificacion = timezone.now()
        self.save()

    def __str__(self):
        return self.nombre


class Producto(models.Model):
    marca = models.ForeignKey(Marca, on_delete=models.CASCADE)
    autor = models.ForeignKey('auth.User', on_delete=models.CASCADE)
    descripcion = models.TextField( blank=True, null=True)

    talle = models.CharField(max_length=10)
    ancho = models.CharField(max_length=10)
    altura_con_cabito = models.CharField(max_length=10)
    altura_sin_cabito = models.CharField(max_length=10, blank=True, null=True)

    BALL = 'Bolita'
    RING = 'Anillo'
    STICK = 'Palito'
    SELF = 'Incorporado'

    HOLDING = (('Bolita', BALL), ('Anillo', RING),  ('Palito', STICK), ('Incorporado', SELF))

    capacidad = models.CharField(max_length=10)

    tipo_de_agarre = models.CharField(max_length=20, choices=HOLDING)

    imagen = models.ImageField(null=True, blank=True, upload_to='images/')

    fecha_creacion = models.DateTimeField(default=timezone.now)
    fecha_modificacion = models.DateTimeField(blank=True, null=True)

    def modified(self):
        self.fecha_modificacion = timezone.now()
        self.save()

    def __str__(self):
        return self.marca.nombre + ' ' + self.talle
