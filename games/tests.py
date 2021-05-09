# Django tests for Games app

from django.test import TestCase
from rest_framework.reverse import reverse

from games.models import Game


class TestGames(TestCase):
    """
    Tests for Games Models
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data, and document how models are created
        """
        cls.game1 = Game.objects.create(
            name="Game 1",
            description="Game 1 Description",
            notes="Game 1 Notes",
            rating="4"
        )
        cls.game2 = Game.objects.create(
            name="Game 2",
            description="Game 2 Description",
            notes="Game 2 Notes",
            rating="3"
        )

    def test_api_game_list(self):
        """
        Test that the API returns a list of games
        """
        response = self.client.get(reverse("games:game-list"))
        self.assertContains(response, "Game 1 Description")
        self.assertContains(response, "Game 2 Notes")

    def test_api_game_detail(self):
        """
        Test that the API returns a list of games
        """
        response = self.client.get(reverse("games:game-detail", [1]))
        self.assertContains(response, "Game 1 Description")
        self.assertContains(response, "Game 1 Notes")
