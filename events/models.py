from django.db import models

class User(models.Model):
    email = models.EmailField()
    name = models.CharField(max_length=255)
    avatar_url = models.CharField(max_length=255)
    google_id = models.CharField(max_length=255)
    google_token = models.TextField()

    def __str__(self):
        return self.name


class Event(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    locale = models.CharField(max_length=255)
    date = models.DateTimeField('event date')

    def __str__(self):
        return self.title


class EventUser(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    event = models.ForeignKey(Event, on_delete=models.CASCADE)
    is_presenter = models.BooleanField()
    slide_url =  models.CharField(max_length=255)
    comment =  models.CharField(max_length=255)
