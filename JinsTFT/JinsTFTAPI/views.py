from django.shortcuts import render
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import *
from .models import *
from .serializer import *

# Create your views here.

class RecentMatchView(APIView):
    def get(self,request):
        data = fetch_recent_matches()

        for game in data:
            populate_tact = fetch_match_info(game)
            populate_tactician(populate_tact)

        return Response(data)
    
class CheckMatchView(APIView):
    def get(self,request,match_id):

        data = fetch_match_info(match_id)

        if(data):
            return Response(data)
        else:
            return Response('Problem Fetching')


# When getting data from here take it from the very 
# last id:1 is the oldest game 
class GameModelView(APIView):
    def get(self,request):
        # Order by descending order
        games = Game.objects.all().order_by('-id')
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    
# param = tactician.itemID then give me a list of placements

class TacticianModelView(APIView):
    def get (self,request):
        tacts = Tactician.objects.all()
        serializers = TacticianSerializer(tacts, many=True)
        return Response(serializers.data)

class TacticianPlacementView(APIView):
    def get(self,request,item_id):

        tactician = Tactician.objects.get(itemID=item_id)

        if tactician:
            tacticianplacements = TacticianPlacements.objects.filter(tactician=tactician)
            serializer = TacticianPlacementSerializer(tacticianplacements, many=True)
            return Response(serializer.data)
            
        return Response('Tactician Not found')        




class MostUsedTactician(APIView):
    def get(self,request):
        tacticianplacements = TacticianPlacements.objects.values('tactician').annotate(game_count = Count('game'))
        tacticianItemID = FindTacticianUsingID(tacticianplacements.latest('game_count')['tactician'])
        if tacticianplacements:
            # return Response({'game_count':tacticianplacements.latest('game_count')['game_count'],'tactician':tacticianplacements.latest('game_count')['tactician']})
            return Response({'game_count':tacticianplacements.latest('game_count')['game_count'],'tactician':tacticianItemID})