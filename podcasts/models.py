# Django Models for Podcasts
from uuid import uuid4

from django.db.models import (
    CASCADE,
    CharField,
    DO_NOTHING,
    EmailField,
    FileField,
    ForeignKey,
    ImageField,
    IntegerField,
    Model,
    TextField, ManyToManyField, UUIDField,
)
from django.urls import reverse


class Podcast(Model):
    title = CharField(max_length=500)
    description = TextField()
    cover_art = ImageField()
    uuid = UUIDField(default=uuid4, editable=False, db_index=True)

    # episodes - manager auto-created by Django with list of episodes associated with this Podcast
    # people - manager auto-created by Django with list of people associated with this Podcast

    def api_detail_url(self):
        return reverse("podcasts:podcast-detail", args=[self.uuid])

    def episode_count(self):
        return self.episodes.all().count()

    def __str__(self):
        return self.title


class Episode(Model):
    podcast = ForeignKey(Podcast, related_name="episodes", on_delete=CASCADE)
    media = FileField()
    sequence = IntegerField()
    show_notes = TextField()

    def __str__(self):
        return f"{self.podcast.title} - Episode {self.sequence}"

    class Meta:
        ordering = ["sequence"]


class Role(Model):
    name = CharField(max_length=40)

    # people - manager auto-created by Django with list of people in this Role

    def __str__(self):
        return self.name


class Person(Model):
    name = CharField(max_length=200)
    email_address = EmailField()
    role = ManyToManyField(Role, related_name="people", through="PodcastPersonRole")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "people"


class PodcastPersonRole(Model):
    podcast = ForeignKey(Podcast, related_name="people", on_delete=DO_NOTHING)
    person = ForeignKey(Person, related_name="podcasts", on_delete=DO_NOTHING)
    role = ForeignKey(Role, related_name="role", on_delete=DO_NOTHING)

    def __str__(self):
        return f"{self.person} ({self.role.name})"