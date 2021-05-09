# Django models for the Games app

from django.db.models import CharField, IntegerField, Model, TextField


class Game(Model):
    """
    Game in our collection
    """
    name = CharField(max_length=500)
    description = TextField()
    notes = TextField()
    rating = IntegerField()
