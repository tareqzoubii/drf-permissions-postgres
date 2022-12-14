from rest_framework import serializers
from .models import Clubs,Players


class ClubsSerializer(serializers.ModelSerializer):
    class Meta:
        model= Clubs
        fields='__all__'

class PlayerSerializer(serializers.ModelSerializer):
    class Meta:
        model= Players
        fields='__all__'