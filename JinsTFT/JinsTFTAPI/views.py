from django.shortcuts import render
from django.db.models import Count, Avg
from rest_framework.views import APIView
from django.db.models.functions import Round
from rest_framework.response import Response
from .services import *
from .models import *
from .serializer import *
import json
import re
from .unitServices import *

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

        unit_info = populate_units(match.game_info)


        #  if tactician:
        #     tacticianplacements = TacticianPlacements.objects.filter(tactician=tactician)
        #     serializer = TacticianPlacementSerializer(tacticianplacements, many=True)
        #     return Response(serializer.data)
        


        
        return Response(tactician_info, unit_info)

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
        # popular_dynamic_units = DynamicUnitDetails.objects.select_related('unit').values('unit__character_id').annotate(game_count=Count('unit')).order_by('-game_count').annotate(avg_placement=Round(Avg('placement'),2))

        most_used = TacticianPlacements.objects.select_related('tactician') \
        .values('tactician__id', 'tactician__itemID','tactician__name','tactician__path') \
        .annotate(game_count=Count('game')) \
        .annotate(avg_placement=Round(Avg('placement'),1)) \
        .order_by('-game_count') 
        tacticianplacements = TacticianPlacements.objects.values('tactician').annotate(game_count = Count('game')).annotate(avg_placement = Avg('placement'))


        if tacticianplacements:

           


            # place the placements inside a list to calc average and slam it into a chart
            
                

            return Response(most_used)
        

        return Response('Tactician Not found')

class GameIdView(APIView):

    """
    Get a list of all the gameIds stored
    """

    def get(self,request):
        game_ids = Game.objects.all()
        serializer = GameIDSerializer(game_ids, many=True)

        return Response(serializer.data)
    

class StaticUnitView(APIView):

    """
    Get all the Static Units, (name: Seraphine cost = 1 )
    """

    def get(self,request):
        static_units = StaticUnitDetails.objects.all()
        serializers= StaticUnitSerializer(static_units,many=True)
        return Response(serializers.data)
    

class DynamicUnitView(APIView):

    """
    Get all the Dynamic Units, (items, tier and placements)
    
    """

    def get(self,request):
        dynamic_units = DynamicUnitDetails.objects.all()
        dynamic_serializers= DynamicUnitSerializer(dynamic_units,many=True)

        unit_list = []

        
        for units in dynamic_serializers.data:
            # Find the static unit using ID
            static_unit = StaticUnitDetails.objects.get(id=units['unit'])
            static_serializer = StaticUnitSerializer(static_unit)
            unit_list.append((units ,static_serializer.data))

        return Response(unit_list)
    
class PopulateUnitView(APIView):
    """
    Populate the units using all the games inside the DB
    """

    def get(self,request):
        games = Game.objects.all()
        for game in games:
            unit_info = populate_units(game.game_info)
        
        return Response('Success?')
    


class MostUsedUnitView(APIView):
    """
    Find the most played Unit 
    Using aggregate functions to find the most played games and avg placement 
    """
    def get (self,request):
        popular_dynamic_units = DynamicUnitDetails.objects.select_related('unit') \
        .values('unit__character_id') \
        .annotate(game_count=Count('unit')) \
        .order_by('-game_count') \
        .annotate(avg_placement=Round(Avg('placement'),2))
        return Response(popular_dynamic_units)


class PopulateTacticians(APIView):

    """
    Used to populate the tacticians itemID ,name,path
    """

    def get(self,request):
        games = Game.objects.all()
        for game in games:
            print(game)
            populating = populate_tactician(game.game_info)



        return Response('yay')