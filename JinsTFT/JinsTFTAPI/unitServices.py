import requests
from .models import *
from constance import config
from .serializer import TacticianSerializer
import json
import re
import threading
import time
from .services import *
key = getattr(config,'API-KEY')


jins_puuid = "seQHyp4GRx0ce9koqdojpTnZidhTk4HCEEVbiw1389A0Uw53g8PVuHxdJEJg8r2R26llMKaSaHJgjw"

    # This file is strictly only for units 

# TODO
# Find the units I used in a game
# Store their info
# Format it 


def populate_units(match_info):

    """
    Find all the units used in game, then create and populate them into my db

    Param
    --------------------
    match_info - Called from the DB,info from the game 
    """

    # read match_info
    participants = match_info['metadata']['participants']
    # find my index from participants or match_info['metadata']['participants'] n look for my puuid
    jins_index = find_index(participants)

    
    if jins_index == -1:
        return "Player not found"
    

    match_id = match_info['metadata']['match_id']
    jins_game_info = match_info['info']['participants'][jins_index]
    all_units = jins_game_info['units']
    # print(all_units[0])
    # jins_placement = jins_game_info['placement']

    for unit in all_units:
    # Populating Static unit details 
        # print(unit)

        # I think each name has the TFT12_Seraphine so we need to format the name when displaying
        character_id = unit['character_id']

         # re.sub is for adding spaces before capital letters, .split is to get everything after TFT12_
        character_id = re.sub('([A-Z])', r' \1', re.split('TFT12_',character_id)[-1])


        # The cost of a unit
        rarity = unit['rarity']

        # print(character_id, rarity)
        
        new_unit,unitIsNew = StaticUnitDetails.objects.get_or_create(character_id=character_id,rarity=rarity)
    
    # Populate the Dynamic unit details

        tier = unit['tier']

        items = unit['itemNames']
        # Format the items
        # TFT_Item_ThiefsGloves, TFT_Item_Artifact_InnervatingLocket, TFT9_Item_OrnnHullbreaker, "TFT12_Item_FaerieEmblemItem", "TFT12_Item_Faerie_QueensCrownRadiant"


        items_list = []

        # O(n^2) idk if i can make it more efficient if im reading the data 
        for item in items:
            

            # Removes Ornn from Items
            n_item = re.sub('Ornn','',item)

            # re.sub is for adding spaces before capital letters, .split is to get everything after _
            # Removes unneeded text like TFT12_ 
            n_item = (re.sub('([A-Z])', r' \1', re.split('_',n_item)[-1]))

            items_list.append(n_item)

            # print(n_item)
        

        game,gameIsNew = Game.objects.get_or_create(game_id=match_id)

        
        new_dynamic_unit, dynamic_unitIsNew = DynamicUnitDetails.objects.get_or_create(itemNames=items_list,tier=tier,unit=new_unit,game=game)

        
        

    
#  # Check or create tactician
#     tactician,tacticianIsNew = Tactician.objects.get_or_create(itemID=jins_tactician)

#     game,gameIsNew = Game.objects.get_or_create(game_id=match_id)

#     tacticianplacements, tacticianPlacementIsNew = TacticianPlacements.objects.get_or_create(game=game,tactician=tactician,defaults={'placement':jins_placement})
    






    pass