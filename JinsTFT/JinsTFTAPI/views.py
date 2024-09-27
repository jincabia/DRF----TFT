from django.shortcuts import render
from django.db.models import Count
from rest_framework.views import APIView
from rest_framework.response import Response
from .services import *
from .models import *
from .serializer import *
import json
import re

# Create your views here.

class RecentMatchView(APIView):

    """
    Fetch Recent matches and populate Tactician for now
    """

    def get(self,request):
        data = fetch_recent_matches()
        print(data)
        if not data:
            return Response( -1)

        for game in data:
            populate_tact = fetch_match_info(game)
            populate_tactician(populate_tact)

        return Response(data)
    
class CheckMatchView(APIView):

    """
    Returns the entire game info 
    """

    def get(self,request,match_id):

        data = fetch_match_info(match_id)

        if(data):
            return Response(data)
        else:
            return Response('Problem Fetching')


class GameModelView(APIView):

    """
    View all recorded gameID's
    """

    def get(self,request):
        # Order by descending order
        games = Game.objects.all().order_by('-id')
        # PopulateGames(games)
        serializer = GameSerializer(games, many=True)
        return Response(serializer.data)
    

class GameInfoView(APIView):

    """
    Gets a detailed view of all the game info, and formats it
    TODO
        Save it to DB
    """

    def get(self,request,gameID):

        # Find the match from my games model
        match = Game.objects.get(game_id = gameID)


            
        # match = fetch_match_info(gameID)
        
        # tactician_info[0] = name of tactician
        # tactician_info[1] = img path
        
        tactician_info = getTacticianPath(match.game_info)


        #  if tactician:
        #     tacticianplacements = TacticianPlacements.objects.filter(tactician=tactician)
        #     serializer = TacticianPlacementSerializer(tacticianplacements, many=True)
        #     return Response(serializer.data)
        


        
        return Response(tactician_info)

class TacticianModelView(APIView):

    """
    Views all the Tacticians I have stored from my recent games
    """

    def get (self,request):
        tacts = Tactician.objects.all()
        serializers = TacticianSerializer(tacts, many=True)
        return Response(serializers.data)

class TacticianPlacementView(APIView):

    """
    Returns a tactician + the gameID and placement
    """

    def get(self,request,item_id):

        tactician = Tactician.objects.get(itemID=item_id)
        print(tactician)

        if tactician:
            tacticianplacements = TacticianPlacements.objects.filter(tactician=tactician)
            serializer = TacticianPlacementSerializer(tacticianplacements, many=True)
            return Response(serializer.data)
            
        return Response('Tactician Not found')        




class MostUsedTactician(APIView):

    """
    Returns the most used tactician
    """

    def get(self,request):
        tacticianplacements = TacticianPlacements.objects.values('tactician').annotate(game_count = Count('game'))


        if tacticianplacements:

            tacticianItemID = FindTacticianUsingID(tacticianplacements.latest('game_count')['tactician'])

            itemID = int(tacticianItemID['itemID'])

            # finds the name of the tactician and the path of it
            results = searchInsideJSON(itemID)
            name,path = results['name'], results['path']

            # find the games and put the placements into a list
            tactician_games = getTacticianGames(itemID)
            serializer = TacticianPlacementSerializer(tactician_games, many=True)

            # placement_average = 0.0
            placements = []

            for game in serializer.data:
                placements.append(game['placement'])
                # print(game['placement'])
                # placement_average += float( game['placement'])
            
            # placement_average /= len(game)
            


            
            
            

            return Response({'game_count':tacticianplacements.latest('game_count')['game_count'],'tactician':tacticianItemID,'name':name, 'path':path,'placements':placements})
        

        return Response('Tactician Not found')

class GameIdView(APIView):

    """
    Get a list of all the gameIds stored
    """

    def get(self,request):
        game_ids = Game.objects.all()
        serializer = GameIDSerializer(game_ids, many=True)

        return Response(serializer.data)