from django.shortcuts import render

# Create your views here.


def level_up_view(request):
    return render(request, "main.html")

