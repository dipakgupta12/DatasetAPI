from django.db import models
from django.conf import settings

CHOICES = (
    ('TITLE', 'title'),
    ('DESCRIPTION', 'description'),
    ('IMAGE', 'image')
)

class Data(models.Model):
    title = models.CharField(
        max_length=200, choices=CHOICES
    )
    description = models.TextField(null=True, blank=True)
    image = models.TextField(null=True, blank=True)

