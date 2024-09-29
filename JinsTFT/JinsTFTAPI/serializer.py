from rest_framework import serializers
from .models import * 

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game_id']

class TacticianSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tactician
        fields = '__all__'

class TacticianPlacementSerializer(serializers.ModelSerializer):
    class Meta:
        model = TacticianPlacements
        fields = '__all__'

class StaticUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticUnitDetails
        fields = '__all__'


class DynamicUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = DynamicUnitDetails
        fields = '__all__'