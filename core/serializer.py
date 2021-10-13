from rest_framework import serializers
from core import models
from django.contrib.auth.models import User

from core.models import Obras


class CoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Obras
        fields = '__all__'