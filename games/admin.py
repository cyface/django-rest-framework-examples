# Django admin for games app
from django.contrib.admin import register, ModelAdmin
from django.contrib.admin.options import TabularInline

from games.models import GamePublisher, Game


@register(Game)
class GameAdmin(ModelAdmin):
    pass


class GameInline(TabularInline):
    model = Game


@register(GamePublisher)
class GamePublisherAdmin(ModelAdmin):
    inlines = [GameInline]
