from rest_framework import serializers

from .models import SuperPlayer


class PlayerSerializer(serializers.ModelSerializer):
    class Meta:# specify  what we need 
        model = SuperPlayer
        fields = ('id','name', 'score', 'country', 'addBy')