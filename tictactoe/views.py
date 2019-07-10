from django.http import HttpResponse
from django.shortcuts import redirect, render


def welcome(request):
  if request.user.is_authenticated:
    return redirect("player_home")
  else:
    return render(request, "tictactoe/home.html")
