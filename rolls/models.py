from django.db import models
from core import models as core_models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _

# Create your models here.


class Roll(core_models.TimeStampedModel):

    """Roll"""

    project = models.ForeignKey(
        "projects.Project", related_name="rolls", on_delete=models.SET_NULL, null=True
    )

    specific_design = models.OneToOneField("designs.SpecificDesign", related_name="rolls", on_delete=models.SET_NULL, blank=True, null=True)

    TYPE_SUB = "sub"
    TYPE_MAIN = "main"
    TYPE_CHOICES = ((TYPE_SUB, "SUB"), (TYPE_MAIN, "MAIN"))

    roll_type = models.CharField(choices=TYPE_CHOICES, max_length=10)

    body = models.OneToOneField(
        "materials.Material",
        related_name="rolls_body",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    steam_shaft = models.OneToOneField(
        "materials.Material",
        related_name="rolls_steam",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    gear_shaft = models.OneToOneField(
        "materials.Material",
        related_name="rolls_gear",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    def save(self, *args, **kwargs):
        if (
            self.body == self.steam_shaft
            or self.steam_shaft == self.gear_shaft
            or self.gear_shaft == self.body
        ) and self.body is not None:
            raise ValidationError(_("Multiple usage of a material"),)
        else:
            super().save(*args, **kwargs)  # call the real save method
