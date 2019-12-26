from django.contrib.auth.models import AbstractUser
from django.db import models


# Create your models here.
class User(AbstractUser):

    """Custom User Model"""

    LANGUAGE_KOREAN = "kr"
    LANGUAGE_ENGLISH = "en"
    LANGUAGE_CHOICES = ((LANGUAGE_KOREAN, "Korean"), (LANGUAGE_ENGLISH, "English"))

    language = models.CharField(
        choices=LANGUAGE_CHOICES, max_length=2, default=LANGUAGE_KOREAN
    )
