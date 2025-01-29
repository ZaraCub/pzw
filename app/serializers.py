from dataclasses import fields
from rest_framework import serializers
from .models import Language, User, Exchange

class LanguageSerializer(serializers.ModelSerializer):
    class Meta:
        model = Language
        fields = '__all__'

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class ExchangeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Exchange
        fields='__all__'
