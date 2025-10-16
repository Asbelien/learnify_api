from rest_framework.routers import DefaultRouter
from .views import CursoViewSet, InstructorViewSet
from django.urls import path, include

router = DefaultRouter()
router.register(r'cursos', CursoViewSet, basename='cursos')
router.register(r'instructores', InstructorViewSet, basename='instructores')

urlpatterns = [
    path('api/v1/', include(router.urls)),
]
