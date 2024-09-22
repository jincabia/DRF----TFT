from rest_framework import serializers
from .models import * 

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class TacticianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tactician
        fields = '__all__'

class TacticianPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TacticianPlacements
        fields = '__all__'