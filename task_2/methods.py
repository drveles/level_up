"""
Task 2 functions
"""

import os
import datetime
import django
import csv
from django.db import transaction

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from task_2.models import Player, Level, Prize, PlayerLevel, LevelPrize


@transaction.atomic
def give_prize(player_id, level_title, prize_title):
    """
    Присвоение игроку приза
    """
    player = Player.objects.get(player_id=player_id)
    level = Level.objects.get(title=level_title)
    prize, created = Prize.objects.get_or_create(title=prize_title)
    player_level = PlayerLevel.objects.get(player=player, level=level)
    player_level.is_completed = True
    player_level.completed = datetime.date.today()
    player_level.save()

    level_prize = LevelPrize()
    level_prize.level = level
    level_prize.prize = prize
    level_prize.received = datetime.date.today()

    level_prize.save()


def export_player_to_csv(file_path):
    """
    Выгрузка в csv следующих данных: 
    id игрока, название уровня, пройден ли уровень, полученный приз за уровень.
    """
    player_levels = PlayerLevel.objects.select_related(
        "player", "level"
    ).prefetch_related(
        django.db.models.Prefetch(
            "level__levelprize_set", queryset=LevelPrize.objects.select_related("prize")
        )
    )

    with open(file_path, mode="w", newline="") as file:
        writer = csv.writer(file)
        writer.writerow(["Player ID", "Level Title", "Is Completed", "Prize Title"])

        for player_level in player_levels:
            player_id = player_level.player.player_id
            level_title = player_level.level.title
            is_completed = player_level.is_completed
            prize_title = (
                player_level.level.levelprize_set.first().prize.title
                if player_level.level.levelprize_set.exists()
                else ""
            )
            writer.writerow([player_id, level_title, is_completed, prize_title])

    print(f"Data exported successfully to {file_path}")
