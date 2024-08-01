""" Tests for task 1"""

import os
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

import datetime
import sqlite3
from task_1.models import Player
from task_1.boosts import take_boost


def grep_table(t_name="player"):
    """
    Printing inputed table
    """
    filename = "./test.sqlite"
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM task_1_{t_name}")
        for row in cursor:
            print(row)


def create_player(set_name="Test"):
    """
    Create Player for tests
    """
    player = Player()
    player.nickname = set_name
    player.first_login = player.last_login = datetime.datetime.now().date()
    player.save()


def task_1_tests():
    """
    All tests for 1 task
    """
    try:
        obj = Player.objects.get(nickname="Test")
    except Player.DoesNotExist:
        create_player()

    take_boost(True, Player.objects.get(nickname="Test"))  # add boost manually
    take_boost(False, Player.objects.get(nickname="Test"))  # add boost at lvl pass

    grep_table()
    grep_table("boost")


if __name__ == "__main__":
    task_1_tests()
