from django.contrib.auth.models import User
from django.db import models

# Create your models here.
class Invitation(models.Model):
  from_user = models.ForeignKey(User, related_name="invitations_sent", on_delete=models.CASCADE)
  to_user = models.ForeignKey(User, related_name="invitations_received", on_delete=models.CASCADE)
  message = models.CharField(max_length=300, blank=True)
  timestamp = models.DateTimeField(auto_now_add=True)