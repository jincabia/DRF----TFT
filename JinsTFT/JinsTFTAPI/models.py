from django.db import models

# Create your models here.

class Game(models.Model):
    game_id = models.CharField(max_length=100,unique=True)
    game_info = models.JSONField(default=dict)

    def __str__(self):
        return self.game_id

# TODO 
# Save game info so incase i dont have apikey itll stil work

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

