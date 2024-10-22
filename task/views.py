from django.shortcuts import render
from rest_framework import viewsets
from task import models
from .serializer import TaskSerializer
# Create your views here.

class TaskViewSet(viewsets.ModelViewSet):
    queryset= models.Task.objects.all()
    serializer_class= TaskSerializer