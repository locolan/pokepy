from django.db import models

class search(models.Model):
    query_text = models.CharField(max_length=50)
    
class egg_groups(models.Model):
    egg_group = models.CharField(max_length=50)
    
class moves(models.Model):
    move = models.CharField(max_length=50)
    type = models.CharField(max_length=50)
    
    
class abilities(models.Model):
    ability = models.CharField(max_length=50)
    
class pokemon(models.Model):
    name = models.CharField(max_length=50)
    type1 = models.CharField(max_length=50)
    type2 = models.CharField(max_length=50)
    games = models.TextField()
    description = models.TextField()
    egg_group = models.ForeignKey(egg_groups)
    moves = models.ManyToManyField(moves)
    abilities = models.ManyToManyField(abilities)