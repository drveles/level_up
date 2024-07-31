""" Tests for task 1"""
import os
import datetime
import sqlite3
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

from task_1.models import Player, Boost


def grep_table(t_name="player"):
    filename = "./../test.sqlite"
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        cursor.execute(f"SELECT * FROM task_1_{t_name}")
        for row in cursor:
            print(row)


def create_player(set_name="Test"):
    player = Player()
    player.nickname = set_name
    player.first_login = player.last_login = datetime.datetime.now().date()
    player.save()


def take_boost(manually: bool, player: Player):
    boost = Boost()
    boost.description = "Manually boost" if manually else "Auto boost, at lvl pass"
    boost.player_id = player
    date = datetime.datetime.now().date()
    date += datetime.timedelta(days=1)
    boost.end_at = datetime.date(1111,11,11) if manually else date
    boost.exp_multiplier = 0 if manually else 2
    boost.exp_take = 100 if manually else 0
    boost.save()


if __name__ == "__main__":
    try:
        obj = Player.objects.get(nickname='Test')
    except Player.DoesNotExist:
        create_player()

    take_boost(True, Player.objects.get(nickname="Test"))   # add boost manually
    take_boost(False, Player.objects.get(nickname="Test"))  # add boost at lvl pass

    grep_table("player")
    grep_table("boost")