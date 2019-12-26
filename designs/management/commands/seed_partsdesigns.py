import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from designs import models as designs_models

app_name = "parts_designs"


class Command(BaseCommand):

    help = f"This command will create the {app_name} with project name:"

    # def add_arguments(self, parser):
    #     parser.add_argument(
    #         "--number",
    #         default=1,
    #         type=int,
    #         help=f"How many {app_name} do you want to create?",
    #     )

    def handle(self, *args, **options):
        designs = [
            ("Agnati", "Master"),
            ("BHS", "AF-P"),
            ("BHS", "MF-B"),
            ("BHS", "MF-P"),
            ("BHS", "QF-P"),
            ("FOSBER", "Edge"),
            ("FOSBER", "Smart"),
            ("Gherardi", "Gheradi"),
            ("HSIEH HSU", "MSF-30P"),
            ("HSIEH HSU", "MSF-30PA"),
            ("HSIEH HSU", "MSF-35P"),
            ("HSIEH HSU", "SF-20N"),
            ("HSIEH HSU", "SF-25NB"),
            ("ISOWA", "CF-40"),
            ("ISOWA", "CF-60"),
            ("K&H", "SF-12V"),
            ("Langston", "Langston 380"),
            ("Langston", "Langston XD"),
            ("Massenzana", "OC200"),
            ("Massenzana", "OC300"),
            ("MHI", "50C"),
            ("MHI", "50E"),
            ("MHI", "50F"),
            ("MHI", "50E-II"),
            ("MHI", "50F-II"),
            ("MHI", "60G"),
            ("MWU", "SFM"),
            ("MWU", "SFB"),
            ("NIWA", "SF-18"),
        ]

        body_types = [
            "SUB",
            "MAIN",
        ]

        shaft_types = [
            "S/S",
            "S/G",
            "M/S",
            "M/G",
        ]

        for design in designs:
            temp_outer_dia = random.randrange(300, 500, 5)
            temp_inner_dia = random.randrange(150, 200, 5)
            temp_shaft_od = temp_inner_dia + 10

            for body_type in body_types:
                designs_models.PartsDesign.objects.create(
                    part_type="body",
                    model_name=f"{design[0]} {design[1]} {body_type}",
                    outer_dia=temp_outer_dia,
                    inner_dia=temp_inner_dia,
                    length=random.randrange(2000, 3000, 10),
                )

            for shaft_type in shaft_types:
                designs_models.PartsDesign.objects.create(
                    part_type="shaft",
                    model_name=f"{design[0]} {design[1]} {shaft_type}",
                    outer_dia=temp_shaft_od,
                    length=random.randrange(400, 600, 10),
                )

        self.stdout.write(self.style.SUCCESS(f"{app_name} created!"))
