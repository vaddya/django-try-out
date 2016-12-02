import datetime
from django.db import models

from django.utils import timezone


class Note(models.Model):
    note_title = models.CharField(max_length=30)
    note_text = models.CharField(max_length=200)
    label = models.CharField(max_length=30)
    pub_date = models.DateTimeField(default=timezone.now())
    author = models.CharField(max_length=30)
    is_pinned = models.BooleanField()

    def was_published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)

    def __str__(self):
        return self.note_title + ' by ' + self.author
