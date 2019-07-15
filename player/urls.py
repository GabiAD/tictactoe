from django.conf.urls import url
from django.contrib.auth.views import LoginView, LogoutView

from player.views import home, new_invitation, accept_invitation

urlpatterns = [
  url('home', home, name="player_home"),
  url('login', LoginView.as_view(template_name="player/login_form.html"), name="player_login"),
  url('logout', LogoutView.as_view(), name="player_logout"),
  url('new_invitation', new_invitation, name="player_new_invitation"),
  url(r'accept_invitation/(?P<id>\d+)/$', accept_invitation, name="player_accept_invitation")
]
