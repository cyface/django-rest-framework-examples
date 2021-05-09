# Django and DRF views for Game app

from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from games.models import Game


class GameSerializer(ModelSerializer):
    class Meta:
        model = Game
        fields = '__all__'


class GameViewSet(ReadOnlyModelViewSet):
    """
    API for Games
    """
    queryset = Game.objects.all()
    serializer_class = GameSerializer
