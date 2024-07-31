import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
django.setup()

import sqlite3
import datetime

from task_1.models import Player, Boost


def grep_all_tables():
    filename = "./../test.sqlite"
    with sqlite3.connect(filename) as conn:
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table'")
        for tablerow in cursor.fetchall():
            table = tablerow[0]
            cursor.execute("SELECT * FROM {t}".format(t=table))
            for row in cursor:
                    for field in row.keys():
                        print(table, field, row[field])


def grep_player_table():
    filename = "./../test.sqlite"
    with sqlite3.connect(filename) as conn:
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM task_1_player")
        for row in cursor:
            print(row)


def create_player():
    print("Creating Player")
    player = Player()
    player.nickname = 'Test 1'
    player.first_login = player.last_login = datetime.datetime.now().date()
    player.save()
    print("Player Saved!!")


if __name__ == "__main__":
    create_player()
    # grep_all_tables()
    grep_player_table()