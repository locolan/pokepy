from django.db import models

class search(models.Model):
    query_text = models.CharField(max_length=200)
    
class pokemon(models.Model):
    name = models.CharField(max_length=200)
    moves = models.ForeignKey(moves)
    
class moves(models.Model):
    