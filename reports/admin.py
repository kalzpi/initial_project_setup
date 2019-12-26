from django.contrib import admin
from . import models

# Register your models here.


@admin.register(models.DefectReport)
class DefectReportAdmin(admin.ModelAdmin):
    list_display = [
        "issued_date",
        "issued_by",
        "material",
        "defect_type",
        "description",
        "photo",
        "is_acceptable",
    ]


@admin.register(models.InspectionReport)
class InspectionReportAdmin(admin.ModelAdmin):
    list_display = [
        "issued_date",
        "issued_by",
        "heat_no",
        "outer_dia_min",
        "outer_dia_max",
        "innder_dia",
        "length",
        "tag_photo",
        "is_acceptable",
    ]
