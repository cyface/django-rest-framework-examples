# Django Admin for Podcasts
from django.contrib.admin import ModelAdmin, TabularInline, register

from podcasts.models import Episode, Person, PodcastPersonRole, Podcast, Role


@register(Episode)
class EpisodeAdmin(ModelAdmin):
    pass


class EpisodeInline(TabularInline):
    model = Episode


@register(Person)
class PersonAdmin(ModelAdmin):
    pass


class PodcastPersonRoleInline(TabularInline):
    model = PodcastPersonRole


@register(Podcast)
class PodcastAdmin(ModelAdmin):
    inlines = [
        EpisodeInline,
        PodcastPersonRoleInline
    ]


@register(Role)
class RoleAdmin(ModelAdmin):
    pass
