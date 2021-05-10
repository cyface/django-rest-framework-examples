# Django API tests for Podcasts app

from django.test import TestCase
from rest_framework.reverse import reverse


class TestGames(TestCase):
    """
    Tests for Games Models
    """
    fixtures = ['initial_data.json']

    def test_api_podcast_list(self):
        """
        Test that the API returns a list of podcasts
        """
        response = self.client.get(reverse("podcasts:podcast-list"))
        self.assertContains(response, "Podcast 1")

    def test_api_podcast_detail(self):
        """
        Test that the API returns a podcast detail by uuid
        """
        response = self.client.get(reverse("podcasts:podcast-detail", ["9b52142a-8369-4a0e-92c6-1b4dd09db3d1"]))
        self.assertContains(response, "Podcast 1")
