# Django model tests for Podcasts app

from django.test import TestCase

from podcasts.models import Podcast


class TestPodcastModels(TestCase):
    """
    Tests for Podcasts Models
    """

    fixtures = ['initial_data.json']

    def test_episode_count(self):
        """
        Test episode count method
        """
        podcast = Podcast.objects.get(pk=1)
        self.assertEqual(2, podcast.episodes.all().count())
        self.assertEqual(2, podcast.episode_count())
