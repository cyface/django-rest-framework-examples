# Django admin for games app
from django.contrib.admin import register, ModelAdmin

from games.models import Game


@register(Game)
class GameAdmin(ModelAdmin):
    pass
