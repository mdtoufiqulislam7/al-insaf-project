from rest_framework import serializers

from .models import agent


class agentSerializers(serializers.ModelSerializer):
    class Meta:
        model= agent
        fields= '__all__'