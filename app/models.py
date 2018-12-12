from django.db import models


# Create your models here.

class Alumno (models.Model):
    nombre = models.CharField(max_length=30)
    apellido = models.CharField(max_length=30)

    alumno.verbose_name = 'Alumno'

class Curso (models.Model):
    año = models.DateTimeField()
    divicion = models.CharField(max_lenght=1)



class Asistencia (models.Model):
    alumno = models.ForeignKey (Alumno)
    fecha = models.DateTimeField()

    def __str__(self):
        return 'inacistencia de {}'.format(self.Alumno)

