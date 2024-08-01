"""
Tests for task 2
"""

import os
import datetime
import sqlite3
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from task_2.models import Player, Level, Prize, PlayerLevel, LevelPrize
from task_2.methods import give_prize, export_player_to_csv


def create_test_data():
    """
    Creating data in DB to tests
    """
    player = Player()
    level = Level()
    prize = Prize()
    player_lvl = PlayerLevel()
    level_prize = LevelPrize()

    player.player_id = "Test uuid"

    level.title = "1 level"
    level.order = 1

    prize.title = "Test prize"

    player_lvl.player = player
    player_lvl.level = level
    player_lvl.completed = datetime.datetime.now().date()
    player_lvl.is_completed = True
    player_lvl.score = 10

    level_prize.level = level
    level_prize.prize = prize
    level_prize.received = datetime.datetime.now().date()

    player.save()
    level.save()
    prize.save()
    player_lvl.save()
    level_prize.save()


def grep_table(t_name="player"):
    """
    Print inputed table
    """
    filename = "./../test.sqlite"
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM task_2_{t_name}")
        for row in cursor:
            print(row)


if __name__ == "__main__":
    try:
        obj = Player.objects.get(player_id="Test uuid")
    except Player.DoesNotExist:
        create_test_data()
    give_prize("Test uuid", "1 level", "Test prize")
    export_player_to_csv("./test.csv")

    grep_table()
    grep_table("level")
    grep_table("prize")
    grep_table("playerlevel")
    grep_table("levelprize")
