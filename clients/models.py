from django.db import models
from core import models as core_models


# Create your models here.
class Client(core_models.TimeStampedModel):

    """Client Model"""

    name = models.CharField(max_length=150, unique=True)
    location = models.CharField(max_length=150, blank=True)

    def __str__(self):
        return self.name
