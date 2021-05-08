# Django Rest Framework Views for Podcasts
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import Throttled
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from podcasts.models import Podcast


class PodcastSerializer(ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['uuid', 'cover_art', 'description', 'title', 'api_detail_url']


class PodcastViewSet(ReadOnlyModelViewSet):
    """
    API for Podcasts
    """
    queryset = Podcast.objects.all()
    serializer_class = PodcastSerializer
    throttle_scope = "podcast_detail"

    def retrieve(self, request, *args, pk=None):
        queryset = self.get_queryset()
        user = get_object_or_404(queryset, uuid=pk)
        serializer = PodcastSerializer(user)
        return Response(serializer.data)

    def throttled(self, request, wait):
        raise Throttled(detail={"message": "rate limit exceeded"})
