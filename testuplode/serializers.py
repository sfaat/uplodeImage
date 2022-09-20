from rest_framework import serializers
from .models import *



class UplodeSerializer(serializers.ModelSerializer):
    class Meta:
        model=Uplode
        fields='__all__'

        