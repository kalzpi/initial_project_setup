from django.db import models
from core import models as core_models

# Create your models here.


class AbstractMaterial(core_models.TimeStampedModel):
    # pk가 있는데 아래의 serial no를 또 쓰는 이유: 외부 업체와 공유하여야 하는 고유 번호가 필요.
    serial = models.CharField(max_length=50, unique=True)
    name = models.CharField(max_length=255)

    class Meta:
        abstract = True

    def __str__(self):
        return self.serial


class Substrate(core_models.TimeStampedModel):

    """Roll Material에서 사용하기 위한 소재 재질을 모델화 하여 향후 유저가 추가 가능하도록 함"""

    name = models.CharField(max_length=20, default="Not defined")

    class Meta:
        verbose_name = "Substrate"

    def __str__(self):
        return self.name


class MaterialType(core_models.TimeStampedModel):
    name = models.CharField(max_length=50, unique=True)

    class Meta:
        verbose_name = "Material Type"


class Material(AbstractMaterial):

    """Material to manufactuing Rolls"""

    material_type = models.ForeignKey(
        "MaterialType",
        related_name="materials",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    # Material의 spec을 design의 foreign key로 연결하지 않는 이유: 실측 size가 기록되어야 함. 작업 후 변경된 치수가 기록되어야 함. 즉 소재의 실 치수가 입력되는 항목이므로 foreign key 사용하지 않음.


class RollMaterial(AbstractMaterial):
    substrate = models.ForeignKey(
        "Substrate", related_name="rollmaterials", on_delete=models.CASCADE
    )

    base_design = models.ForeignKey(
        "designs.PartsDesign",
        related_name="materials",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    # 향후 추가 될 항목이 너무 많아서 우선 charfield로 구성해둠
    status = models.CharField(max_length=150, default="입고대기")

    # purchasing app에서 base design + rule에 의거하여 아래 값들을 결정하고 채워넣을 것임.
    # 이후 입고 시 inspection에서 실제 size를 입력할 것임.
    # 생산 기록에 의해 입고 후 실제 size가 변경될 것임.
    outer_dia = models.FloatField()
    inner_dia = models.FloatField()

    ic_depth = models.FloatField()
    ic_hardness_min = models.IntegerField()
    ic_hardness_max = models.IntegerField()

    qt_hardness_min = models.IntegerField()
    qt_hardness_max = models.IntegerField()
