import requests
from .models import *
from constance import config
from .serializer import TacticianSerializer
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

        
        for game in data:
            if not Game.objects.filter(game_id=game).exists():
                new_game = Game(game_id=game)
                new_game.save()
       
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

        participant_index = 0

        # this returns only my game info
        # finds what index my info is gonna be at
        # for player in (data['metadata']['participants']):
        #     if player == jins_puuid:
        #         # print(participant_index)
        #         break
        #     participant_index += 1

        # return(data['info']['participants'][participant_index])


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

def FindTacticianUsingID(id):

    """
    Helper function to find the Tactician using id
    """

    tactician = Tactician.objects.get(id=id)
    serializer = TacticianSerializer(tactician)
    # print(tactician)
    if tactician:   
        return serializer.data
    return -1