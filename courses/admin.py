from django.contrib import admin
from .models import Curso, Instructor

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'especialidad']
    search_fields = ['nombre', 'especialidad']

@admin.register(Curso)
class CursoAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'duracion_horas', 'nivel', 'instructor']
    search_fields = ['nombre', 'nivel']
    list_filter = ['nivel', 'instructor']
