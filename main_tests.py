import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'settings')
import django
django.setup()

from task_1.tests import task_1_tests
from task_2.tests import task_2_tests

if __name__ == "__main__":
    task_1_tests()
    task_2_tests()