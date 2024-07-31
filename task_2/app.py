"""
Task 2 functions
"""
import os
import datetime
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from .models import Player, Level, Prize, PlayerLevel, LevelPrize


def give_prize():
    # Присвоение игроку приза за прохождение уровня.
    pass

def export_player_to_csv():
    """
    Выгрузка в csv следующих данных: id игрока, название уровня, пройден ли уровень, полученный приз за уровень.
    Учесть, что записей может быть 100 000 и более.
    :return: csv
    """
    pass
