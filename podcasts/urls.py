# URLs for Podcasts
from django.conf import settings
from django.conf.urls.static import static
from django.urls import include, path
from rest_framework import routers

from podcasts.views.page_views import EpisodeDetail, PodcastDetail, PodcastList, HomePage
from podcasts.views.rest_api_views import PodcastViewSet

app_name = "podcasts"

podcasts_api_router = routers.DefaultRouter()
podcasts_api_router.register("podcasts", PodcastViewSet)

urlpatterns = [
                  path("", HomePage.as_view(), name="home_page"),
                  path("api/", include(podcasts_api_router.urls)),
                  path("detail/<int:pk>", PodcastDetail.as_view(), name="podcast_detail"),
                  path("episode/<int:pk>", EpisodeDetail.as_view(), name="episode_detail"),
                  path("list/", PodcastList.as_view(), name="podcast_list"),
                  # Automatically Created API URLs from Router
                  # api/  'api-root' - shows list of apis available
                  # api/podcasts/  'podcast-list' - shows list of all podcasts
                  # api/podcasts/<uuid> 'podcast-detail' shows the detail of a single podcast based on its uuid

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
