from django.contrib.auth.models import User
from django.db import models
from django.db.models import Q

GAME_STATUS_CHOICES = (
  ("F", "First player's turn"),
  ("S", "Second player's turn"),
  ("W", "First player wins"),
  ("L", "Second player wins"),
  ("D", "Draw"),
)


class GamesQuerySet(models.QuerySet):
  def games_for_user(self, user):
    return self.filter(Q(first_player=user) | Q(second_player=user))

  def active(self):
    return self.filter(Q(status='F') | Q(status='S'))


class Game(models.Model):
  first_player = models.ForeignKey(User, related_name="games_first_player", on_delete=models.SET_NULL, null=True)
  second_player = models.ForeignKey(User, related_name="games_second_player", on_delete=models.SET_NULL, null=True)

  start_time = models.DateTimeField(auto_now_add=True)
  last_active = models.DateTimeField(auto_now=True)

  status = models.CharField(max_length=1, default='F', choices=GAME_STATUS_CHOICES)

  objects = GamesQuerySet.as_manager()

  def __str__(self):
    return f"{self.first_player} vs {self.second_player}"


class Move(models.Model):
  x = models.IntegerField()
  y = models.IntegerField()
  cpmment = models.CharField(max_length=300, blank=True)
  by_first_player = models.BooleanField()

  game = models.ForeignKey(Game, on_delete=models.CASCADE)
