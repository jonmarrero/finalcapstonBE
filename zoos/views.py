from django.shortcuts import render
from .models import Zoo
from rest_framework import viewsets
from rest_framework import permissions
from .serializers import ZooSerializer

# Create your views here.
class ZooViewSet(viewsets.ModelViewSet):
    queryset = Zoo.objects.all()
    serializer_class = ZooSerializer
    permission_classes = [permissions.AllowAny]