# URLs for Podcasts
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
from rest_framework import routers

from podcasts.views.rest_api_views import PodcastViewSet

app_name = "podcasts"

podcast_api_router = routers.DefaultRouter()
podcast_api_router.register(r"podcasts", PodcastViewSet)

urlpatterns = [
                  path("", TemplateView.as_view(template_name="podcasts/home.html")),
                  path("admin/", admin.site.urls),
                  path("api/", include(podcast_api_router.urls)),
                  # Automatically Created API URLs from Router
                  # api/  'api-root' - shows list of apis available
                  # api/podcasts/  'podcast-list' - shows list of all podcasts
                  # api/podcasts/<uuid> 'podcast-detail' shows the detail of a single podcast based on its uuid

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
