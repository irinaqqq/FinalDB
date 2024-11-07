# serializers.py
from rest_framework import serializers
from .models import RegistrationRequest

class RegistrationRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistrationRequest
        fields = ['first_name', 'last_name', 'organization', 'email', 'phone_number', 'status']
