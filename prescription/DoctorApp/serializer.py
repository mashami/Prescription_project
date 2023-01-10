from rest_framework import serializers
from .models import *
from authentication.models import User

class DoctorSerializer(serializers.ModelSerializer):
    
    class Meta:
        model=DoctorM
        fields=['DoctorName', 'medicine', 'Diseases','Date']


class PharmacistSerializer (serializers.ModelSerializer):
    
    morning=serializers.BooleanField(default=False)
    Noon=serializers.BooleanField(default=False)
    evening=serializers.BooleanField(default=False)
    Valide=serializers.BooleanField(default=True)

    class Meta:
        model=DoctorM
        fields=['Date','DoctorName', 'medicine', 'morning','Noon', 'evening','Valide']

        extra_kwargs = {
            
            'doctor':{'read_only': True},
            'medicines':{'read_only': True},     
        }

class getPatientSerializer (serializers.ModelSerializer):

    class Meta:
        model=User
        fields=['email']