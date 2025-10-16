from django.db import models

class Instructor(models.Model):
    nombre = models.CharField(max_length=120)
    especialidad = models.CharField(max_length=120, blank=True)

    def __str__(self):
        return self.nombre

class Curso(models.Model):
    nombre = models.CharField(max_length=200)
    duracion_horas = models.PositiveIntegerField()  # duración en horas
    nivel = models.CharField(max_length=50)  # p. ej. 'Básico', 'Intermedio', 'Avanzado'
    instructor = models.ForeignKey(Instructor, related_name='cursos', on_delete=models.CASCADE)

    def __str__(self):
        return self.nombre
