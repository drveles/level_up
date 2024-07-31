"""
Модели для 1го задания
"""
from django.db import models


class Player(models.Model):
    id = models.BigAutoField(primary_key=True)
    nickname = models.CharField(max_length=100)
    first_login = models.DateField()
    last_login = models.DateField()
    level = models.PositiveIntegerField(default=0)
    exp = models.PositiveIntegerField(default=0)


class Boost(models.Model):
    id = models.BigAutoField(primary_key=True)
    description = models.CharField(max_length=100)
    player_id = models.ForeignKey(Player, on_delete=models.CASCADE)
    end_at = models.DateTimeField(default=None)
    exp_multiplier = models.PositiveIntegerField(default=0)
    exp_take = models.PositiveIntegerField(default=0)
