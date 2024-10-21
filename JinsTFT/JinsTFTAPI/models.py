from django.db import models

# Create your models here.

class Game(models.Model):
    game_id = models.CharField(max_length=100,unique=True)
    game_info = models.JSONField(default=dict)
    def __str__(self):
        return self.game_id
    
    # def save(self,*args,**kwargs):
    #     pass

class GamePlacements(models.Model):
    """
    Storing game placements so I dont need to keep reading it from Game objects
    """
    placement = models.IntegerField()
    game = models.ForeignKey(Game, on_delete=models.CASCADE)

# Ill store the tactician itemID i used and put all my placing inside 
# a list to showcase my winrate with them

class Tactician(models.Model):
    itemID = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    path = models.CharField(max_length=500)



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
    
    # TRAITS???

    rarity = models.IntegerField( )
    # rarity = models.IntegerChoices

    

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

    placement = models.IntegerField()


class StaticTraitDetails(models.Model):
    """
    things that do not change for traits
    """

    trait_name = models.CharField(max_length=100)
    tier_total = models.IntegerField(default=0)


    pass

class DynamicTraitDetails(models.Model):

    """
    things that do change from game to game
    """

    # style_dict = {
    #     0 : 'Not Active',
    #     1 : 'Bronze',
    #     2 : 'Silver',
    #     3 : 'Gold',
    #     4 : 'Prismatic',
    #     5 : 'Unique'
    #                 }

    # Idk
    tier_current = models.IntegerField()

    # How much units of a certain trait are on the board
    num_units = models.IntegerField()
    
    # What color the trait is currently (Bronze, Silver, Gold, Prismatic)
    style = models.IntegerField()

    static_trait_details = models.ForeignKey(StaticTraitDetails, on_delete=models.CASCADE)

    game = models.ForeignKey(Game, on_delete=models.CASCADE)

    placement = models.IntegerField()



    pass