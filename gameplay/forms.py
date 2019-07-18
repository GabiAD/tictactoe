from django.forms import ModelForm

from gameplay.models import Move


class MoveForm(ModelForm):
  class Meta:
    model = Move
    exclude = []