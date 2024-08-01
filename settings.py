"""
File for using Django lib without Django apps, included settings
"""
import os

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

DEFAULT_AUTO_FIELD = 'django.db.models.AutoField'

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": os.path.join(BASE_DIR, "test.sqlite"),
    }
}

INSTALLED_APPS = ("task_1", "task_2", )
