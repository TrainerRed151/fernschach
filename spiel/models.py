from django.db import models


# Create your models here.
class Player(models.Model):
    username = models.CharField(max_length=64)
    password = models.CharField(max_length=256//8)
    salt = models.CharField(max_length=8)
    elo = models.IntegerField(default=0)


class Game(models.Model):
    white = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='white')
    black = models.ForeignKey(Player, on_delete=models.CASCADE, related_name='black')
    history = models.CharField(max_length=2048, default='')
