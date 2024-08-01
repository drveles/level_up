"""
Method for 1 task
"""
import os
import datetime
import django

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")
django.setup()

from task_1.models import Player, Boost


def take_boost(manually: bool, player: Player):
    """
    Add boost to player manually or after complite level
    """
    boost = Boost()

    boost.description = "Manually boost" if manually else "Auto boost, at lvl pass"
    boost.player_id = player
    date = datetime.datetime.now().date()
    date += datetime.timedelta(days=1)
    boost.end_at = datetime.date(1111, 11, 11) if manually else date
    boost.exp_multiplier = 0 if manually else 2
    boost.exp_take = 100 if manually else 0

    boost.save()
