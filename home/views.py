from django.shortcuts import render
from rest_framework import routers, viewsets 
from . models import Teams
from .TeamSerializer import TeamSerializer

class TeamsViewset(viewsets.ModelViewSet):
    queryset=Teams.objects.all()
    serializer_class=TeamSerializer

