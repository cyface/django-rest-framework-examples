# Django Rest Framework Views for Podcasts
from django.shortcuts import get_object_or_404
from rest_framework.exceptions import Throttled
from rest_framework.response import Response
from rest_framework.serializers import ModelSerializer
from rest_framework.viewsets import ReadOnlyModelViewSet

from podcasts.models import Podcast


class PodcastDetailSerializer(ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['uuid', 'cover_art', 'description', 'title']


class PodcastListSerializer(ModelSerializer):
    class Meta:
        model = Podcast
        fields = ['uuid', 'cover_art', 'title', 'api_detail_url']


class PodcastViewSet(ReadOnlyModelViewSet):
    """
    API for Podcasts
    """
    queryset = Podcast.objects.all()
    serializer_class = PodcastListSerializer
    throttle_scope = "podcasts"

    def retrieve(self, request, *args, pk=None):
        queryset = self.get_queryset()
        podcast = get_object_or_404(queryset, uuid=pk)
        serializer = PodcastDetailSerializer(podcast)
        return Response(serializer.data)

    def throttled(self, request, wait):
        raise Throttled(detail={"message": "rate limit exceeded"})
