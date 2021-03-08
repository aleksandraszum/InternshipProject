from datetime import datetime
from django.db import models


class Note(models.Model):
    note_uuid = models.CharField(max_length=36)
    title = models.CharField(max_length=50)
    content = models.TextField()
    created = models.DateTimeField(default=datetime.now)
    modified = models.DateTimeField(default=datetime.now)
    version = models.PositiveIntegerField(default=1)
    newest_version = models.BooleanField(default=True)
    deleted = models.BooleanField(default=False)

    class Meta:
        index_together = ['note_uuid', 'version']

    def __str__(self):
        return f"{self.title}"



