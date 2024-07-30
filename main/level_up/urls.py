from django.urls import path
from .views import level_up_view, level_up_login_view, RegisterVeiw

app_name = "level_up"

urlpatterns = [
    path("", level_up_view, name="level_up"),
    path("login", level_up_login_view, name="login"),
    path("register", RegisterVeiw.as_view(), name="register"),
]
