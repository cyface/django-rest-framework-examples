# Django views for the podcasts app
from django.views.generic import TemplateView, ListView, DetailView

from podcasts.models import Episode, Podcast


class HomePage(TemplateView):
    template_name = "podcasts/home.html"


class EpisodeDetail(DetailView):
    model = Episode
    context_object_name = "episode"


class PodcastList(ListView):
    model = Podcast
    context_object_name = "podcasts"


class PodcastDetail(DetailView):
    model = Podcast
    context_object_name = "podcast"
