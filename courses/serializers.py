from rest_framework import serializers
from .models import Curso, Instructor

class InstructorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Instructor
        fields = ['id', 'nombre', 'especialidad']

class CursoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'duracion_horas', 'nivel', 'instructor']

class CursoDetailSerializer(serializers.ModelSerializer):
    instructor = InstructorSerializer(read_only=True)
    class Meta:
        model = Curso
        fields = ['id', 'nombre', 'duracion_horas', 'nivel', 'instructor']

class InstructorDetailSerializer(serializers.ModelSerializer):
    cursos = CursoSerializer(many=True, read_only=True)
    class Meta:
        model = Instructor
        fields = ['id', 'nombre', 'especialidad', 'cursos']
