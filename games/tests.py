# Django tests for Games app

from django.test import TestCase
from rest_framework.reverse import reverse

from games.models import Game, GamePublisher


class TestGames(TestCase):
    """
    Tests for Games Models
    """

    @classmethod
    def setUpTestData(cls):
        """
        Set up test data, and document now models wire together
        """
        cls.publisher1 = GamePublisher.objects.create(name="Game Publisher 1")
        cls.game1 = Game.objects.create(
            name="Game 1",
            description="Game 1 Description",
            notes="Game 1 Notes",
            publisher=cls.publisher1,
            rating="4"
        )
        cls.game2 = Game.objects.create(
            name="Game 2",
            description="Game 2 Description",
            notes="Game 2 Notes",
            publisher=cls.publisher1,
            rating="3"
        )

    def test_publisher_rating(self):
        """
        Test that games are added to publishers, and that average rating calculates correctly
        """
        self.assertEqual(2, self.publisher1.games.all().count())
        self.assertEqual(3.5, self.publisher1.average_game_rating())

    def test_api_game_list(self):
        """
        Test that the API returns a list of games
        """
        response = self.client.get(reverse("games:game-list"))
        self.assertContains(response, "Game 1 Description")
        self.assertContains(response, "Game 2 Notes")
        self.assertContains(response, "Publisher 1")

    def test_api_game_detail(self):
        """
        Test that the API returns a list of games
        """
        response = self.client.get(reverse("games:game-detail", [1]))
        self.assertContains(response, "Game 1 Description")
        self.assertContains(response, "Game 1 Notes")
        self.assertContains(response, "Publisher 1")
