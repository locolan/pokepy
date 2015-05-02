from django.db import models

class Search(models.Model):
    def __init__(self,query_text):
        self.query_text = models.CharField(max_length=50,default='default')
    
    def __str__(self):
        return self.query_text
    
class EggGroups(models.Model):
    def __init__(self,egg_group):
        self.egg_group = models.CharField(max_length=50,default='default')
    def __str__(self):
        return self.egg_group
    
class Moves(models.Model):
    def __init__(self,move,type):
        self.move = models.CharField(max_length=50,default='default')
        self.type = models.CharField(max_length=50,default='default')
    def __str__(self):
        return self.move
    
    
class Abilities(models.Model):
    def __init__(self,ability):
        self.ability = models.CharField(max_length=50,default='default')
    def __str__(self):
        return self.ability
    
class Pokemon(models.Model):
    def __init__(self, **kwargs):
        self.name = models.CharField(max_length=50, default='bob')
        self.type1 = models.CharField(max_length=50,default='normal')
        self.type2 = models.CharField(max_length=50,default='normal')
        self.games = models.TextField(default='default')
        self.description = models.TextField(default='default')
        self.egg_group = models.CharField(max_length=50,default='default')
        self.moves = models.ManyToManyField(Moves)
        self.abilities = models.ManyToManyField(Abilities)
    def __str__(self):
        return self.name
    