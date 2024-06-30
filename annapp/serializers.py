from django.db import models

from rest_framework import serializers

from .models import Ann
class AnnSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ann
        fields = '__all__'

        