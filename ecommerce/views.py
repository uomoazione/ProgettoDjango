from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView

from django.shortcuts import render


def home(request):
    return render(request, "home.html")


class Login(LoginView):
    authentication_form = AuthenticationForm
    template_name = "authentication/login.html"
