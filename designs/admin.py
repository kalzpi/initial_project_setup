from django.contrib import admin
from . import models


# Register your models here.
@admin.register(models.Company)
class CompanyAdmin(admin.ModelAdmin):
    list_display = ["name"]


@admin.register(models.PartsDesign)
class PartsDesignAdmin(admin.ModelAdmin):
    list_display = [
        "model_name",
        "part_type",
        "outer_dia",
        "inner_dia",
        "length",
    ]


@admin.register(models.Design)
class DesignAdmin(admin.ModelAdmin):
    list_display = [
        "name",
        "company",
        "sub_body",
        "sub_steam_shaft",
        "sub_gear_shaft",
        "main_body",
        "main_steam_shaft",
        "main_gear_shaft",
    ]


@admin.register(models.SpecificDesign)
class SpecificDesignAdmin(admin.ModelAdmin):
    list_display = [
        "project",
        "base_design",
        "drawing",
        "lot_no",
        "finish_od",
        "od_tolerance",
        "number_of_teeth",
        "flute_type",
        "flute_height",
        "flute_height_tolerance",
        "pitch",
        "radius_1",
        "radius_1_tolerance",
        "radius_2",
        "radius_2_tolerance",
        "take_up_ratio",
        "crown",
        "crown_tolerance",
    ]

