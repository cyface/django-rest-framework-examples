# URLs for Games
from django.urls import include, path
from django.views.generic import RedirectView
from rest_framework import routers
from games.views import GameViewSet

app_name = "games"

games_api_router = routers.SimpleRouter()
games_api_router.register("", GameViewSet)

urlpatterns = [
                  path("", RedirectView.as_view(url="/games/api/")),
                  path("api/", include(games_api_router.urls)),
                  # Automatically Created API URLs from the Router:
                  # api/ - list of all games (url name is 'game-list')
                  # api/<pk> - detail of a single game based on its primary key (url name is 'game-detail')
              ]
