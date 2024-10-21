from rest_framework import serializers
from .models import * 

class GameSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'

class GameInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game_info']

class GameIDSerializer(serializers.ModelSerializer):
    class Meta:
        model = Game
        fields = ['game_id']

class GamePlacementSerializer(serializers.ModelSerializer):

    # Use GameSerializer to retrieve the whole Game model fields
    game_info = GameSerializer(source='game', read_only=True)

    class Meta:
        model = GamePlacements
        fields = ['placement', 'game', 'game_info']

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


class StaticTraitSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticTraitDetails
        fields = '__all__'

class StaticTraitNameSerializer(serializers.ModelSerializer):
    class Meta:
        model = StaticTraitDetails
        fields = ['trait_name']


class DynamicTraitSerializer(serializers.ModelSerializer):
    static_trait_details = StaticTraitNameSerializer(read_only=True)
    game = GameIDSerializer(read_only=True)

    class Meta:
        model = DynamicTraitDetails
        fields = ['static_trait_details','tier_current','num_units','style','placement','game']