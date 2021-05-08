# URLs for Games
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

from games.views import GameViewSet

app_name = "games"

games_api_router = routers.DefaultRouter()
games_api_router.register("games", GameViewSet)

urlpatterns = [
                  path("", TemplateView.as_view(template_name="games/home.html")),
                  path("api/", include(games_api_router.urls)),
                  # Automatically Created API URLs from Router
                  # api/  'api-root' - shows list of apis available
                  # api/games/  'game-list' - shows list of all podcasts
                  # api/games/<id> 'game-detail' shows the detail of a single game based on its id

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
