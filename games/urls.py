# URLs for Games
from django.conf import settings
from django.conf.urls.static import static
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
                  # Automatically Created API URLs from Router
                  # api/  'game-list' - shows list of all games
                  # api/<pk> 'game-detail' shows the detail of a single game based on its primary key
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
