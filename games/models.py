# Django models for the Games app

from django.db.models import CASCADE, CharField, ForeignKey, IntegerField, Model, TextField, Avg


class GamePublisher(Model):
    """
    Publisher of games in our collection
    """
    name = CharField(max_length=500)

    # 'games' is available as an auto-created manager

    def average_game_rating(self):
        return self.games.all().\
            aggregate(Avg('rating')).\
            get('rating__avg')


class Game(Model):
    """
    Game in our collection
    """
    name = CharField(max_length=500)
    description = TextField()
    notes = TextField()
    publisher = ForeignKey(GamePublisher, related_name="games", on_delete=CASCADE)
    rating = IntegerField()
