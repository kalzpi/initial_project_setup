import random
from django.core.management.base import BaseCommand
from django_seed import Seed
from clients import models as clients_models
from projects import models as projects_models
from users import models as users_models

app_name = "projects"


class Command(BaseCommand):

    help = f"This command will create the {app_name} with project name: [client name + flute_type + num_of_sets]"

    def add_arguments(self, parser):
        parser.add_argument(
            "--number",
            default=1,
            type=int,
            help=f"How many {app_name} do you want to create?",
        )

    def handle(self, *args, **options):
        number = options.get("number")
        seeder = Seed.seeder()
        all_clients = clients_models.Client.objects.all()
        seeder.add_entity(
            projects_models.Project,
            number,
            {
                "name": "Nonamed",
                "client": lambda x: random.choice(all_clients),
                "initiator": users_models.User.objects.get(pk=2),
            },
        )
        seeder.execute()
        a = projects_models.Project.objects.filter(name="Nonamed")
        all_flutes = [
            "A",
            "B",
            "C",
            "E",
            "F",
            "G",
        ]
        for projects in a:
            rename = f"{projects.client.name} {random.choice(all_flutes)}/F {random.randrange(1, 6, 1)} sets"
            projects.name = rename

            projects.save()

        self.stdout.write(self.style.SUCCESS(f"{number} {app_name} created!"))
