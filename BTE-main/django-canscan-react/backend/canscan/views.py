from django.shortcuts import render
from rest_framework import viewsets
from .serializers import canscanSerializer
from .models import canscan
# Create your views here.

class canscanView(viewsets.ModelViewSet):
    serializer_class = canscanSerializer
    queryset = canscan.objects.all()
