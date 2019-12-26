from django.db import models
from django.utils import timezone
from core import models as core_models


class DefectReport(core_models.TimeStampedModel):
    issued_date = models.DateField(default=timezone.now)
    issued_by = models.ForeignKey(
        "users.User",
        related_name="defect_reports",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )
    material = models.ForeignKey(
        "materials.RollMaterial",
        related_name="defect_reports",
        on_delete=models.CASCADE,
    )

    TYPE_IC_CRACK = "ic_crack"
    TYPE_SPEC_DEVIATION = "deviation"
    TYPE_MACRO_STREAK_FLOW = "macro"
    TYPE_FAULT_OVERCUT = "overcutted"
    TYPE_FAULT = "fault"
    TYPE_CHOICES = (
        (TYPE_IC_CRACK, "induction hardening crack"),
        (TYPE_SPEC_DEVIATION, "spec deviation"),
        (TYPE_MACRO_STREAK_FLOW, "macro streak flow"),
        (TYPE_FAULT_OVERCUT, "overcutted"),
        (TYPE_FAULT, "manufacturing fault"),
    )

    defect_type = models.CharField(choices=TYPE_CHOICES, max_length=255)

    description = models.TextField()
    photo = models.FileField(upload_to="defect/photos/")

    is_acceptable = models.BooleanField(default=False)

    # 결함 종류. 작업불량, 소지흠, 저주파크랙, 치수 오류


class InspectionReport(core_models.TimeStampedModel):
    issued_date = models.DateField(default=timezone.now)
    issued_by = models.ForeignKey(
        "users.User",
        related_name="inspection_reports",
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
    )

    material = models.ManyToManyField(
        "materials.RollMaterial", related_name="inspection_reports"
    )

    heat_no = models.CharField(max_length=20, blank=True, null=True)
    outer_dia_min = models.FloatField(blank=True, null=True)
    outer_dia_max = models.FloatField(blank=True, null=True)
    innder_dia = models.FloatField(blank=True, null=True)
    length = models.FloatField(blank=True, null=True)
    hardness_by_vendor00 = models.FloatField(blank=True, null=True)
    hardness_by_vendor01 = models.FloatField(blank=True, null=True)
    hardness_by_vendor02 = models.FloatField(blank=True, null=True)
    hardness_by_vendor03 = models.FloatField(blank=True, null=True)
    hardness_by_vendor04 = models.FloatField(blank=True, null=True)
    hardness_by_vendor05 = models.FloatField(blank=True, null=True)
    hardness_by_vendor06 = models.FloatField(blank=True, null=True)
    hardness_by_vendor07 = models.FloatField(blank=True, null=True)
    hardness_by_vendor08 = models.FloatField(blank=True, null=True)
    hardness_by_vendor09 = models.FloatField(blank=True, null=True)
    hardness_by_src00 = models.FloatField(blank=True, null=True)
    hardness_by_src01 = models.FloatField(blank=True, null=True)
    hardness_by_src02 = models.FloatField(blank=True, null=True)
    hardness_by_src03 = models.FloatField(blank=True, null=True)
    hardness_by_src04 = models.FloatField(blank=True, null=True)
    thickness_upper_0 = models.FloatField(blank=True, null=True)
    thickness_upper_90 = models.FloatField(blank=True, null=True)
    thickness_upper_180 = models.FloatField(blank=True, null=True)
    thickness_upper_270 = models.FloatField(blank=True, null=True)
    thickness_bottom_0 = models.FloatField(blank=True, null=True)
    thickness_bottom_90 = models.FloatField(blank=True, null=True)
    thickness_bottom_180 = models.FloatField(blank=True, null=True)
    thickness_bottom_270 = models.FloatField(blank=True, null=True)

    tag_photo = models.FileField(blank=True, null=True, upload_to="reports/inspection/")
    is_acceptable = models.BooleanField(default=False)
