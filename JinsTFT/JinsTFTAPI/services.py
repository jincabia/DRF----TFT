import requests
from .models import *
from constance import config
from .serializer import TacticianSerializer
import json
import re
import threading
import time
key = getattr(config,'API-KEY')


jins_puuid = "seQHyp4GRx0ce9koqdojpTnZidhTk4HCEEVbiw1389A0Uw53g8PVuHxdJEJg8r2R26llMKaSaHJgjw"


def fetch_recent_matches():

    """
    
    Get my most recent 20 games
    As well as save them under Game as a model in db


    """

    # my id will never change
    find_match_api_url = f"https://americas.api.riotgames.com/tft/match/v1/matches/by-puuid/{jins_puuid}/ids?start=0&count=20&api_key={key}"

    try:
        response = requests.get(find_match_api_url)
        response.raise_for_status()
        data = response.json()

        # Checks if they are already present, this way I can save more than 20 games

        PopulateGames(data)
        # for game in data:
        #     if not Game.objects.filter(game_id=game).exists():
        #         new_game = Game(game_id=game)
        #         new_game.save()
        


       
        return(data)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")


def fetch_match_info(match_id):

    """
    Fetches the match info from a specific game using a match_id which can be found
    using the fetch_recent_matches().
    """

    match_info_api_url = f'https://americas.api.riotgames.com/tft/match/v1/matches/{match_id}?api_key={key}'
    print(match_info_api_url)
    try:
        response = requests.get(match_info_api_url)
        response.raise_for_status()
        data = response.json()

        # this returns the entire game info
        return (data)
    except requests.exceptions.HTTPError as http_err:
        print(f"HTTP error occurred: {http_err}")
    except Exception as err:
        print(f"Other error occurred: {err}")

    return




def find_index(metadata_participant):

    """

    helper function to find my index in participants when reading game info

    the parameter metadata_participant is going to be from match_info['metadata']['participants']

    """

    # this represents the index where my data is stored
    jins_index = 0

    for player in metadata_participant:
        if jins_puuid == player:
            return jins_index
        jins_index +=1

    # not found
    return -1

def populate_tactician(match_info):

    """
    Find which tactician and add the placings of game to the db.
    """

    # inside models, Tactician only has itemID, and a list for placements

    # read match_info
    participants = match_info['metadata']['participants']
    # find my index from participants or match_info['metadata']['participants'] n look for my puuid
    jins_index = find_index(participants)

    if jins_index == -1:
        return "Player not found"
    
    match_id = match_info['metadata']['match_id']
    jins_game_info = match_info['info']['participants'][jins_index]
    jins_tactician = jins_game_info['companion']['item_ID']
    print(jins_tactician)
    jins_placement = jins_game_info['placement']

    # new_game = Game(game_id=game)
    #             new_game.save()

    # Check or create tactician
    tactician,tacticianIsNew = Tactician.objects.get_or_create(itemID=jins_tactician)

    game,gameIsNew = Game.objects.get_or_create(game_id=match_id)

    tacticianplacements, tacticianPlacementIsNew = TacticianPlacements.objects.get_or_create(game=game,tactician=tactician,defaults={'placement':jins_placement})
    


    # if tactician found, edit the list of placement
    # need to make sure the placement is unique?
    # read the placement then append it
        
    # after finding my index, to find my tactician
    # go match_info['info']['participants']['jinsIndex']['companion']['item_ID']
    # find placemen t inside match_info['info']['participants']['jinsIndex']['placement']

    # if its not inside Tacticians.object.all save it

    return

def PopulateGames(matches):

    """
    Param
    ------------------
    matches - list of all matches fetched from recent all games
    """

    for match in matches:
        # match_info = (1.0, fetch_match_info(match))
        match_info = fetch_match_info(match)
        game,gameIsNew = Game.objects.get_or_create(game_id=match, 
                defaults={'game_info': match_info}  # Store match_info as JSON
            )
        
        if not gameIsNew:
            game.game_info = match_info
            game.save()
        
        time.sleep(1)


    return

def FindTacticianUsingID(id):

    """
    Helper function to find the Tactician using id
    WHEN STORED INSIDE DATABASE
    """

    tactician = Tactician.objects.get(id=id)    
    serializer = TacticianSerializer(tactician)
    # print(tactician)
    if tactician:   
        return serializer.data
    return -1

def bsTactician (data ,low ,high , target):

    """
    Parameters
    ---------------
    data = JSON file (companions.json)
    target = itemID

    Returns
    ---------------
    index of the json file for our tactician, i think lol
    """
    
    if high >= low:
        mid = low+(high-low)//2

        # target found
        if(data[mid]['itemId'] == target):
            return mid
        
        # if its smaller then mid
        elif data[mid]['itemId'] > target:
            return bsTactician(data, low, mid-1, target)
        
        # if its greater than mid
        else:
            return bsTactician(data, mid + 1, high, target)
    else:
        return -1

def getTacticianPath(match):
        
        """
        Finds the tactician im using using the game data fetched from the api 

        Maybe i should read from db instead of api calls?
        """

        participants = match['metadata']['participants']
        jins_index = find_index(participants)

        if jins_index == -1:
            return ("Jin's PUUID can not be found in this game")
        
        # Match Info contains details abt the players data (tacticians, augments, units)
        match_info = match['info']

        # My match info
        jins_info = match_info['participants'][jins_index]

        # This is the item_ID used in game
        item_ID = jins_info['companion']['item_ID']

        # Change the path for the json file here
        # JinsTFT\JinsTFTAPI
        # with open('JinsTFTAPI\companions.json', 'r', encoding="utf8") as file:
        #     companions_json = json.load(file)
        
        # len_companions_json = len(companions_json)

        # index_tactician_used = bsTactician(companions_json,0,len_companions_json,item_ID)

        # tactician_used = companions_json[index_tactician_used]['name']

        # img_path = re.split('Companions/', companions_json[index_tactician_used]['loadoutsIcon'])[-1]


        # return [tactician_used,img_path]

        return searchInsideJSON(item_ID)

def searchInsideJSON(target_tact_id):

    """
    Search inside the JSON file and return the name of tactician and the img path
    """

    with open('JinsTFTAPI\companions.json', 'r', encoding="utf8") as file:
            companions_json = json.load(file)
        
    len_companions_json = len(companions_json)

    index_tactician_used = bsTactician(companions_json,0,len_companions_json,target_tact_id)

    name = companions_json[index_tactician_used]['name']

    img_path = re.split('Companions/', companions_json[index_tactician_used]['loadoutsIcon'])[-1]


    return {'name':name, 'path':img_path}

def getTacticianGames(itemID):

    """
    Get the games from the tactician using its id
    """

    tactician = Tactician.objects.get(itemID=itemID)
    print(tactician)

    if tactician:
            tacticianplacements = TacticianPlacements.objects.filter(tactician=tactician)
            return(tacticianplacements)
    
    return('Tactician not found')
            


