# URLs for Podcasts
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic import TemplateView
import games.urls as games_urls
import podcasts.urls as podcast_urls

urlpatterns = [
                  path("", TemplateView.as_view(template_name="project/home.html")),
                  path("admin/", admin.site.urls),
                  path("games/", include(games_urls, namespace="games")),
                  path("podcasts/", include(podcast_urls, namespace="podcasts")),

              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
