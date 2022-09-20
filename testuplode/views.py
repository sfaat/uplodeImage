from msilib.schema import Upgrade
from typing import Generic
from django.shortcuts import render
from rest_framework import viewsets
from .serializers import *
from rest_framework.permissions import IsAdminUser

# Create your views here.


class UplodList(viewsets.ModelViewSet):
    queryset = Uplode.objects.all()
    serializer_class = UplodeSerializer
    permission_classes = [IsAdminUser]