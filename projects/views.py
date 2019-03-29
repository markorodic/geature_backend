from django.shortcuts import render
from projects.serializer import ProjectSerializer
from rest_framework import viewsets
from projects.models import Project
import django_filters.rest_framework

# Create your views here
class ProjectsViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    filter_backends = (django_filters.rest_framework.DjangoFilterBackend,)
    filterset_fields = ('id', 'name')