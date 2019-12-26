from django.db import models
from core import models as core_models


class AbstractItem(core_models.TimeStampedModel):

    """ Abstract Items """

    name = models.CharField(max_length=80)

    class Meta:
        abstract = True

    def __str__(self):
        return self.name


class Company(AbstractItem):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name_plural = "Companies"


class PartsDesign(core_models.TimeStampedModel):

    # PART를 Body와 Shaft로 나눈 이유는, 나중에 발주 시 Design에서 사용한 Partial Design을 참조할텐데, 이 때 part_name이 shaft면 축 황삭도면을 발주서에 첨부해야 하고 body면 도면을 발주서에 첨부하지 않아야 하기 때문이다.
    PART_BODY = "body"
    PART_SHAFT = "shaft"
    PART_CHOICES = ((PART_BODY, "Body"), (PART_SHAFT, "Shaft"))

    model_name = models.CharField(max_length=200)
    part_type = models.CharField(choices=PART_CHOICES, max_length=10)
    outer_dia = models.FloatField()
    inner_dia = models.FloatField(blank=True, null=True)
    length = models.FloatField()
    cutback = models.FloatField(blank=True, null=True)
    drawing = models.FileField(upload_to="designs/partial/")

    def save(self, *args, **kwargs):

        """
        추가될 것
        이미 존재하는 PartsDesign objects 중 outer_dia, inner_dia, length, cutback이 동일한 소재가 있는지 검색
        검색결과가 있으면 User에게 해당 object를 보여주며, 상호 호환이 불가능 한지 질문하고 가능할 시에는 save해주지 않고 기존 object를 검색하여 이름을 수정해라고 권한다.
        상호 다른 소재라면 그대로 save해준다.
        """

        super().save(*args, **kwargs)  # Call the real save() method

    def __str__(self):
        return self.model_name


class Design(core_models.TimeStampedModel):

    """Roll Design"""

    name = models.CharField(max_length=150, unique=True)
    company = models.ForeignKey(
        "Company",
        related_name="designs",
        on_delete=models.CASCADE,
        blank=True,
        null=True,
    )

    sub_body = models.ForeignKey(
        "PartsDesign",
        related_name="designs_sub_body",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    sub_steam_shaft = models.ForeignKey(
        "PartsDesign",
        related_name="designs_sub_steam_shaft",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )
    sub_gear_shaft = models.ForeignKey(
        "PartsDesign",
        related_name="designs_sub_gear_shaft",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    main_body = models.ForeignKey(
        "PartsDesign",
        related_name="designs_main_body",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    main_steam_shaft = models.ForeignKey(
        "PartsDesign",
        related_name="designs_main_steam_shaft",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    main_gear_shaft = models.ForeignKey(
        "PartsDesign",
        related_name="designs_main_gear_shaft",
        on_delete=models.PROTECT,
        blank=True,
        null=True,
    )

    def __str__(self):
        return self.name


class SpecificDesign(core_models.TimeStampedModel):
    project = models.ForeignKey(
        "projects.Project",
        related_name="designs",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    base_design = models.ForeignKey(
        "Design", related_name="SpecificDesign", on_delete=models.PROTECT
    )
    drawing = models.FileField(upload_to="designs/specific/")
    lot_no = models.CharField(max_length=50, unique=True)
    finish_od = models.FloatField(blank=True, null=True)
    od_tolerance = models.FloatField(blank=True, null=True)

    number_of_teeth = models.FloatField(blank=True, null=True)
    flute_type = models.CharField(max_length=10, blank=True, null=True)
    flute_height = models.FloatField(blank=True, null=True)
    flute_height_tolerance = models.FloatField(blank=True, null=True)

    pitch = models.FloatField(blank=True, null=True)
    radius_1 = models.FloatField(blank=True, null=True)
    radius_1_tolerance = models.FloatField(blank=True, null=True)
    radius_2 = models.FloatField(blank=True, null=True)
    radius_2_tolerance = models.FloatField(blank=True, null=True)
    take_up_ratio = models.FloatField(blank=True, null=True)
    crown = models.FloatField(blank=True, null=True)
    crown_tolerance = models.FloatField(blank=True, null=True)
