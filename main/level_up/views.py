from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import FormView

# Create your views here.

@login_required
def level_up_view(request):
    return render(request, "main.html")
def level_up_login_view(request):
    return render(request, "login.html")

class RegisterVeiw(FormView):
    template_name = 'register.html'
    success_url = reverse_lazy("level_up:")
    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
