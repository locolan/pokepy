from django.db import models

class Search(models.Model):
    query_text = models.CharField(max_length=50,default='default') 
    def __str__(self):
        return self.query_text
    
#===============================================================================
# class EggGroups(models.Model):
#     egg_group = models.CharField(max_length=50,default='default')
#     def __str__(self):
#         return self.egg_group
#===============================================================================
    
class Moves(models.Model):
    move = models.CharField(max_length=50,default='default')
    type = models.CharField(max_length=50,default='default')
    def __str__(self):
        return self.move
    
    
class Abilities(models.Model):
    ability = models.CharField(max_length=50,default='default')
    def __str__(self):
        return self.ability
    
class Pokemon(models.Model):
    name = models.CharField(max_length=50, default='bob')
    type1 = models.CharField(max_length=50,default='normal')
    type2 = models.CharField(max_length=50,default='normal')
    games = models.TextField(default='default')
    description = models.TextField(default='default')
    egg_group = models.CharField(max_length=50,default='default')
    moves = models.ManyToManyField(Moves)
    abilities = models.ManyToManyField(Abilities)
    def __str__(self):
        return self.name
    