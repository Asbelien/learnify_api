from rest_framework import viewsets
from .models import Curso, Instructor
from .serializers import (
    CursoSerializer,
    CursoDetailSerializer,
    InstructorSerializer,
    InstructorDetailSerializer
)

class CursoViewSet(viewsets.ModelViewSet):
    queryset = Curso.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return CursoDetailSerializer
        return CursoSerializer


class InstructorViewSet(viewsets.ModelViewSet):
    queryset = Instructor.objects.all()

    def get_serializer_class(self):
        if self.action == 'retrieve':
            return InstructorDetailSerializer
        return InstructorSerializer
