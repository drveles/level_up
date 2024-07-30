from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView


def level_up_view(request):
    return render(request, "main.html")