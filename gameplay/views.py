from django.contrib.auth.decorators import login_required
from django.shortcuts import render, get_object_or_404, redirect

# Create your views here.
from gameplay.forms import MoveForm
from gameplay.models import Game


@login_required
def game_detail(request, id):
  game = get_object_or_404(Game, pk=id)

  context = {'game': game}
  if game.is_users_move(request.user):
    context['form'] = MoveForm()

  return render(request, "gameplay/game_detail.html", context)

@login_required
def make_move(request, id):

  game = get_object_or_404(Game, pk=id)

  if not game.is_users_move(request.user):
    raise PermissionError

  move = game.new_move()
  form = MoveForm(instance=move, data=request.POST)

  if form.is_valid():
    game.save()
    form.save()
    return redirect("gameplay_detail", id)
  else:
    return render(request, "gameplay/game_detail.html", {'game': game, 'form': form})