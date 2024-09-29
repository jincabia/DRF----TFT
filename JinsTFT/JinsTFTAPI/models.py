from django.db import models

# Create your models here.

class Game(models.Model):
    game_id = models.CharField(max_length=100,unique=True)
    game_info = models.JSONField(default=dict)

    def __str__(self):
        return self.game_id


# Ill store the tactician itemID i used and put all my placing inside 
# a list to showcase my winrate with them

# TODO
# add name to db instead of needing to look it up constantly
class Tactician(models.Model):
    itemID = models.CharField(max_length=100)



    # placing = models.JSONField(default=list)

    # # tact a
    # # [8,1,4,6]

    # games = models.ForeignObject

    def __str__(self):
        return self.itemID



class TacticianPlacements(models.Model):

    game = models.ForeignKey(Game, on_delete=models.CASCADE)
    tactician = models.ForeignKey(Tactician,on_delete=models.CASCADE)
    placement = models.IntegerField()

    # NA-0000
    # Tactician A
    # Placement : 0



# Characteristics that will not be changed, ie Cost of a Unit & character_id
class StaticUnitDetails(models.Model):
    # Name of the unit
    character_id = models.CharField(max_length=100)

    # API-Rarity = In Game Costs
    rarity_choices =(
        # One Cost
        (0,1),
        # Two Cost
        (1,2),
        # Three Cost
        (2,3),
        # Four Cost
        (4,4),
        # 5 Cost
        (6,5),
        # A unit that cannot be bought, ie Frost Wolf & Yummi
        (9,0),
    )

    rarity = models.IntegerField( choices=rarity_choices)

    

# WARNING
# Be careful for duplicates since I can place more than 1 of the same Unit 
# Details that change from game to game, ie Tier of a unit, and its items
class DynamicUnitDetails(models.Model):

    # List of items
    itemNames = models.JSONField(default=list)
   
    # the star of a unit 1 star (bronze) , 2 star (silver), 3 star (gold)
    tier = models.IntegerField(default=0)


    # the game it belongs to
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    # the other character details
    unit = models.ForeignKey(StaticUnitDetails,on_delete=models.CASCADE)

