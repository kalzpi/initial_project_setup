from django.core.management.base import BaseCommand
from designs import models as designs_models

app_name = "designs"


class Command(BaseCommand):

    help = f"This command will create the {app_name} with project name: [client name + flute_type + num_of_sets]"

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

        for design in designs:
            filterset = designs_models.PartsDesign.objects.filter(
                model_name__startswith=f"{design[0]} {design[1]}"
            )
            maker = designs_models.Company.objects.get(name=design[0])
            designs_models.Design.objects.create(
                name=design[1],
                company=maker,
                sub_body=filterset[0],
                sub_steam_shaft=filterset[2],
                sub_gear_shaft=filterset[3],
                main_body=filterset[1],
                main_steam_shaft=filterset[4],
                main_gear_shaft=filterset[5],
            )

        self.stdout.write(self.style.SUCCESS(f"{app_name} created!"))
