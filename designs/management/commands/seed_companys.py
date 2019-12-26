from django.core.management.base import BaseCommand
from designs import models as designs_models

app_name = "company"


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
        companies = [
            "Agnati",
            "BHS",
            "FOSBER",
            "Gherardi",
            "HSIEH HSU",
            "ISOWA",
            "K&H",
            "Langston",
            "Massenzana",
            "MHI",
            "MWU",
            "NIWA",
        ]
        for company in companies:
            designs_models.Company.objects.create(name=company)
        self.stdout.write(self.style.SUCCESS(f"{app_name} created!"))
