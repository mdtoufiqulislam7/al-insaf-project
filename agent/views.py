from django.shortcuts import render

# Create your views here.
from .serializer import agentSerializers
from .models import agent
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated,AllowAny



class agentview(generics.ListCreateAPIView):
    queryset = agent.objects.all()
    serializer_class = agentSerializers
    permission_classes = [AllowAny]