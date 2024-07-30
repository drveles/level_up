from django.urls import path
from .views import level_up_view

app_name = "level_up"

urlpatterns = [
    path("", level_up_view, name="level_up"),
]
